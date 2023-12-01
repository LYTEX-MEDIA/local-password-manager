class Delete:
    def __init__(self, db):
        self.db = db
        self.category_names = self.db.config.keys()
        self.category = self.choose_category()
        self.collect_data_and_delete()


    def choose_category(self):
        options = "\n".join(f"({i}) {category}" for i, category in enumerate(self.category_names, 1))
        choice = input(f'Choose a category:\n{options}\n')
        try:
            selected = list(self.category_names)[int(choice) - 1]
            return selected
        except (IndexError, ValueError):
            print('Invalid action!\n')
            return self.choose_category()


    def collect_data_and_delete(self):
        identifier = input('Name of the entry to be deleted: ')
        self.db.delete_entry(self.category, identifier)
        print(f'{self.category.capitalize()} entry "{identifier}" deleted!\n')