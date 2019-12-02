from flask import json, make_response
from flask_restful import Api, Resource

from .models import Word


api = Api()


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data, indent=2), code)
    resp.headers.extend(headers or {})
    return resp


class IndexResource(Resource):
    def get(self):
        return {"healthy": True}


class WordResource(Resource):
    def get(self):
        return Word.query.paginate().items


api.add_resource(IndexResource, '/')
api.add_resource(WordResource, '/words')
