"""
.. module:: User
    :synopsis: A user database model.

.. moduleauthor:: Dan Schlosser <dan@dan@schlosser.io>
"""

from app import db
from datetime import datetime


class User(db.Document):
    """An example user model.

    :ivar date_created: :class:`mongoengine.fields.DateTimeField` - The date
        that this user was created.
    :ivar date_modified: :class:`mongoengine.fields.DateTimeField` - The date
        the this user was last modified.
    :ivar name: :class:`mongoengine.fields.StringField` - The user's name.
    :ivar email: :class:`mongoengine.fields.EmailField` - The user's email
        address.
    """

    date_created = db.DateTimeField(required=True, default=datetime.now())
    date_modified = db.DateTimeField(required=True, default=datetime.now())
    name = db.StringField(required=True, max_length=510)
    email = db.EmailField(required=True, unique=True)

    # MongoEngine ORM metadata
    meta = {
        'allow_inheritance': True,
        'indexes': ['email', ]
    }

    def clean(self):
        """Called by Mongoengine on every ``.save()`` to the object.

        Update date_modified.

        :raises: :class:`wtforms.validators.ValidationError`
        """
        self.date_modified = datetime.now()

    def __repr__(self):
        """The representation of this user.

        :returns: The user's details.
        :rtype: str
        """
        return '<User name={}, email={}>'.format(self.name, self.email)
