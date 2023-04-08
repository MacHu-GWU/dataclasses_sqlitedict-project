# -*- coding: utf-8 -*-

"""
Sqlite backed dataclasses. It is a light weight persistent storage for dataclasses.
If you are looking for a full featured ORM, please check out SQLAlchemy.
"""


from ._version import __version__

__short_description__ = "Sqlite backed dataclasses. It is a light weight persistent storage for dataclasses."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from .api import (
        dataclasses,
        SingleRowDataModel,
        SingleTableDataModel,
    )
except ImportError as e:  # pragma: no cover
    print(e)
