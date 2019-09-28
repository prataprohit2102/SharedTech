from enum import Enum
from typing import List

import attr
import requests
from marshmallow import Schema, fields, post_load

BASE_URL = "http://autothon-nagarro-backend-b08.azurewebsites.net"


class Category(Enum):
    Comedy = 'Comedy'
    Thriller = 'Thriller'
    Drama = 'Drama'


class ReviewSchema(Schema):
    id = fields.Int()
    from_ = fields.Str()
    posted = fields.Str()
    rating = fields.Int()
    text = fields.Str()

    @post_load
    def create_object(self, json_data):
        return Review(**json_data)


class EnumProperty(Enum):
    VALUE = 'value'
    NAME = 'name'


class EnumField(fields.Field):

    def __init__(self, enum, load_by_value=True, *args, **kwargs):
        self.enum = enum
        self.dump_by = EnumProperty.VALUE if load_by_value else EnumProperty.NAME
        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj):
        return None if value is None else getattr(value, self.dump_by.value)

    def _deserialize(self, value, attr, data):
        deserialized_value = None
        if value is None:
            deserialized_value = None
        if self.dump_by == EnumProperty.VALUE:
            deserialized_value = self.enum(value)
        if self.dump_by == EnumProperty.NAME:
            deserialized_value = self.enum[value]
        return deserialized_value


@attr.s
class Review:
    id = attr.ib(type=int)
    from_ = attr.ib(type=str)
    posted = attr.ib(type=str)
    rating = attr.ib(type=int)
    text = attr.ib(type=str)


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    image = fields.Str()
    director = fields.Str()
    rating = fields.Int()
    rented = fields.Str()
    reviews = fields.Nested('ReviewSchema', many=True)
    categories = fields.List(EnumField(Category))
    until = fields.Int()
    que = fields.Int()

    @post_load
    def create_object(self, json_data):
        return Movie(**json_data)


@attr.s
class Movie:
    id = attr.ib(type=int)
    title = attr.ib(type=str)
    description = attr.ib(type=str)
    image = attr.ib(type=str)
    director = attr.ib(type=str)
    rating = attr.ib(type=int)
    rented = attr.ib(type=bool)
    reviews = attr.ib(type=List[Review])
    categories = attr.ib(type=List[Category])
    until = attr.ib(type=int)
    que = attr.ib(type=int)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    city = fields.Str()
    street = fields.Str()
    number = fields.Int()
    myMovies = fields.List(fields.Integer())

    @post_load
    def create_object(self, json_data):
        return User(**json_data)


@attr.s
class User:
    id = attr.ib(type=int)
    username = attr.ib(type=str)
    email = attr.ib(type=str)
    city = attr.ib(type=str)
    street = attr.ib(type=str)
    number = attr.ib(type=int)
    myMovies = attr.ib(type=List[int])
    password = attr.ib(type=str, default=None)

    @staticmethod
    def login(username, password):
        login_url = BASE_URL + '/login'
        request_body = {"username": username, "password": password}
        response = requests.post(url=login_url, json=request_body)
        assert response.status_code == 200
        user = UserSchema().load(response.json())
        return user


if __name__ == '__main__':
    user_json = {
        "username": "user",
        "password": "password",
        "email": "seven@nine.ten",
        "city": "Holywood",
        "street": "Famous Street Name",
        "number": "21",
        "id": "10294509580624989",
        "myMovies": [
            2,
            0
        ]
    }
    UserSchema().load(user_json)
