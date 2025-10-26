import click
from flask.cli import with_appcontext
from app import create_app
from app.extensions import db
from app.models import Role, User
from werkzeug.security import generate_password_hash

app = create_app()

@app.cli.command("seed")
@with_appcontext
def seed():
    """Seed initial roles and an admin user."""
    admin = Role.query.filter_by(name='admin').first() or Role(name='admin')
    clinician = Role.query.filter_by(name='clinician').first() or Role(name='clinician')
    db.session.add_all([admin, clinician])
    db.session.commit()

    if not User.query.filter_by(email='admin@example.nhs.uk').first():
        u = User(email='admin@example.nhs.uk', full_name='Admin User', password_hash=generate_password_hash('ChangeMe123!'))
        u.roles.append(admin)
        db.session.add(u)
        db.session.commit()
        click.echo('Created admin user: admin@example.nhs.uk / ChangeMe123!')
    else:
        click.echo('Admin user already exists.')
