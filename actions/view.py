class View:
    def __init__(self, db):
        self.db = db
        self.category = self.choose_category()
        self.view_entry()


    def choose_category(self):
        options = "\n".join(f"({i}) {category}" for i, category in enumerate(self.db.config.keys(), 1))
        choice = input(f'Choose a category:\n{options}\n')
        try:
            selected = list(self.db.config.keys())[int(choice) - 1]
            return selected
        except (IndexError, ValueError):
            print('Invalid action!\n')
            return self.choose_category()


    def view_entry(self):
        identifier = input('Name of the entry: ')
        self.db.view_entry(self.category, identifier)