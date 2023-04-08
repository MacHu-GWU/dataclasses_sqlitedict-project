# -*- coding: utf-8 -*-

"""
A sqlite backed dataclass. Each instance of class is a table.
"""

import dataclasses
from sqlitedict import SqliteDict


@dataclasses.dataclass
class DataModel:
    """
    Base class for sqlite backed dataclass. Each instance of class is a table.
    Each instance of class could be different tables in the same databases,
    or different table in different databases.

    Below is an usage example:

    .. code-block:: python

        @dataclasses.dataclass
        class User(DataModel):
            username: str
            password: str

        db = SqliteDict("user.sqlite", autocommit=False)

        user = User(db=db, username="alice", password="pwd")
        user.write()

        user1 = User.read(db)
    """

    db: SqliteDict = dataclasses.field()

    def write(self):
        """
        Write data to database.
        """
        for field in dataclasses.fields(self.__class__):
            if field.name != "db":
                self.db[field.name] = getattr(self, field.name)
        self.db.commit()

    @classmethod
    def read(cls, db: SqliteDict) -> "DataModel":
        """
        Create a new instance of class from database.
        """
        kwargs = {
            field.name: db[field.name]
            for field in dataclasses.fields(cls)
            if field.name != "db"
        }
        kwargs["db"] = db
        return cls(**kwargs)


