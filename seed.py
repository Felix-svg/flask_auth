from config import db, app
from models import User, ProgrammingLanguage
from faker import Faker

with app.app_context():
    print("Deleting all records")
    User.query.delete()

    fake = Faker()

    print("Creating users")

    user1 = User(username="blueberry123")
    user1.password_hash = "Pa$$w0rd123"
    user2 = User(username="firefly99")
    user2.password_hash = "Secr3tP@ss"
    user3 = User(username="smilingsam23")
    user3.password_hash = "Rand0mPwd!"
    user4 = User(username="thunderbolt87")
    user4.password_hash = "P@ssw0rd456"
    user5 = User(username="midnightowl55")
    user5.password_hash = "StrongPwd789"
    user6 = User(username="dreamcatcher11")
    user6.password_hash = "12345qwerty"
    user7 = User(username="silverfox42")
    user7.password_hash = "P@ssw0rd!234"
    user8 = User(username="cosmicjazz77")
    user8.password_hash = "MyPwd123$"
    user9 = User(username="blazingstar28")
    user9.password_hash = "Secure12345!"
    user10 = User(username="serenitynow63")
    user10.password_hash = "P@ssw0rd789$"

    db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, user9, user10])
    db.session.commit()

    print("Creating programming languages")
    lang1 = ProgrammingLanguage(name="JavaScript", level="high")
    lang2 = ProgrammingLanguage(name="Python", level="high")
    lang3 = ProgrammingLanguage(name="Java", level="high")
    lang4 = ProgrammingLanguage(name="Go", level="high")
    lang5 = ProgrammingLanguage(name="TypeScript", level="high")
    lang6 = ProgrammingLanguage(name="C", level="low")
    lang7 = ProgrammingLanguage(name="C#", level="low")
    lang8 = ProgrammingLanguage(name="Rust", level="low")
    lang9 = ProgrammingLanguage(name="Kotlin", level="high")
    lang10 = ProgrammingLanguage(name="Assembly", level="low")

    db.session.add_all([lang1, lang2, lang3, lang4, lang5, lang6, lang7, lang8, lang9, lang10])
    db.session.commit()

    print("Seeding db...")
    print("Seeding complete")

