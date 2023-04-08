import dataclasses
from sqlitedict import SqliteDict
from dataclasses_sqlitedict import SingleRowDataModel


@dataclasses.dataclass
class User(SingleRowDataModel):
    username: str
    password: str

    db = SqliteDict("user.sqlite", autocommit=False)

    @property
    def primary_key(self) -> str:
        return self.username


user = User(username="alice", password="pwd")
user.write()

user1 = User.read("alice")
print(user1)
