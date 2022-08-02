import json
import os

class File:
    name = None
    path = None

    def __init__(self, name:str, path:str = None):
        self.name = name
        self.path = path

    @staticmethod
    def read_json(full_path:str) -> dict:
        response = None
        with open(full_path, 'r') as f:
            response = json.load(f)
        return response

