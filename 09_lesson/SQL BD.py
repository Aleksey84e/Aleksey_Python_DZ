from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
# Используем инспектор для получения информации о таблицах
	inspector = inspect(db)
	names = inspector.get_table_names()
	assert names[1] == 'employee'

def test_get_table_names():
    inspector = inspect(db)
    tables = inspector.get_table_names()
    print(tables)
    return tables

table_names = test_get_table_names()
print("Вторая таблица:", table_names[1])

#Получить строки из таблицы: select
def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1['name'] == "QA Студия 'ТестировщикЪ'"

    connection.close()


#Получить строку по одному фильтру
def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"

    connection.close()

#Получить строки по двум фильтрам
def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company "
                       "WHERE \"is_active\" = :is_active AND id >= :id")
    result = connection.execute(sql_statement, {"id": 65, "is_active": True})
    rows = result.mappings().all()

    assert len(rows) == 0

#Добавить компанию: insert
def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO company(name, is_active, create_timestamp, change_timestamp) VALUES (:new_name, TRUE, NOW(), NOW())")
    connection.execute(sql, {"new_name": "FIGNYA"})

    transaction.commit()
    connection.close()

#Изменить компанию: update
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    connection.execute(sql, {"descr": 'New go', "id": 25})

    transaction.commit()
    connection.close()

#Удалить компанию: delete
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM company WHERE id = :id")
    connection.execute(sql, {"id":25})

    transaction.commit()
    connection.close()

