import sqlite



the =  sqlite.Database('./xhello.db')

the.create_table_users()
the.add_user(id=9, name='test')
