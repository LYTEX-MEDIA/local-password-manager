# add.py
class Add:
    def __init__(self, db):
        self.db = db
        self.category_names = self.db.config.keys()
        self.category = self.choose_category()
        self.collect_data_and_add()


    def choose_category(self):
        options = "\n".join(f"({i}) {category}" for i, category in enumerate(self.category_names, 1))
        choice = input(f'Choose a category:\n{options}\n')
        try:
            selected = list(self.category_names)[int(choice) - 1]
            return selected
        except (IndexError, ValueError):
            print('Invalid action!\n')
            return self.choose_category()


    def collect_data_and_add(self):
        data = {}
        for field in self.db.config[self.category]['fields']:
            if field != 'id':
                data[field] = input(f'{field.capitalize()}: ')
        self.db.add_entry(self.category, **data)
        print(f'{self.category.capitalize()} added! ' + " - ".join(f'[{field}]' for field in data))