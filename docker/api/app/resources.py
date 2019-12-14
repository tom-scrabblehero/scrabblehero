from flask import json, make_response
from flask_restful import Api, Resource

from .models import Word


api = Api()


@api.representation('application/json')
def output_json(data, code, headers=None):
    result = {
        'data': data,
        'status_code': code
    }
    resp = make_response(json.dumps(result, indent=2), code)
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


class TwoLetterWordsResource(Resource):
    def get(self):
        return Word.query.filter(Word.length==2).all()


class WordsStartingWithResource(Resource):
    def get(self, letters):
        letters = letters.upper()
        return Word.query.filter(Word.id.like(f"{letters}%")).paginate().items


class WordsEndingWithResource(Resource):
    def get(self, letters):
        letters = letters.upper()
        return Word.query.filter(Word.id.like(f"%{letters}")).paginate().items


class WordsContainingResource(Resource):
    def get(self, letters):
        letters = letters.upper()
        return Word.query.filter(Word.id.like(f"%{letters}%")).paginate().items


class VowelWordsResource(Resource):
    def get(self):
        return Word.query.filter(Word.vowels_length > 4).filter(Word.consonants_length < 4).paginate().items


class ConsonantWordsResource(Resource):
    def get(self):
        return Word.query.filter(Word.vowels_length < 4).filter(Word.consonants_length > 4).paginate().items


api.add_resource(IndexResource, '/')
api.add_resource(WordResource, '/words')
api.add_resource(WordDetailResource, '/words/<word>')
api.add_resource(WordRecommendationsResource, '/words/<word>/recommendations')
api.add_resource(TwoLetterWordsResource, '/two-letter-words')
api.add_resource(WordsStartingWithResource, '/words/starting-with/<letters>')
api.add_resource(WordsEndingWithResource, '/words/ending-with/<letters>')
api.add_resource(WordsContainingResource, '/words/containing/<letters>')
api.add_resource(VowelWordsResource, '/vowel-words')
api.add_resource(ConsonantWordsResource, '/consonant-words')
