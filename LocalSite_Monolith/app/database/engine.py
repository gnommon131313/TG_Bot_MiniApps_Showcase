from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///test_sqlite.db')  # Скорее всего когда-нибудь понадобиться для теста
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)