# AlphaB

## Python library for rendering charts and computing statistics for A/B testing

### Current state

This library is in the very initial state. 

### AlphaB allows you to:

* Automatically generate charts from bucket testing
* Compute statistics in order to confirm a statistical significance between groups
* Customize the number of groups that are taken into account `ABTESTING`, `ABCTESTING`, `ABCDTESTING` etc.

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
```