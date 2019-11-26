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

* [Matplotlib](https://matplotlib.org/) - a library to generate charts from data sets
* [Pandas](https://pandas.pydata.org/) - a library providing high-performance, easy-to-use data structures and data analysis tools
* [Numpy](https://numpy.org/) - a library providing support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions
* [Scipy](https://www.scipy.org/) - a library used for scientific computing and technical computing
* [Pathlib](https://docs.python.org/3/library/pathlib.html) - offers a set of classes to handle filesystem paths

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path
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
        custom_ylabel='#',
        custom_day_interval=1
    )
    bucket_test.render()
    bucket_test.compute_pvalues()
```

### Arguments

* `df` - data frame to be used for the bucket test. It is recommended to group the data frame before passing it (e.g.: When doing a bucket test on the group `design`, you should group the data frame by design and date first)
* `y_axis` - specifies the values on the y_axis for the chart and statistical significance check
* `group` - the name of the column which the data frame is grouped by
* `x_axis` (default: `date`) - specifies the values on the x_axis for the chart
* `custom_title` (default: `y_axis`) - specifies the title for the chart

### Screenshots

A generated chart and statistical significance analysis example:

<p align="center">
  <img width="100%" src="example/example_impressions_by_group.png" />
</p>

## Next steps

* Customize the number of groups that are taken into account A/B/C testings, A/B/C/D testings, A/B/C/D/E testings.
* Group data frame so that it can be given to `bucket_test.render()`
* Render charts and compute p-values for data from more than one data frame
* Create tests for `render` and `compute_pvalue` methods
* Handle other `x_axis` that date only

## How to contribute

You can contribute by creating a new branch on the repository and a PR 

## Contributors

The method for checking statistical significance was highly inspired by the work of **Paulina Gralak [@Loczi94](https://github.com/Loczi94)**.
Thank a lot!
