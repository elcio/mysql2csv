import sys, os, datetime
import MySQLdb
import csv

if len(sys.argv)!=5:
  print """Usage:
  %s host user passwd db""" % sys.argv[0]
  sys.exit(1)

db=MySQLdb.connect(*sys.argv[1:])
tables=db.cursor()
tables.execute('SHOW TABLES')

dbname=sys.argv[4]

if not os.path.isdir(dbname):
  os.mkdir(dbname)

for table in tables:
  f=csv.writer(open(os.path.join(dbname,"%s.csv" % table),'w'))
  colunas=db.cursor()
  colunas.execute('DESCRIBE %s' % table)
  f.writerow([i[0] for i in colunas])
  dados=db.cursor()
  dados.execute('SELECT * FROM %s' % table)
  f.writerows(dados)
    

