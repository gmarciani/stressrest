from locust import HttpLocust, TaskSet, task
import random


class SimpleGoogleTasks(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/")


class GoogleLocustUniform(HttpLocust):
    weight = 1
    host = "https://google.com"
    task_set = SimpleGoogleTasks
    wait_function = lambda self: random.uniform(5000, 9000)