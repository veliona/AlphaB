#!/usr/bin/env python3

from bucket_test import BucketTest, GroupBy
import pandas as pd



def main():
    df = pd.DataFrame()
    bucket_test = BucketTest(
        df=df[df['device'] == 'mobile'],
        y_axis='impressions',
        group='design',
        x_axis='date',
        custom_title='Impressions by design for mobile',
    )
    bucket_test.render()
    bucket_test.compute_pvalues()
