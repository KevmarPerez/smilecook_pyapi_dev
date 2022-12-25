class Config:
    name = "kevin"
    password = "123456"
    db_name = "smilecook"
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{name}:{password}@localhost/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATION = False