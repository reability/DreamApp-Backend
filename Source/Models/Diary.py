from bson.objectid import ObjectId


class DiaryModel:
    def __init__(self, client, userid):
        self.userid = userid
        self.dao = client.diaries

    def insert(self, value: int, type: int, timestamp: int):
        entry_to_insert = {"value": value, "type": type, timestamp: timestamp}

        return self.dao.insert_one(entry_to_insert)

    def read_all(self):
        cursor = self.dao.find({ "_id": ObjectId(self.userid) })
        if cursor:
            temp = []
            for _entry in cursor:
                temp.append(_entry)
            return {"entries": temp}
        else:
            return {"Error": "No cursor founded"}

