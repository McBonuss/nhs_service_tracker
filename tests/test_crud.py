from datetime import date

def login(client, email='admin@example.nhs.uk', password='ChangeMe123!'):
    client.post('/auth/register', data={
        'full_name':'Admin User','email':email,'password':password
    }, follow_redirects=True)
    client.post('/auth/login', data={'email':email, 'password':password}, follow_redirects=True)

def test_patient_crud(client):
    login(client)
    rv = client.post('/patients/create', data={
        'nhs_number':'9990001111',
        'first_name':'Alice',
        'last_name':'Brown',
        'date_of_birth':date(1991,2,3),
        'contact_email':'alice@example.com'
    }, follow_redirects=True)
    assert b'Patient created' in rv.data

    rv = client.get('/patients/?q=Brown')
    assert b'Brown' in rv.data
