Requires the psycopg2 library. Install with `pip install psycopg2`.

If you're running main.py directly, you'll need to create a creds.json file located in the same directory as main.py. See `credsExample.json`.

If you're not running main.py directly, in your script, simply:
- import main
- create a PSQL_Connection(host, database, user, password, port) object
- run the application functions via the object
