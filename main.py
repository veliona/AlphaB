#!/usr/bin/env python3

from bucket_test import BucketTest, GroupBy
import pandas as pd


def main():
    df = pd.DataFrame()

    bucket_test = BucketTest(
        df=df,
        y_axis='impressions',
        groups=['design', 'device'],
        x_axis='date',
    )

    bucket_test.render()

    bucket_test.compute_pvalues()
