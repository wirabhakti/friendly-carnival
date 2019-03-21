#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Calculate Interquartile Range (IQR) of one dimensional array"""

import statistics, math, argparse, re

parser = argparse.ArgumentParser(prog='Return IQR of one dimensional array', description='this program will return IQR of one dimensional array', usage='The IQR is used to measure how spread out the data points in a set are from the mean of the data set. The higher the IQR, the more spread out the data points; in contrast, the smaller the IQR, the more bunched up the data points are around the mean')

def returnToList(arr):
    regex = re.compile(r'\d+')
    new_list = []
    for i in regex.findall(arr):
        new_list.append(int(i))
    return new_list

parser.add_argument('list_array', help='dont forget give double/single quote', type=returnToList)

def iQR(arr):
    if len(arr) % 2 == 0:
        slice_median = int(len(arr)/2)
        print(slice_median)
        arr1 = arr[:slice_median]
        print(arr1)
        arr2 = arr[slice_median:]
        print(arr2)
        Q1 = statistics.median(arr1)
        Q3 = statistics.median(arr2)
        result =  Q3 - Q1
        print(result)
    else:
        arr1 = arr[:math.floor(len(arr)/2)]
        arr2 = arr[math.ceil(len(arr)/2):]
        Q1 = statistics.median(arr1)
        Q3 = statistics.median(arr2)
        result = Q3 - Q1
        print(result)

if __name__ == '__main__':
    args = parser.parse_args()
    iQR(args.list_array)
