import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "postgresql://postgres:w7726791@localhost:5432/postgres"

Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subject'
    # Указываем точные названия колонок из вашего требования
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(100), nullable=False)

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture
def db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    #Удаляем ID 17 перед тестом, если он остался от прошлых запусков
    session.query(Subject).filter(Subject.subject_id == 17).delete()
    session.commit()

    yield session

    #Удаляем ID 17 после каждого теста
    session.query(Subject).filter(Subject.subject_id == 17).delete()
    session.commit()
    session.close()


# --- ТЕСТЫ ---

def test_add_subject_economy(db_session):
    """Тест 1: Добавление 'Economy' с id 17"""
    new_subject = Subject(subject_id=17, subject_title='Economy')
    db_session.add(new_subject)
    db_session.commit()

    result = db_session.query(Subject).filter_by(subject_id=17).first()
    assert result is not None
    assert result.subject_title == 'Economy'


def test_update_subject_economy(db_session):
    """Тест 2: Изменение названия предмета на 'Economy' для id 17"""
    # Сначала создаем запись с другим названием
    initial_subject = Subject(subject_id=17, subject_title='Old Subject')
    db_session.add(initial_subject)
    db_session.commit()

    # Изменяем на 'Economy'
    initial_subject.subject_title = 'Economy'
    db_session.commit()

    updated = db_session.query(Subject).filter_by(subject_id=17).first()
    assert updated.subject_title == 'Economy'


def test_delete_subject_economy(db_session):
    """Тест 3: Удаление предмета 'Economy' с id 17"""
    # Подготовка: создаем запись
    subject_to_del = Subject(subject_id=17, subject_title='Economy')
    db_session.add(subject_to_del)
    db_session.commit()

    # Удаление
    db_session.delete(subject_to_del)
    db_session.commit()

    result = db_session.query(Subject).filter_by(subject_id=17).first()
    assert result is None
