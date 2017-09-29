import psycopg2

try:
    conn = psycopg2.connect(database="adriansotosuarez",
            user="adriansotosuarez", host="localhost",
            password="")
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute("SELECT * FROM R")

    row_r = cur.fetchone()
    while row_r:
        cur2.execute("SELECT * FROM S")
        row_s = cur2.fetchone()
        while row_s:
            if (row_r[1] == row_s[0]):
                print("{} - {}".format(row_r, row_s))
            row_s = cur2.fetchone()
        row_r = cur.fetchone()

except:
    print("Hubo algún problema")
