def test_register_and_login(client, app):
    rv = client.post('/auth/register', data={
        'full_name': 'Test User',
        'email': 'test@example.nhs.uk',
        'password': 'Secret123!'
    }, follow_redirects=True)
    assert b'Account created' in rv.data

    rv = client.post('/auth/login', data={
        'email': 'test@example.nhs.uk',
        'password': 'Secret123!'
    }, follow_redirects=True)
    assert b'Signed in successfully' in rv.data

def test_skip_link_present(client):
    rv = client.get('/', follow_redirects=True)
    assert b'Skip to content' in rv.data
