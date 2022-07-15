import json
from bson import ObjectId

# Кастомный енкодер для работы с монго
# Нужно сериализовать только ObjectId


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
