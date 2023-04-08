# -*- coding: utf-8 -*-

import os
import pytest
import dataclasses
from pathlib import Path
from sqlitedict import SqliteDict
from dataclasses_sqlitedict.single_row import DataModel

dir_here = Path(__file__).absolute().parent
path_db = dir_here / "test_single_row.sqlite"


@dataclasses.dataclass
class User(DataModel):
    username: str
    password: str

    db = SqliteDict(str(path_db), autocommit=False)

    @property
    def primary_key(self) -> str:
        return self.username


@dataclasses.dataclass
class Person(DataModel):
    """
    Test if the second subclass will conflict with the first subclass.
    """

    name: str
    age: int

    db = SqliteDict(str(path_db), autocommit=False)

    @property
    def primary_key(self) -> str:
        return self.name


@dataclasses.dataclass
class Student(Person):
    """
    Test if allow inheritance.
    """

    student_id: str


@dataclasses.dataclass
class Pet(DataModel):
    """
    Test edge case when user forget to implement db.
    """

    name: str
    type: str

    @property
    def primary_key(self) -> str:
        return self.name


class TestDataModel:
    def test(self):
        # ----------------------------------------------------------------------
        user = User(username="alice", password="pwd")
        user.write()

        person = Person(name="bob", age=20)
        person.write()

        student = Student(name="charlie", age=15, student_id="sid-chalice")
        student.write()

        user1 = User.read("alice")
        assert user1.username == user.username
        assert user1.password == user.password

        person1 = Person.read("bob")
        assert person1.name == person.name
        assert person1.age == person.age

        student1 = Student.read("charlie")
        assert student1.name == student.name
        assert student1.age == student.age
        assert student1.student_id == student.student_id
        # ----------------------------------------------------------------------
        person.age = 30
        person.write()

        person1 = Person.read("bob")
        assert person1.age == 30

    def test_edge_case(self):
        pet = Pet(name="fire", type="dog")
        with pytest.raises(NotImplementedError):
            pet.write()


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
