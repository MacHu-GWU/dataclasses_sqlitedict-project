import dataclasses
from sqlitedict import SqliteDict
from dataclasses_sqlitedict import SingleTableDataModel


@dataclasses.dataclass
class User(SingleTableDataModel):
    username: str
    password: str


db = SqliteDict("user.sqlite", autocommit=False)

user = User(db=db, username="alice", password="pwd")
user.write()

user1 = User.read(db)
print(user1)
