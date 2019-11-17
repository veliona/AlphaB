#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


class BucketTest:
    """ BucketTest class computes and renders charts and statistics for bucket testing. """

    def __init__(self, df: pd.DataFrame, y_axis: str, groups: list, x_axis="date"):
        """ Create a new bucket test with the given attributes """
        self.df = df
        self.y_axis = y_axis
        self.x_axis = x_axis
        self.groups = groups
        # TODO: Set time interval (each day, each week, etc.)
        # TODO: Custom y_label value (ex. [%])


    def render(self, figure_size_x=12, figure_size_y=5, line_width=3, title_font_size=16, legend_font_size=14):
        """ Render renders the charts representing the bucket test """
        fig, ax = plt.subplots(figsize=(figure_size_x, figure_size_y))

        # TODO: Improve title to be `per groups[0] and group[1]...` and so on.
        plt.title('{} per {}'.format(self.y_axis, self.groups), fontsize=title_font_size)
        plt.legend(bbox_to_anchor=(1.3, 0.8), frameon=False, fontsize=legend_font_size)
        plt.ylabel(self.y_axis)

        for group_one_value in self.df[self.group[0]].unique():
            self.df = self.df[self.df[self.group[0]] == group_one_value]
            if len(self.group) > 1:
                for group_two_value in self.df[self.group[1]].unique():
                    self.df = self.df[self.df[self.group[1]] == group_two_value]
                    self.df.set_index(self.x_axis, inplace=True)
                    ax.plot(self.df[self.y_axis], label=group_two_value, line_width=line_width)

        # plt.ylabel('[%]')
        plt.ylim(0, max(self.y_axis))
        plt.xticks(rotation=30);
        self.__set_locator_and_formatter__(ax)
        plt.show()

    def compute_pvalues(self):
        """ ComputePValues computes all pvalues, variance etc. for each combination of categories within
        the bucket test and renders a table containing the results """
        # TODO: Compute PValue between A-B, A-C, B-C, etc.
        print("not implemented")

    def __set_locator_and_formatter__(self, ax):
        # TODO: Set major locator and formatter for x_axis
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
