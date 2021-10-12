from gleifpy.db import engine
from gleifpy.models import Base


def recreate_db() -> None:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    print('Start creating tables...')

    # Base.metadata.create_all(engine)
    recreate_db()

    print('Tables created.')
