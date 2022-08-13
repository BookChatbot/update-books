import MySQLdb


class UseDB:
    def __init__(self, user, passwd, host, db):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.db = db

    def connect_db(self):
        """
        DATABASE 연결
        """
        connection = MySQLdb.connect(
            user=self.user,
            passwd=self.passwd,
            host=self.host,
            db=self.db,
            charset="utf8")

        return connection

    def book_to_db(self, books, cursor, connection):
        """dictionary형태의 책 정보를 받아와서 db에 저장
        books : 책 여러권의 데이터
        """
        for i in books.keys():
            try:
                sql = 'INSERT INTO books (isbn,title,author,publisher,pubDate,summary,img,genre,rate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                if books[i]['isbn'] != '':
                    val = [books[i]['isbn'], books[i]['title'], books[i]['author'],
                           books[i]['publisher'], books[i]['pubDate'], books[i]['summary'],
                           books[i]['img'], books[i]['genre'], books[i]['rate']]
                    # 데이터 저장하기
                    cursor.execute(sql, val)
                    # 커밋하기
                    connection.commit()
            except Exception as e:
                print(e)
