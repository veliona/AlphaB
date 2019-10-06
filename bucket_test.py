#!/usr/bin/env python3

from enum import Enum
import matplotlib.pyplot as plt


class TestType(Enum):
    ABTESTING = 1
    ABCTESTING = 2
    ABCDTESTING = 3
    ABCDETESTING = 4


class BucketTest:
    """ BucketTest class computes and renders charts and statistics for bucket testing. """

    def __init__(self, test_type: TestType, y_axis: str, category_name: str, filter_name: str, categories: dict, x_axis="date"):
        """ Create a new bucket test with the given attributes """
        self.test_type = test_type
        self.y_axis = y_axis
        self.x_axis = x_axis
        self.category_name = category_name
        self.filter_name = filter_name
        self.categories = categories

    def render(self, figure_size_x=12, figure_size_y=5, line_width=3, title_font_size=16, legend_font_size=14):
        """ Render renders the charts representing the bucket test """
        plt.subplots(figsize=(figure_size_x, figure_size_y))

        self.__build_chart_axis__(line_width)

        plt.title('{self.y_axis} per {self.category_name} for {filter_name}', fontsize=title_font_size)
        plt.legend(bbox_to_anchor=(1.3, 0.8), frameon=False, fontsize=legend_font_size)
        plt.ylabel(self.y_axis)

        # TODO: Calculate ylim
        # plt.ylim(0, 7000)

        plt.xticks(rotation=30)
        plt.show()

    def compute_pvalues(self):
        """ ComputePValues computes all pvalues, variance etc. for each combination of categories within
        the bucket test and renders a table containing the results """
        # TODO: Compute PValue between A-B, A-C, B-C, etc.
        print("not implemented")

    def __build_chart_axis__(self, line_width):
        # TODO: Logic to put data into plot
        print("not implemented")
        # for category in self.categories:
        #   for wiki in df_wiki['wiki'].unique():
        #   df_plot_wiki = df_wiki[df_wiki['wiki'] == wiki]
        #   df_plot_wiki.set_index('date', inplace=True)
        #   ax.plot(df_plot_wiki['impressions'], label=wiki, linewidth=line_width)

    def __set_locator_and_formatter__(self):
        # TODO: Set major locator and formatter for x_axis
        print("not implemented")
        # ax.x_axis.set_major_locator(mdates.DayLocator(interval=15))
        # ax.x_axis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))