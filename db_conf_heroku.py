import dj_database_url
import psycopg2

DATABASELINK = "postgres://esqqjgvmoduonp:линк на ваше бд"


db_info = dj_database_url.config(default=DATABASELINK)
connection = psycopg2.connect(database=db_info.get('database'),
		    		user=db_info.get('user'),
		    		password=db_info.get('pass'),
		    		host=db_info.get('host'),
		    		port=db_info.get('5432'))
cursor = connection.cursor()

cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar")

connection.commit()

connection.close()

cursor.close()




# # Импортируем библиотеку, соответствующую типу нашей базы данных 
# import sqlite3

# # Создаем соединение с нашей базой данных
# # В нашем примере у нас это просто файл базы
# conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# # Создаем курсор - это специальный объект который делает запросы и получает их результаты
# cursor = conn.cursor()

# # ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# # КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

# # Не забываем закрыть соединение с базой данных
# conn.close()