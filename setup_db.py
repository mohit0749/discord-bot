from database import engine
from database.models import Base


def init_db():
    Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)


if __name__ == '__main__':
    init_db()
