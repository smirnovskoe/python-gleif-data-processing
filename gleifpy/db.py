from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from gleifpy.config import settings

engine = create_engine(settings.DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def get_db_session() -> Session:
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
