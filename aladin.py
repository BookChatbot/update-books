import requests
import json
import os


key = os.environ.get('ALADIN_KEY')


def json_to_dict(url, informs):
    """가져온 json 데이터를 필요한 책 정보만 추출
        Args:
            url : 입력URL
            informs : 책 정보를 담을 dictionary
    """
    cnt = 0

    try:
        # request 보내기
        response = requests.get(url)
        # 받은 response를 json 타입으로 바뀌주기
        contents = json.loads(response.text)
        for content in contents["item"]:
            isbn = content["isbn13"]
            title = content["title"]
            author = content["author"]
            publisher = content["publisher"]
            pubDate = content["pubDate"]
            summary = content["description"]
            img = content["cover"]
            genre = content["categoryName"].split('>')[1]
            rate = content["customerReviewRank"]
            inform = {
                'isbn': isbn, 'title': title, 'author': author,
                'publisher': publisher, 'pubDate': pubDate, 'summary': summary,
                'img': img, 'genre': genre, 'rate': rate
            }
            informs[cnt] = inform
            cnt += 1

    except Exception as e:
        print(e)

    return informs


def search_keywords(query, num=100):
    """알라딘에서 키워드로 책을 검색하여 정보 반환
        Args:
            query : 검색 키워드
            num : 출력 건수 (기본값 100)
    """
    url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={key}&Query={query}&QueryType=Keyword&MaxResults={num}&start=1&SearchTarget=Book&output=js&Version=20131101"
    informs = {}
    informs = json_to_dict(url, informs)
    return informs


def search_list(item_list='ItemNewAll', num=100):
    """원하는 리스트를 불러오기
        Args:
            item_list : [ItemNewAll, ItemNewSpecial, ItemEditorChoice, Bestseller, BlogBest] 중 하나 선택
            num : 출력 건수 (기본값 100)
    """
    url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType={item_list}&MaxResults={num}&start=1&SearchTarget=Book&output=js&Version=20131101"
    informs = {}
    informs = json_to_dict(url, informs)
    return informs


if __name__ == "__main__":
    #  word = input('키워드 입력: ')
    isbn = '9788996991342'
    book = search_keywords(isbn, 1)  # 키워드로 1건 검색

    print(book[0]['pubDate'])
    print(book[0]['genre'])
    # 신간, 주목할 만한 신간, 에디터 추천, 베스트셀러, 블로거 베스트
    #  li = ['ItemNewAll', 'ItemNewSpecial',
    #        'ItemEditorChoice', 'Bestseller', 'BlogBest']
    #  books = search_list(li[3], 4)
    #  for i in books.keys():
    #      print(books[i])
