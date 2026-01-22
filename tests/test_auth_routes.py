import pytest


@pytest.mark.django_db
def test_register_and_login(client):
    rv = client.post(
        "/register/",
        data={
            "full_name": "Test User",
            "email": "test@example.nhs.uk",
            "password1": "Secret123!",
            "password2": "Secret123!",
        },
        follow=True,
    )
    assert b"Account created." in rv.content

    rv = client.post(
        "/login/",
        data={
            "username": "test@example.nhs.uk",
            "password": "Secret123!",
        },
        follow=True,
    )
    assert b"NHS Service Tracker Dashboard" in rv.content


def test_skip_link_present(client):
    rv = client.get("/login/")
    assert b"Skip to content" in rv.content
