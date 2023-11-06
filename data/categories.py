import json
from pathlib import Path

class Categories:
    def __init__(self, filename='categories.json'):
        self.filename = filename
        self.filepath = Path(self.filename)
        self.categories = self.load_categories()


    def load_categories(self):
        if not self.filepath.is_file():
            return {}
        with open(self.filename, 'r') as file:
            return json.load(file)


    def save_categories(self):
        with open(self.filename, 'w') as file:
            json.dump(self.categories, file, indent=4)


    def add_category(self, category_name, fields):
        if category_name in self.categories:
            print(f"Category '{category_name}' already exists.")
            return False
        self.categories[category_name] = {"fields": fields}
        self.save_categories()
        return True


    def remove_category(self, category_name):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
            return False
        del self.categories[category_name]
        self.save_categories()
        return True


    def get_all_categories(self):
        return self.categories


    def update_category(self, category_name, fields):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
            return False
        self.categories[category_name] = {"fields": fields}
        self.save_categories()
        return True