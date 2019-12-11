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


class WordDetailResource(Resource):
    def get(self, word):
        return Word.query.get_or_404(word.upper())


class WordRecommendationsResource(Resource):
    def get(self, word):
        return Word(word.upper()).recommendations()


api.add_resource(IndexResource, '/')
api.add_resource(WordResource, '/words')
api.add_resource(WordDetailResource, '/words/<word>')
api.add_resource(WordRecommendationsResource, '/words/<word>/recommendations')
