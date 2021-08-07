from flask import Response
import json


def api_ok(input_object={}, code=200):
    serialized = json.dumps(input_object, ensure_ascii=False)
    response = Response(serialized, content_type="application/json")

    return response, code


def api_not_found(code=404):
    response = Response("Not found", content_type="application/json")
    return response, code
