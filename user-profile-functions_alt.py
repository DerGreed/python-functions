def create_user_profile(**fields):

    if not ("name" in fields.keys() and "email" in fields.keys()):
        print("Name und Email müssen angegeben werden!")
        return None
    # Erklärung: Es können beliebige Keyword-Argumente übergeben werden. Sollte jedoch entweder
    # "name" oder "email" fehlen, dann wird die Profilerstellung mit einem Kommentar abgebrochen
    # und nichts zurückgegeben. Es treten keine Programmfehler auf.

    profile = {}

    for key, value in fields.items():
        profile[key] = value

    return profile


alice = create_user_profile(name="Alice", age=33, city="New York", email = "alice@tn.techstarter.de")
bob = create_user_profile(name="Bob", last_name="Smith", age=22, phone_number=1234567890)

print(alice)
print(bob)