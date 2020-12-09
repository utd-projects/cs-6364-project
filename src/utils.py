#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import json
import os
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    mnist_df = pd.read_csv(os.path.join("data", "raw", "mnist.csv"))
    stratified_mnist_train, stratified_mnist_test = train_test_split(
        pd.read_csv(os.path.join("data", "raw", "mnist.csv")),
        test_size=0.2,
        stratify=mnist_df["label"],
    )
    del mnist_df

    stratified_mnist_train, stratified_mnist_val = train_test_split(
        stratified_mnist_train,
        train_size=0.875,
        stratify=stratified_mnist_train["label"],
    )

    print(stratified_mnist_train)
    print(stratified_mnist_val)
    print(stratified_mnist_test)

    stratified_mnist_train.to_csv(
        os.path.join("data", "processed", "mnist_train.csv"), index=False
    )
    del stratified_mnist_train

    stratified_mnist_val.to_csv(
        os.path.join("data", "processed", "mnist_val.csv"), index=False
    )
    del stratified_mnist_val

    stratified_mnist_test.to_csv(
        os.path.join("data", "processed", "mnist_test.csv"), index=False
    )
    del stratified_mnist_test

    fashion_mnist_df = pd.read_csv(os.path.join("data", "raw", "fashion-mnist.csv"))
    stratified_fashion_mnist_train, stratified_fashion_mnist_test = train_test_split(
        fashion_mnist_df,
        test_size=0.2,
        stratify=fashion_mnist_df["label"],
    )
    del fashion_mnist_df

    stratified_fashion_mnist_train, stratified_fashion_mnist_val = train_test_split(
        stratified_fashion_mnist_train,
        train_size=0.875,
        stratify=stratified_fashion_mnist_train["label"],
    )

    print(stratified_fashion_mnist_train)
    print(stratified_fashion_mnist_val)
    print(stratified_fashion_mnist_test)

    stratified_fashion_mnist_train.to_csv(
        os.path.join("data", "processed", "fashion-mnist_train.csv"), index=False
    )
    del stratified_fashion_mnist_train

    stratified_fashion_mnist_val.to_csv(
        os.path.join("data", "processed", "fashion-mnist_val.csv"), index=False
    )
    del stratified_fashion_mnist_val

    stratified_fashion_mnist_test.to_csv(
        os.path.join("data", "processed", "fashion-mnist_test.csv"), index=False
    )
    del stratified_fashion_mnist_test
