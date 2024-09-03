#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

# class Person:
#     def __init__(self, name='person', job='job'):
#         self.name = name
#         self.job = job
#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         if 0 < len(str(name)) < 25 and name != "":
#         # and name.replace(' ','').isalpha():
#             self._name = name.title()
#         else:
#             print("Name must be string between 1 and 25 characters.")
#     def get_job(self):
#         return self._job
#     def set_job(self, job):
#         if str(job) in APPROVED_JOBS:
#             self._job = job.title()
#         else:
#             add = ''.join(APPROVED_JOBS)
#             print(f"Job must be one of the following: {add}")
#     name = property(get_name,set_name)
#     age = property(get_job,set_job)


class Person:
    approved_jobs = APPROVED_JOBS
    def __init__(self, name="name", job="Sales"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()

        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = 'name'

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = 'Sales'

