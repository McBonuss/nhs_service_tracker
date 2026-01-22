import pytest


@pytest.mark.django_db
def test_patient_crud(client, user):
    assert client.login(username=user.username, password="ChangeMe123!")

    rv = client.post(
        "/patients/add/",
        data={
            "nhs_number": "9990001111",
            "first_name": "Alice",
            "last_name": "Brown",
            "date_of_birth": "1991-02-03",
            "contact_email": "alice@example.com",
            "status": "active",
            "priority": "medium",
        },
        follow_redirects=True,
    )
    assert b"Patient created" in rv.content

    rv = client.get("/patients/?q=Brown")
    assert b"Brown" in rv.content
