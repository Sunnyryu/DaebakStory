import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def Read():
    pw = os.getenv("PASSWORD")
    user = os.getenv("USER")
    db = os.getenv("DB")
    connection = None
    rows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= user,
                                 password= pw,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            csv_product = open('/home/sunny/DaebakStudy/Sunny/9999/wysiwyg2/editor/static/csv/BR-banharimarket--268items.csv', 'r', encoding='utf-8')
            csv_product_reader = csv.reader(csv_product)
            next(csv_product_reader)
            with connection.cursor() as cursor:
                sql = '''
                SELECT body_HTML FROM product where vendor = %s
                '''
                a = cursor.execute(sql, vendor)
                rows = cursor.fetchall()
                print(rows)

            connection.commit()

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows