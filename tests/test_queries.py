import pytest
from base.main import setup_db

QUERIES = [
    """
        SELECT COUNT(*)
        FROM Orders
        LEFT JOIN Contacts
            ON Contacts.Id=Orders.ContactId
        -- WHERE Contacts.CreatedOn >= datetime("now",'-1 day')
        WHERE Orders.CreatedOn >= datetime("2019-10-09 10:13:00",'-1 day')
            AND Contacts.FirstName == "Ivan"
    """,
    """
        SELECT COUNT(*)
        FROM Contacts
        LEFT JOIN Cities
            ON Cities.id=Contacts.CityId
        WHERE Cities.CountryId == "Ukraine"

    """,
    """
        SELECT DISTINCT Contacts.FirstName
        FROM Contacts
        ORDER BY Contacts.FirstName
    """
]

ANSWERS = [
    [2],
    [2],
    ['Anna', 'Ivan', 'Lina', 'Petro']
]


@pytest.fixture(scope="module")
def db():
    return setup_db()

@pytest.mark.parametrize("query, answer", zip(QUERIES, ANSWERS))
def test_queries(db, query, answer):
    result = [r[0] for r in db.execute(query).fetchall()]
    assert result == answer
