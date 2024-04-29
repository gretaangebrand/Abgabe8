import json
from datetime import datetime

class Person():
    def __init__(self, first_name, last_name, birthdate=None, sex=None):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate  # Geburtsdatum als privates Attribut
        self.sex = sex
        if birthdate and sex:
            self.heart_rate = self.estimate_max_hr()
        else:
            self.heart_rate = None

    def save(self, filename):
        # Nur öffentliche Attribute speichern
        data = {"first_name": self.first_name, "last_name": self.last_name, "sex":self.sex, "heart_rate": self.heart_rate}
        with open(filename, 'w') as file:
            json.dump(data, file)

    def get_age(self):
        if self.__birthdate:
            birth_date = datetime.strptime(self.__birthdate, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        else:
            return None

    def estimate_max_hr(self):
        if self.__birthdate and self.sex:
            age = self.get_age()
            if self.sex == "male":
                max_hr_bpm = int(223 - 0.9 * age)
            elif self.sex == "female":
                max_hr_bpm = int(226 - 1.0 * age)
            else:
                max_hr_bpm = int(input("Enter maximum heart rate:"))
            return max_hr_bpm
        else:
            return None

class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, sex):
        super().__init__(first_name, last_name, birthdate, sex)

class Examiner(Person):
    def __init__(self, first_name, last_name, ID):
        super().__init__(first_name, last_name)
        self.ID = ID

    # Überschreibe die save-Methode, um nur öffentliche Attribute zu speichern
    def save(self, filename):
        data = {"first_name": self.first_name, "last_name": self.last_name, "ID": self.ID}
        with open(filename, 'w') as file:
            json.dump(data, file)

class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

# Beispiel einer Person
subject = Subject("Max", "Mustermann", "1990-01-01", "male")

examiner = Examiner("Maria", "Musterfrau", "123456")

# Speichere die Personen in JSON-Dateien
subject.save("subject.json")
examiner.save("examiner.json")
