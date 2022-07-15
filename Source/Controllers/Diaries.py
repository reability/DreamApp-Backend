from flask import request

from Source.Utility.Encoder import CustomJSONEncoder


class DiariesController:
    def __init__(self, diary):
        self.diary = diary

    def make_an_entry(self):
        content = request.get_json()

        entry_value = content["value"]
        entry_type = content["type"]
        entry_timestamp = content["timestamp"]

        return self.diary.insert(value=entry_value, type=entry_type, timestamp=entry_timestamp)

    def read_entries(self):
        return self.diary.read_all()
