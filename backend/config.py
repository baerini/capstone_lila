db = {
	'user' : 'root',
    'password' : '1111',
    'host' : 'localhost',
    'port' : 3306,
    'database' : 'lila'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"