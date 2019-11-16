#!/usr/bin/env python3

from bucket_test import BucketTest, GroupBy


def main():
    bucket_test = BucketTest(
        #dataframe=df,
        y_axis="CTR",
        # category_name="design",
        filter_name="device",
        # categories={
        #     'A': ['10303394', '03948402', '30495043', '30495906'],
        #     'B': ['04342343', '64748877', '33677675', '98657939'],
        # },
        x_axis="date",
        GroupBy(column_name="design", groups={
                'old': ['10303394', '03948402', '30495043', '30495906'],
                'new': ['04342343', '64748877', '33677675', '98657939'],
        }),
        GroupBy(column_name="device", groups={
                'desktop': ['desktop'],
                'mobile': ['mobile'],
        }),
    )

    bucket_test.render()

    bucket_test.compute_pvalues()
