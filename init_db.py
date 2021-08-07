from app import app
from exts import db
from models.car import Car


def init_db():
    names = ["Ford", "Nissan", "Honda", "Ferrari", "McLaren", "Mercedes"]
    models = ["Sedan", "Truck", "Motorcycle"]
    doors = [2, 4]
    cars = []
    for name in names:
        for model in models:
            for door in doors:
                cars.append(Car(name, model, door))
    db.session.add_all(cars)
    db.session.commit()


with app.app_context():
    init_db()