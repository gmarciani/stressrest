from locust import HttpLocust, TaskSet, task
import random


class SimpleTasks(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/")


class GoogleLocustUniform(HttpLocust):
    task_set = SimpleTasks
    wait_function = lambda self: random.uniform(5000, 9000)