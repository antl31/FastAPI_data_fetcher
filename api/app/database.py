from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.app import config

settings = config.get_settings()

engine = create_engine(
    settings.database_uri,
    pool_size=20,
    max_overflow=10,
    connect_args={"connect_timeout": 10},
)
Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
