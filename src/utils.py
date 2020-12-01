#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import json
import os
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def stratified_train_test_split(
    df: pd.DataFrame, column: str, test_size: float = 0.2
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Create stratified train-test split sampling on the given pandas datafram
    based on the column given.

    Parameters
    ----------
    df : pandas.DataFrame
        The pandas dataframe to perform the train-test split upon
    column : str
        The column to group by the different possible values.

    Returns
    -------
    TODO

    """
    stratified_test = df.groupby("label").apply(lambda x: x.sample(frac=test_size))

    return (
        df[~df.apply(tuple, 1).isin(stratified_test.apply(tuple, 1))].reset_index(
            drop=True
        ),
        stratified_test.reset_index(drop=True),
    )


if __name__ == "__main__":
    stratified_mnist_train, stratified_mnist_test = stratified_train_test_split(
        pd.read_csv(os.path.join("data", "raw", "mnist.csv")), "label"
    )

    stratified_mnist_train.to_csv(
        os.path.join("data", "processed", "mnist_train.csv"), index=False
    )
    stratified_mnist_test.to_csv(
        os.path.join("data", "processed", "mnist_test.csv"), index=False
    )

    (
        stratified_fashion_mnist_train,
        stratified_fashion_mnist_test,
    ) = stratified_train_test_split(
        pd.read_csv(os.path.join("data", "raw", "fashion-mnist.csv")), "label"
    )

    stratified_fashion_mnist_train.to_csv(
        os.path.join("data", "processed", "fashion-mnist_train.csv"), index=False
    )
    stratified_fashion_mnist_test.to_csv(
        os.path.join("data", "processed", "fashion-mnist_test.csv"), index=False
    )
