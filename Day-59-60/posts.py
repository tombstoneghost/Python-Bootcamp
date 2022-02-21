# Imports
import requests
import json

class Post:
    def __init__(self):
        self.api = "https://api.npoint.io/f58b8ccbc8ee08816ab1"
        self.blogs = []
        self.load_blogs()

    def load_blogs(self):
        response = requests.get(url=self.api)
        self.blogs = response.json()

    def get_all_blogs(self):
        return self.blogs

    def get_blog(self, id):
        for blog in self.blogs:
            if blog["id"] == int(id):
                return blog
