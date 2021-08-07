from exts import db
from models.mixins.api_identified import APIIdentified


class Car(APIIdentified, db.Model):
    __tablename__ = 'car'
    __pluralized__ = "cars"

    API_ID_PREFIX = "car"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    doors = db.Column(db.Integer(), nullable=False)

    def __init__(self, name, model, doors):
        APIIdentified.__init__(self)
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"

    def to_dict(self):
        return {
            "api_identifier": self.api_identifier,
            "name": self.name,
            "model": self.model,
            "doors": self.doors
        }

