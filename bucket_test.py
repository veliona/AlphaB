#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import shapiro
from scipy.stats import ttest_ind
from scipy.stats import f
from scipy.stats import mannwhitneyu


class BucketTest:
    """ BucketTest class computes and renders charts and statistics for bucket testing. """

    def __init__(self, df: pd.DataFrame, y_axis: str, group: str, x_axis='date', custom_title=""):
        """ Create a new bucket test with the given attributes """
        self.df = df
        self.y_axis = y_axis
        self.x_axis = x_axis
        self.group = group
        self.custom_title = custom_title
        # TODO: Set time interval (each day, each week, etc.)
        # TODO: Custom y_label value (ex. [%])

    def render(self, figure_size_x=12, figure_size_y=5, line_width=3, title_font_size=16, legend_font_size=14):
        """ Render renders the charts representing the bucket test """

        fig, ax = plt.subplots(figsize=(figure_size_x, figure_size_y))
        for group_value in self.df[self.group].unique():
            df = self.df[self.df[self.group] == group_value]
            df.set_index(self.x_axis, drop=False, inplace=True)
            ax.plot(df[self.y_axis], label=group_value, linewidth=line_width)
        # TODO: Improve title to be `per groups[0] and group[1]...` and so on.

        if self.custom_title != "":
            plt.title(self.custom_title, fontsize=title_font_size)
        else:
            plt.title('{} per {}'.format(self.y_axis, self.group), fontsize=title_font_size)
        plt.legend(bbox_to_anchor=(1.3, 0.8), frameon=False, fontsize=legend_font_size)

        # plt.ylabel('[#]')
        plt.ylim(0, )
        plt.xticks(rotation=30);
        self.__set_locator_and_formatter__(ax)
        plt.show()

    def __set_locator_and_formatter__(self, ax):
        # TODO: Set major locator and formatter for x_axis
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    def compute_pvalues(self):
        """ ComputePValues computes all pvalues, variance etc. for each combination of categories within
        the bucket test and renders a table containing the results """
        # Create a list with unique values from a dataframe
        values_df_group = self.df[self.group].unique()

        # normality
        normality_group_a = shapiro(self.df[self.df[self.group] == values_df_group[0]][self.y_axis])
        normality_group_b = shapiro(self.df[self.df[self.group] == values_df_group[1]][self.y_axis])
        print('Shapiro group A p-value: ', normality_group_a)
        print('Shapiro group B p-value: ', normality_group_b)

        # variance
        F = np.var(self.df[self.df[self.group] == values_df_group[0]][self.y_axis]) / np.var(
            self.df[self.df[self.group] == values_df_group[1]][self.y_axis])
        df_group_a = len(self.df[self.df[self.group] == values_df_group[0]][self.y_axis]) - 1
        df_group_b = len(self.df[self.df[self.group] == values_df_group[1]][self.y_axis]) - 1
        f_pvalue = f.cdf(F, df_group_a, df_group_b)
        print('F test p-value: ', f_pvalue)

        if (normality_group_a[1] > 0.01 and normality_group_b[1] > 0.01 and f_pvalue > 0.01):
            # T-test
            ttest_pvalue = ttest_ind(self.df[self.df[self.group] == values_df_group[0]][self.y_axis],
                                     self.df[self.df[self.group] == values_df_group[1]][self.y_axis]).pvalue
            print('T-test p-value: ', ttest_pvalue)
            print("Statistical significance: ", ttest_pvalue <= 0.01)
        elif (normality_group_a[1] > 0.01 and normality_group_b[1] > 0.01 and f_pvalue <= 0.01):
            # Welch's test
            welch_pvalue = ttest_ind(self.df[self.df[self.group] == values_df_group[0]][self.y_axis],
                                     self.df[self.df[self.group] == values_df_group[1]][self.y_axis],
                                     equal_var=False).pvalue
            print('T-test p-value: ', welch_pvalue)
            print("Statistical significance: ", welch_pvalue <= 0.01)
        else:
            # Mann-Whitney U test
            mannwhitneyu_pvalue = mannwhitneyu(self.df[self.df[self.group] == values_df_group[0]][self.y_axis],
                                               self.df[self.df[self.group] == values_df_group[1]][self.y_axis]).pvalue
            print('Mann-Whitney U test: ', mannwhitneyu_pvalue)
            print("Statistical significance: ", mannwhitneyu_pvalue <= 0.01)

