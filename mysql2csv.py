#!/usr/bin/env python
'''Mysql database to csv exporter'''

import sys, os, datetime
import MySQLdb
import csv

def export(host,user,passwd,dbname):
  '''Export a database into csv files.'''

  db=MySQLdb.connect(host,user,passwd,dbname)
  tables=db.cursor()
  tables.execute('SHOW TABLES')

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
    
if __name__=="__main__":
  if len(sys.argv)!=5:
    print """Usage:
    %s host user passwd db""" % sys.argv[0]
    sys.exit(1)
  export(*sys.argv[1:])

