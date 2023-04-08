# -*- coding: utf-8 -*-

"""
A sqlite backed dataclass. Each instance of class is a table.
"""

import dataclasses
from sqlitedict import SqliteDict


@dataclasses.dataclass
class DataModel:
    db: SqliteDict = dataclasses.field()

    @classmethod
    def read(cls, db: SqliteDict) -> "DataModel":
        kwargs = {
            field.name: db[field.name]
            for field in dataclasses.fields(cls)
            if field.name != "db"
        }
        kwargs["db"] = db
        return cls(**kwargs)

    def write(self):
        for field in dataclasses.fields(self.__class__):
            if field.name != "db":
                self.db[field.name] = getattr(self, field.name)
        self.db.commit()
