from flask import request

from Source.Utility.Encoder import CustomJSONEncoder


class DreamsController:
    def __init__(self, dreams, jobs):
        self.dreams = dreams
        self.jobs = jobs

    def get_one(self):
        data = self.dreams.read_user_one()
        jobsid_array = data["jobs"]

        temp = []

        for job_id in jobsid_array:
            job = self.jobs.read_one(job_id)
            job["user_id"] = None
            temp.append(job)

        data["jobs"] = temp

        return CustomJSONEncoder().encode(self.dreams.read_user_one())

    def store(self):
        content = request.get_json()

        dream_title = content["title"]
        dream_description = content["description"]

        jobs_to_store = []

        dream_jobs = content["jobs"]
        for dream_job in dream_jobs:
            job_title = dream_job["title"]
            job_marked = dream_job["marked"]

            new_job = self.jobs.insert(job_title, job_marked)
            if new_job:
                new_job_id = new_job["_id"]
                jobs_to_store.append(new_job_id)
            else:
                return {"Error": "Failed to create a dream"}
        return self.dreams.insert(dream_title, dream_description, jobs_to_store)

    def add_job(self, dreamid):
        content = request.get_json()

        job_title = content["title"]
        job_marked = content["marked"]

        job = self.jobs.insert(title=job_title, marked=job_marked)
        job_id = job["_id"]

        return self.dreams.insert_new_job(dreamId=dreamId, job_id=job_id)

    def update_job(self, dreamid, jobid):
        content = request.get_json()

        new_job_title = content["title"]
        new_job_marked = content["marked"]

        self.jobs.update(jobid, new_job_title, new_job_marked)

    def delete_job(self, dreamid, jobid):
        self.jobs.delete(jobid)
        return self.dreams.delete_job(dreamid, jobid)







