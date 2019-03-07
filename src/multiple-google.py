from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task
import random


class SimpleGoogleTasks(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/")

    @task(3)
    def search(self):
        query = "Giacomo+Marciani"
        self.client.get("/search?q=%s" % query)


class SimpleGoogleSequentialTasks(TaskSequence):

    @seq_task(1)
    def first_task(self):
        self.client.get("/")

    @seq_task(2)
    def second_task(self):
        query = "Giacomo+Marciani"
        self.client.get("/search?q=%s" % query)

    @seq_task(3)
    @task(10)
    def third_task(self):
        self.client.get("/")


class GoogleLocustUniform(HttpLocust):
    weight = 1
    host = "https://google.com"
    task_set = SimpleGoogleTasks
    wait_function = lambda self: random.uniform(5000, 9000)


class GoogleLocustExponential(HttpLocust):
    weight = 3
    host = "https://google.com"
    task_set = SimpleGoogleSequentialTasks
    wait_function = lambda self: random.expovariate(3000)