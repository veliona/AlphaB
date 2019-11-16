#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


class BucketTest:
    """ BucketTest class computes and renders charts and statistics for bucket testing. """

    def __init__(self, y_axis: str, category_name: str, filter_name: str, categories: dict, x_axis="date"):
        """ Create a new bucket test with the given attributes """
        # TODO: This should take and set a pd.Dataframe.
        self.y_axis = y_axis
        self.x_axis = x_axis
        self.category_name = category_name
        self.filter_name = filter_name
        self.categories = categories
        # TODO: Call all groupby functions with self.

    def render(self, figure_size_x=12, figure_size_y=5, line_width=3, title_font_size=16, legend_font_size=14):
        """ Render renders the charts representing the bucket test """
        plt.subplots(figsize=(figure_size_x, figure_size_y))

        self.__build_chart_axis__(line_width)

        plt.title('{self.y_axis} per {self.category_name} for {filter_name}', fontsize=title_font_size)
        plt.legend(bbox_to_anchor=(1.3, 0.8), frameon=False, fontsize=legend_font_size, title=self.category_name)
        plt.ylabel(self.y_axis)

        # TODO: Calculate ylim
        # plt.ylim(0, 7000)

        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=30)
        plt.show()

    def compute_pvalues(self):
        """ ComputePValues computes all pvalues, variance etc. for each combination of categories within
        the bucket test and renders a table containing the results """
        # TODO: Compute PValue between A-B, A-C, B-C, etc.
        print("not implemented")

    def __build_chart_axis__(self, line_width, category):
        # TODO: Logic to put data into plot
        # for category in self.categories.unique():
        #    df_plot_category = df_category[df_category[category] == category]
        #    df_plot_category.set_index('date', inplace=True)
        #    ax.plot(df_plot_category[self.filter_name], label=category, linewidth=line_width)

    def __set_locator_and_formatter__(self):
        # TODO: Set major locator and formatter for x_axis
        print("not implemented")
        # ax.x_axis.set_major_locator(mdates.DayLocator(interval=15))
        # ax.x_axis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))


def GroupBy(column_name: str, groups: dict):
    """ Calls group by with the given arguments """
    def groupBy(test: BucketTest):
        # groupBy is in the scope of GroupBy so it has access to the column name and groups.
        # TODO: Call groupBy on the dataframe with the given arguments
        # TODO: Set the groups and grouped column names in the BucketTest as attributes.
        # TODO: Return the grouped dataframe
    return groupBy