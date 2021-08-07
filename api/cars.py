from flask import Blueprint, request

from exts import db
from lib.api import api_ok, api_not_found
from models.car import Car

cars = Blueprint('cars', __name__, url_prefix="/cars")


@cars.route('/', methods=['POST'])
def create_car():
    if request.is_json:
        data = request.get_json()
        new_car = Car(name=data['name'], model=data['model'], doors=data['doors'])
        db.session.add(new_car)
        db.session.commit()
        return {"message": f"car {new_car.name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}


@cars.route('/', methods=['GET'])
def list_cars():
    all_cars = Car.query.all()
    results = [
        {
            "api_identifier": car.api_identifier,
            "name": car.name,
            "model": car.model,
            "doors": car.doors
        } for car in all_cars]

    return api_ok({"count": len(results), "cars": results})


@cars.route('/<car_id>', methods=['GET'])
def get_car(car_id):
    car = Car.query.filter(Car.api_identifier == car_id).one_or_none()
    if car:
        return api_ok(car.to_dict())
    else:
        return api_not_found()
