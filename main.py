#!/usr/bin/env python3

from bucket_test import TestType, BucketTest


def main():
    bucket_test = BucketTest(
        test_type=TestType.ABTESTING,
        y_axis="CTR",
        category_name="design",
        filter_name="device",
        categories={
            'A': ['10303394', '03948402', '30495043', '30495906'],
            'B': ['04342343', '64748877', '33677675', '98657939'],
        },
        x_axis="date",
    )

    bucket_test.render()

    bucket_test.compute_pvalues()
