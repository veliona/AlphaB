#!/usr/bin/env python3

from alphab import BucketTest
import pandas as pd


def main():
    df = pd.DataFrame()
    bucket_test = BucketTest(
        df=df,
        y_axis='impressions',
        group='design',
        x_axis='date',
        custom_title='Impressions by design',
        custom_ylabel='#',
        custom_day_interval=1
    )
    bucket_test.render()
    bucket_test.compute_pvalues()
