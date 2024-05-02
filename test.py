from my_classes import Person, Subject

# Beispiel: Erstellen eines Subjects und Aktualisieren der E-Mail-Adresse
def test_subject_workflow():
    # Erstelle eine neue Person mit den erforderlichen Daten
    new_subject = Subject("Max", "Mustermann", "1990-01-01", "male", "max@example.com")

    # Aktualisiere die E-Mail-Adresse des Subjects
    new_subject.update_email()

if __name__ == "__main__":
    # Führe den Test durch
    test_subject_workflow()
