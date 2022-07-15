from bson.objectid import ObjectId


class JobsModel:
    def __init__(self, client, userid):
        self.userid = userid
        self.dao = client.db.jobs

    def insert(self,
               title: str,
               marked: bool
               ):
        job_to_insert = {
            "userid": self.userid,
            "title": title,
            "marked": marked
        }

        return self.dao.insert_one(job_to_insert)

    def read_one(self, _id):
        cursor = self.dao.find_one({"_id": ObjectId(_id)})
        if cursor:
            return cursor
        else:
            return {"Error": "Not found"}

    def update(self,
               jobid,
               title: str,
               marked: bool):
        job = self.dao.find_one({"_id": ObjectId(jobid)})
        job["title"] = title
        job["marked"] = marked
        return self.dao.update({'_id': ObjectId(jobid)}, {"$set": job}, upsert=False)

    def delete(self, jobid):
        self.dao.remove({"_id": ObjectId(jobid)})
