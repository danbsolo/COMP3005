import psycopg2
import json
from  datetime import datetime


class PSQL_Connection:
    def __init__(self, host, database, user, password, port):
        # Connect Python to the local postgresql server
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

        # Create a cursor for executing statements and fetching their results
        self.cur = self.conn.cursor()


    # Print each result line by line for simple viewing
    def printResultsLineByLine(self):
        while result := self.cur.fetchone():
            print(result)

    # Application functions. Only novel part is that it includes placeholders, as mentioned in lecture.
    def getAllStudents(self):
        self.cur.execute("SELECT * FROM students")
        self.printResultsLineByLine()


    def addStudent(self, first_name, last_name, email, enrollment_date):
        self.cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) \
                          VALUES (%s, %s, %s, %s)",
                          (first_name, last_name, email, enrollment_date))


    def updateStudentEmail(self, student_id, new_email):
        self.cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                         (new_email, student_id))


    def deleteStudent(self, student_id):
        self.cur.execute("DELETE FROM students WHERE student_id = %s",
                         (student_id))


    # Commit all changes and close
    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()



if __name__ == "__main__":
    with open("creds.json", "r") as f:
        creds = json.load(f)

    psql = PSQL_Connection(creds["HOST"], creds["DATABASE"], creds["USER"], creds["PASSWORD"], creds["PORT"])

    # 1
    psql.getAllStudents()

    # 2
    psql.addStudent("Daniel", "Solomon", "example@gmail.com", datetime.now())
    
    # 3
    psql.updateStudentEmail("4", "kekw@kek.conn")
    
    # 4
    psql.deleteStudent("1")

    psql.close()
    