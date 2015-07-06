"""
.. module:: EditUserForm
    :synopsis: A form for editing a :class:`~app.models.User`.

.. moduleauthor:: Dan Schlosser <dan@dan@schlosser.io>
"""

from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required, Email

EMAIL_ERROR = 'Please provide a valid email address.'


class EditUserForm(Form):
    """A form for editing a :class:`~app.models.User`.

    :ivar name: :class:`wtforms.fields.StringField` - The user's name
    :ivar email: :class:`wtforms.fields.StringField` - The user's email address
    """
    name = StringField('Full Name', [Required("Please type a name")])
    email = StringField('Email Address',
                        [Email(message=EMAIL_ERROR),
                         Required(message=EMAIL_ERROR)])
