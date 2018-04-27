#!/usr/bin/env python3

import psycopg2

# queries to fetch data from datbase 
# query to get the top 3 most popular articles 
get_print_top_articles = """SELECT articles.title, COUNT(*) AS num
                FROM articles
                JOIN log
                ON log.path LIKE concat('/article/%', articles.slug)
                GROUP BY articles.title
                ORDER BY num DESC
                LIMIT 3;
"""

# query to get top 3 most popular authors
get_print_top_authors = """SELECT authors.name, COUNT(*) AS num
               FROM authors
               JOIN articles
               ON authors.id = articles.author
               JOIN log
               ON log.path like concat('/article/%', articles.slug)
               GROUP BY authors.name
               ORDER BY num DESC
               LIMIT 3;
"""

# query to get days with more than 1% of errors
get_days_with_errors = """select time, percentageoffailure
            from errorpercent
            where percentageoffailure > 1;
"""

# Query data from the database,with help of DB-API
def execute_query(query):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Print title for a user friendly output 
def display_title(title):
    print ("\n\t\t" + title + "\n")


# Print top three articles of all time
def print_top_articles():
    print_top_articles = execute_query(get_print_top_articles)
    display_title("The most popular three articles of all time")

    for title, num in print_top_articles:
        print(" \"{}\" -- {} views".format(title, num))


# Print top authors of all time
def print_top_authors():
    print_top_authors = execute_query(get_print_top_authors)
    display_title(" The most popular article authors of all time")

    for name, num in print_top_authors:
        print(" {} -- {} views".format(name, num))


# Print the days with more than 1% errors
def higest_error_days():
    higest_error_days = execute_query(get_days_with_errors)
    display_title("Days with more than one percentage of error requests")

    for day, percentageoffailure in higest_error_days:
        print("""{0:%B %d, %Y}
            -- {1:.2f} % errors""".format(day, percentageoffailure))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    higest_error_days()
