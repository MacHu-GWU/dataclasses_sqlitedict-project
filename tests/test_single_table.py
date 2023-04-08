# -*- coding: utf-8 -*-

import os
import pytest
import dataclasses
from pathlib import Path
from sqlitedict import SqliteDict
from dataclasses_sqlitedict.single_table import DataModel

dir_here = Path(__file__).absolute().parent
path_db = dir_here / "test_single_table.sqlite"


@dataclasses.dataclass
class User(DataModel):
    username: str
    password: str


class TestDataModel:
    def test(self):
        db = SqliteDict(str(path_db), autocommit=False)

        user = User(db=db, username="alice", password="pwd")
        user.write()

        user1 = User.read(db)
        assert user1.username == user.username
        assert user1.password == user.password

        db = SqliteDict(str(path_db), tablename="user-bob", autocommit=False)
        user = User(db=db, username="bob", password="pwd")
        user.write()

        user1 = User.read(db)
        assert user1.username == user.username
        assert user1.password == user.password


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
