import json
import requests
from datetime import datetime

class Person():
    def __init__(self, first_name, last_name=None, birthdate=None, sex=None):
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

    def email(self):
        return f"{self.first_name.lower()}@example.com"

class Examiner(Person):
    def __init__(self, first_name, last_name, ID):
        super().__init__(first_name, last_name)
        self.ID = ID

    # Überschreibe die save-Methode, um nur öffentliche Attribute zu speichern
    def save(self, filename):
        data = {"first_name": self.first_name, "last_name": self.last_name, "ID": self.ID}
        with open(filename, 'w') as file:
            json.dump(data, file)

# GET-Anfrage an Webadresse senden
    response = requests.get(url= 'http://127.0.0.1:5000/')

    # POST-Anfrage an Webadresse senden und in json umformatieren
    def put(self, url):
        response = requests.put(url, json=self.__dict__)
        return response

    # Funktion zum Aktualisieren der E-Mail-Adresse
    def update_email(self):
        # Annahme: Ein Subject mit dem gleichen Vornamen wurde zuvor mit der Methode put() angelegt
        # Führe einen REST-POST-Befehl aus, um die E-Mail-Adresse auf dem Server zu aktualisieren
        # Verwende dazu die URL und die JSON-Daten entsprechend der API des Servers
        url = "http://127.0.0.1:5000/"
        data = {
            'first_name': self.first_name,
            'update_email': self.email
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("E-Mail-Adresse erfolgreich aktualisiert")
        else:
            print("Fehler beim Aktualisieren der E-Mail-Adresse")

# Beispiel zur Nutzung der update_email-Methode:
subject = Subject("Elisabeth", "lisi@example.com")
subject.update_email()

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