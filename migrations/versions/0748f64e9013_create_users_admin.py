"""create users & admin

Revision ID: 0748f64e9013
Revises: 216d099ef82a
Create Date: 2023-01-13 01:05:10.205625

"""
from alembic import op
import sqlalchemy as sa
from app import db
from app.models import User

# revision identifiers, used by Alembic.
revision = '0748f64e9013'
down_revision = '216d099ef82a'
branch_labels = None
depends_on = None


def upgrade():
    u = User(username="user_2", email="name2@example.com", is_admin=False)
    u.set_password("pass")
    db.session.add(u)
    db.session.commit()

    u = User(username="admin_1", email="name3@example.com", is_admin=True)
    u.set_password("pass")
    db.session.add(u)
    db.session.commit()


def downgrade():
    u = User.query.filter_by(username="user_2").first()
    db.session.delete(u)
    db.session.commit()

    u = User.query.filter_by(username="admin_1").first()
    db.session.delete(u)
    db.session.commit()