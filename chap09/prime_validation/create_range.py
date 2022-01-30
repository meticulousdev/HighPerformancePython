import unittest


def create(range_from, range_to, chunks):
    partial_range_length = (range_to - range_from) / float(chunks)