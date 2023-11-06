class Update:
    def __init__(self, db):
        self.db = db
        self.category = self.choose_category()
        self.collect_data_and_update()


    def choose_category(self):
        options = "\n".join(f"({i}) {category}" for i, category in enumerate(self.db.config.keys(), 1))
        choice = input(f'Was willst du aktualisieren?\n{options}\nWähle eine Nummer: ')
        try:
            selected = list(self.db.config.keys())[int(choice) - 1]
            return selected
        except (IndexError, ValueError):
            print('Ungültige Eingabe!\n')
            return self.choose_category()


    def collect_data_and_update(self):
        identifier = input('Name des zu aktualisierenden Eintrags: ')
        data = {}
        for field in self.db.config[self.category]['fields']:
            if field != 'id':  # id is auto-incremented
                new_value = input(f'Neuer Wert für {field.capitalize()}: ')
                data[field] = new_value
        self.db.update_entry(self.category, identifier, **data)
        print(f'{self.category.capitalize()} aktualisiert!')