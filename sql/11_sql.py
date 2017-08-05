import sqlite3

with sqlite3.connect("new.db") as connection:
    #SQL functions
    c = connection.cursor()
    sql = {'average': "SELECT avg(population) FROM population",
            'maximum': "SELECT max(population) FROM population",
            'minimum': "SELECT min(population) FROM population",
            'sum': "SELECT sum(population) FROM population",
            'count': "SELECT count(city) FROM population"}
    for keys, values in sql.items():
        #execute each query
        c.execute(values)
        # fetchone() retrieves one record from the query
        result = c.fetchone()
        print (keys + ":",result[0])

        """
        1. Essentially, we created a dictionary of SQL statements and then looped through the
        SQL Functions
        dictionary, executing each statement.
        2. Next, using a for loop, we printed the results of each SQL query.
        """
