import psycopg2
DBNAME = "news"


def query_db(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    query_result = c.fetchall()
    db.close()
    return query_result


def popular_three_articles():
    print("1. What are the most popular three articles of all time? \n ")
    print('\t' + " title   \t                   "+"views \n ")
    query1 = "SELECT * from views LIMIT 3;"
    results = query_db(query1)
    for i in results:
        print('\t{}   {} views'.format(i[1], i[0]))


def popular_authors():
    print("\n Who are the most popular article authors of all time ? \n ")
    print('\t' + "  author name  " + '\t  \t \t ' + "  views \n ")
    query2 = """SELECT name , SUM(number_of_viewer) AS number_of_viewers FROM
    author_views GROUP BY name
    ORDER BY number_of_viewers DESC ;"""
    results = query_db(query2)
    for i in results:
        print('\t{0:<25}{1:>12} views'.format(i[0], i[1]))


def errors():
    print("\n 3. On which days did more than 1% of requests lead to error \n ")
    query3 = "SELECT * FROM percent WHERE percent >1.0;"
    results = query_db(query3)
    for i in results:
        print ('\t' + str(i[0]) + '\t \t' + str(i[1]) + '%')


if __name__ == '__main__':
    popular_three_articles()
    popular_authors()
    errors()
