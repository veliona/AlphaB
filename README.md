# AlphaB

## Python library for rendering charts and computing statistics for A/B testing

### Current state

This library is in the very initial state. Currently, it supports only A/B testings (two groups).

### AlphaB allows you to:

* Automatically generate charts from A/B testings
* Compute statistics in order to confirm a statistical significance between groups


<!-- <p align="center"><img src="images/AlphaB.png" width="250"/></p> -->

## Table of content

* [Requirements](#requirements)
* [How to use it](#how-to-use-it)

## Requirements

You can directly install all of the requirements for AlphaB by running `pip install -r requirements.txt` from the root of the repository.

### Matplotlib

AlphaB uses the [Matplotlib](https://matplotlib.org/) library in order to generate charts from data sets.


```python
import matplotlib.pyplot as plt
```

## How to use it

It is highly recommended to use [Jupyter](https://jupyter.org/) to perform A/B testing analysis in Python, and AlphaB is built to be used in Jupyter Notebooks. 

Here is an example usage for AlphaB (this example doesn't include specifying a data set for now):

```python
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
```

## Next steps

* Customize the number of groups that are taken into account A/B/C testings, A/B/C/D testings, A/B/C/D/E testings.
* Group data frame so that it can be given to `bucket_test.render()`
* Render charts and compute p-values for data from more than one data frame



## Contributors

The method for checking statistical significance was highly inspired by the work of **Paulina Gralak @Loczi94**.
Thank a lot! :) 

