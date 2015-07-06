"""
.. module:: client
    :synopsis: All routes on the ``client`` Blueprint.

.. moduleauthor:: Dan Schlosser <dan@dan@schlosser.io>
"""

from flask import Blueprint, render_template

client = Blueprint('client', __name__)


@client.route('/', methods=['GET'])
def index():
    """View the homepage.

    **Route:** ``/``

    **Methods:** ``GET``
    """
    return render_template('index.html')


@client.route('/typography', methods=['GET'])
def typography():
    """View the typographic styles.

    **Route:** ``/typography``

    **Methods:** ``GET``
    """
    return render_template('typography.html')
