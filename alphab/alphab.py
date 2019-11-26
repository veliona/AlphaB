#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import ttest_ind
from scipy.stats import f
from scipy.stats import mannwhitneyu


class BucketTest:
    """ BucketTest class computes and renders charts and statistics for bucket testing """

    def __init__(self, df: pd.DataFrame, variable: str, group: str, x_axis='date', custom_title="", custom_day_interval=1,
                 custom_ylabel=""):
        """ Create a new bucket test with the given attributes """
        self.df = df
        self.variable = variable
        self.x_axis = x_axis
        self.group = group
        self.custom_title = custom_title
        self.custom_day_interval = custom_day_interval
        self.custom_ylabel = custom_ylabel

    def render(self, figure_size_x=12, figure_size_y=5, line_width=3, title_font_size=16, legend_font_size=14):
        """ Render renders the charts representing the bucket test """

        fig, ax = plt.subplots(figsize=(figure_size_x, figure_size_y))
        for group_value in self.df[self.group].unique():
            df = self.df[self.df[self.group] == group_value]
            df.set_index(self.x_axis, drop=False, inplace=True)
            ax.plot(df[self.variable], label=group_value, linewidth=line_width)

        # Title customization
        if self.custom_title != "":
            plt.title(self.custom_title, fontsize=title_font_size)
        else:
            plt.title('{} per {}'.format(self.variable, self.group), fontsize=title_font_size)
        plt.legend(bbox_to_anchor=(1.3, 0.8), frameon=False, fontsize=legend_font_size)

        # Y-label customization
        if self.custom_ylabel != "":
            plt.ylabel(self.custom_ylabel)
        else:
            plt.ylabel(self.variable)

        plt.ylim(0, )
        plt.xticks(rotation=30)
        self.__set_locator_and_formatter__(ax)
        plt.show()
        plt.savefig(Path("Chart"))

    def __set_locator_and_formatter__(self, ax):
        # Major locator customization
        if self.custom_day_interval != 1:
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=self.custom_day_interval))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    def compute_pvalues(self):
        """ ComputePValues computes all pvalues, variance etc. for each combination of categories within
        the bucket test and renders a table containing the results """
        # Create a list with unique values from a data frame
        values_df_group = self.df[self.group].unique()

        # Create variables for group A and B
        group_a = self.df[self.df[self.group] == values_df_group[0]][self.variable]
        group_b = self.df[self.df[self.group] == values_df_group[1]][self.variable]

        # normality
        normality_group_a = shapiro(group_a)
        normality_group_b = shapiro(group_b)
        print('Shapiro group A p-value: ', normality_group_a[1])
        print('Shapiro group B p-value: ', normality_group_b[1])

        # variance
        F = np.var(group_a) / np.var(group_b)
        critical_value_group_a = len(group_a) - 1
        critical_value_group_b = len(group_b) - 1
        f_pvalue = f.cdf(F, critical_value_group_a, critical_value_group_b)
        print('F test p-value: ', f_pvalue)

        if (normality_group_a[1] and normality_group_b > 0.01[1]) and f_pvalue > 0.01:
            # T-test
            ttest_pvalue = ttest_ind(group_a, group_b).pvalue
            print('T-test p-value: ', ttest_pvalue)
            print("Statistical significance: ", ttest_pvalue <= 0.01)
        elif (normality_group_a[1] and normality_group_b > 0.01[1]) and f_pvalue <= 0.01:
            # Welch's test
            welch_pvalue = ttest_ind(group_a, group_b, equal_var=False).pvalue
            print('T-test p-value: ', welch_pvalue)
            print("Statistical significance: ", welch_pvalue <= 0.01)
        else:
            # Mann-Whitney U test
            mannwhitneyu_pvalue = mannwhitneyu(group_a, group_b).pvalue
            print('Mann-Whitney U test: ', mannwhitneyu_pvalue)
            print("Statistical significance: ", mannwhitneyu_pvalue <= 0.01)
