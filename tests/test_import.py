# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import dataclasses_sqlitedict

    _ = dataclasses_sqlitedict.dataclasses
    _ = dataclasses_sqlitedict.SingleRowDataModel
    _ = dataclasses_sqlitedict.SingleTableDataModel


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
