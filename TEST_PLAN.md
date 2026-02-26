## Test Plan

This document captures automated and manual testing for the NHS Service Tracker.

## Automated Tests

- Run all tests: `pytest`
- CRUD tests: `pytest tests/test_crud.py`
- Authentication tests: `pytest tests/test_auth_routes.py`
- Model tests: `pytest tests/test_models.py`

## Manual Testing

Outcomes are marked "Not run" until verified in the local or deployed environment.

| ID | Area | Steps | Expected Result | Outcome |
| --- | --- | --- | --- | --- |
| M1 | Sign in | Open `/login/`, enter valid credentials, submit | User lands on dashboard and sees welcome message | Not run |
| M2 | Register | Open `/register/`, enter details, submit | Account created and user is signed in | Not run |
| M3 | Patient create | Go to Patients > Add Patient, complete form, save | New patient appears in list with success message | Not run |
| M4 | Patient edit | Open a patient, click Edit, update fields, save | Changes persist and detail view updates | Not run |
| M5 | Patient delete | Open a patient, click Delete | Record removed and list updates | Not run |
| M6 | Service create | Go to Services > Add Service, save | Service appears in list | Not run |
| M7 | Service edit | Edit a service, save | Updates appear in list | Not run |
| M8 | Service delete | Delete a service from list | Service removed from list | Not run |
| M9 | Appointment create | Go to Appointments > Schedule Appointment, save | Appointment appears in list | Not run |
| M10 | Appointment edit | Edit an appointment, save | Updates appear in list | Not run |
| M11 | Appointment delete | Delete an appointment from list | Appointment removed | Not run |
| M12 | Search | Search patients by last name | Filtered list shows matching results | Not run |
| M13 | Accessibility | Use Tab to navigate links and controls | Focus ring visible and logical order | Not run |
| M14 | Responsive layout | Resize browser to mobile width | Navigation, tables, and cards remain usable | Not run |

## Bugs Found & Fixes

| ID | Issue | Cause | Fix | Status |
| --- | --- | --- | --- | --- |
| B1 | Users redirected to login after form submissions | Unstable `SECRET_KEY` caused session invalidation between requests/workers | Require a stable `SECRET_KEY` and add dev/test fallback keys | Fixed |
