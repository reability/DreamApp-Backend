from bson.objectid import ObjectId


class DreamsModel:
    def __init__(self, client, userid):
        self.userid = userid
        self.dao = client.db.dreams

    def insert(self,
               title: str,
               description: str,
               jobs: [int]):
        dream_to_insert = {
            "userid": self.userid,
            "title": title,
            "description": description,
            "jobs": jobs
        }

        return self.dao.insert_one(dream_to_insert)

    def read_one(self, _id):
        cursor = self.dao.find_one({"_id": ObjectId(_id)})
        if cursor:
            return cursor
        else:
            return {"Error": "Not found"}

    def read_user_one(self):
        cursor = self.dao.find_one({"userid": self.userid})
        if cursor:
            return cursor
        else:
            return {"Error": "Not found"}

    def insert_new_job(self,
                       dreamid,
                       jobid):
        dream = self.dao.find_one({"_id": ObjectId(dreamid)})
        dream["jobs"].append(jobid)
        return self.dao.update({'_id': ObjectId(dreamid)}, {"$set": dream}, upsert=False)

    def delete_job(self,
                   dreamid,
                   jobid):
        dream = self.dao.find_one({"_id": ObjectId(dreamid)})
        jobs = dream["jobs"]
        jobs.remove(jobid)
        return self.dao.update({'_id': ObjectId(dreamid)}, {"$set": dream}, upsert=False)
