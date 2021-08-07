from builtins import object

from exts import db
from lib.utils import random_string

MAX_API_ID_LENGTH = 255


class APIIdentified(object):
    API_ID_LENGTH = 12

    api_identifier = db.Column(db.String(MAX_API_ID_LENGTH), nullable=False)

    def __init__(self):
        self.api_identifier = self.generate_api_identifier()

    @classmethod
    def prefix_identifier(cls, identifier):
        if cls.API_ID_PREFIX:
            return u"{}_{}".format(cls.API_ID_PREFIX, identifier)
        return identifier

    @classmethod
    def generate_api_identifier(cls):
        return cls.prefix_identifier(random_string(cls.API_ID_LENGTH))
