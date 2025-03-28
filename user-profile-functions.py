def create_user_profile(*, name, email, **fields):
    # Erklärung: Durch "*," am Anfang der Parameterliste wird festgelegt, dass alle nachfolgenden
    # Argumente der Funktion Keyword-Argumente sind. "name" und "email" sind danach festgelegt,
    # alle anderen sind variabel. Wenn eines der beiden Argumente fehlt, wird ein Fehler erzeugt.
    
    profile = {}

    profile["name"] = name
    profile["email"] = email

    for key, value in fields.items():
        profile[key] = value

    return profile

alice = create_user_profile(name="Alice", age=33, city="New York", email = "alice@tn.techstarter.de")
print(alice)

bob = create_user_profile(name="Bob", last_name="Smith", age=22, phone_number=1234567890)
print(bob)