# -*- coding: utf-8 -*-

"""
A sqlite backed dataclass. Each instance of class is a row in the table.
"""

import dataclasses
from sqlitedict import SqliteDict


@dataclasses.dataclass
class DataModel:
    """
    Base class for sqlite backed dataclass. Each instance of class is a row
    in the table. And all the instances of the same class share the same
    database table.

    Below is an usage example:

    .. code-block:: python

        @dataclasses.dataclass
        class User(DataModel):
            username: str
            password: str

            db = SqliteDict(str(path_db), autocommit=False)

            @property
            def primary_key(self) -> str:
                return self.username

        user = User(username="alice", password="pwd")
        user.write()

        user1 = User.read("alice")
    """

    @property
    def primary_key(self) -> str:
        raise NotImplementedError(
            "you must implement a primary_key property method in your class! "
            "it should return a string of the unique identifier "
            "for the instance of this class!"
        )

    def write(self):
        """
        Write data to database.
        """
        if self.db is None:
            raise NotImplementedError(
                "you must set a class attribute (NOT instance attribute) 'db', "
                "it is a sqlitedict.SqliteDict object that is used as the backend!"
            )
        data = dataclasses.asdict(self)
        self.db[self.primary_key] = data
        self.db.commit()

    @classmethod
    def read(cls, primary_key: str) -> "DataModel":
        """
        Create a new instance of class from database.
        """
        if cls.db is None:
            raise NotImplementedError(
                "you must set a class attribute (NOT instance attribute) 'db', "
                "it is a sqlitedict.SqliteDict object that is used as the backend!"
            )
        return cls(**cls.db[primary_key])


DataModel.db: SqliteDict
DataModel.db = None
