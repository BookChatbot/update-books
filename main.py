import aladin
import logging
from db import UseDB
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='log/update.log')


#  db 변수 설정
user = os.environ.get('USER')
passwd = os.environ.get('PASSWD')
host = os.environ.get('HOST')
db = os.environ.get('DB')

# db 연결
use_db = UseDB(user, passwd, host, db)
connection = use_db.connect_db()

# 커서 생성하기
cursor = connection.cursor()

# 신간, 주목할 만한 신간, 에디터 추천, 베스트셀러, 블로거 베스트
#  li = ['ItemNewAll', 'ItemNewSpecial',
#        'ItemEditorChoice', 'Bestseller', 'BlogBest']
li = ['ItemNewAll', 'ItemNewSpecial']
for item_list in li:
    books = aladin.search_list(item_list, num=100)
    use_db.book_to_db(books, cursor, connection)
    logging.info(f"책 {len(books)} 권 데이터 저장 완료\n")
# 연결 종료하기
connection.close()
