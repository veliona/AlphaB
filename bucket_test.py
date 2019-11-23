#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


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
        # normality
        normality_princesses_pvalue = shapiro(df_princesses)[1]
        normality_heroes_pvalue = shapiro(df_heroes)[1]
        print('Shapiro princesses p-value: ', normality_princesses_pvalue)
        print('Shapiro heroes p-value: ', normality_heroes_pvalue)

        # variance
        F = np.var(df_princesses) / np.var(df_heroes)
        df_p = len(df_princesses) - 1
        df_h = len(df_heroes) - 1
        f_pvalue = f.cdf(F, df_p_o, df_h_o)
        print('F p-value: ', f_pvalue)

        if (normality_princesses_pvalue > 0.05 and normality_heroes_pvalue > 0.05 and f_pvalue > 0.05):
            # test
            test_pvalue = ttest_ind(df_princesses, df_heroes).pvalue
            print('Test p-value: ', test_pvalue)
            return (test_pvalue <= 0.05)
        else:
            # Mann-Whitney U test
            mannwhitneyu_pvalue = mannwhitneyu(df_princesses, df_heroes).pvalue
            print('Mann-Whitney U test: ', mannwhitneyu_pvalue)
            return (mannwhitneyu_pvalue <= 0.05)

    def __set_locator_and_formatter__(self, ax):
        # TODO: Set major locator and formatter for x_axis
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
