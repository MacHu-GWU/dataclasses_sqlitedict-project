
.. .. image:: https://readthedocs.org/projects/dataclasses_sqlitedict/badge/?version=latest
    :target: https://dataclasses_sqlitedict.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/dataclasses_sqlitedict-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/dataclasses_sqlitedict-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/dataclasses_sqlitedict-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/dataclasses_sqlitedict-project

.. image:: https://img.shields.io/pypi/v/dataclasses_sqlitedict.svg
    :target: https://pypi.python.org/pypi/dataclasses_sqlitedict

.. image:: https://img.shields.io/pypi/l/dataclasses_sqlitedict.svg
    :target: https://pypi.python.org/pypi/dataclasses_sqlitedict

.. image:: https://img.shields.io/pypi/pyversions/dataclasses_sqlitedict.svg
    :target: https://pypi.python.org/pypi/dataclasses_sqlitedict

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/dataclasses_sqlitedict-project

------


.. .. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://dataclasses_sqlitedict.readthedocs.io/index.html

.. .. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://dataclasses_sqlitedict.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://dataclasses_sqlitedict.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/dataclasses_sqlitedict-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/dataclasses_sqlitedict-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/dataclasses_sqlitedict-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/dataclasses_sqlitedict#files


Welcome to ``dataclasses_sqlitedict`` Documentation
==============================================================================
Sqlite backed dataclasses. It is a light weight persistent storage for dataclasses.
If you are looking for a full featured ORM, please check out SQLAlchemy.


Features
------------------------------------------------------------------------------


Single Row Data Model
------------------------------------------------------------------------------
Each instance of class is a row in the table. And all the instances of the same class share the same database table.

.. code-block:: python

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


Single Table Data Model
------------------------------------------------------------------------------
Each instance of class is a table. Each instance of class could be different tables in the same databases, or different table in different databases.

.. code-block:: python

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


.. _install:

Install
------------------------------------------------------------------------------

``dataclasses_sqlitedict`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install dataclasses_sqlitedict

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade dataclasses_sqlitedict