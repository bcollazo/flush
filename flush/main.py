import argparse
import sys

import boto3
import psycopg2


def main():
    parser = argparse.ArgumentParser(
        description='Archive PostgreSQL tables to S3')
    parser.add_argument(
        'dsn', help='PostgreSQL DSN (e.g. postgresql://localhost:5432/mydb)')
    parser.add_argument('tablename', help='Name of table to flush')
    args = parser.parse_args()
    tablename = args.tablename

    with psycopg2.connect(args.dsn) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT tablename FROM pg_catalog.pg_tables')
            tables = set(i[0] for i in cur.fetchall())
            if tablename not in tables:
                print('{} is not a tablename'.format(tablename))
                sys.exit(1)

            cur.execute("SELECT * FROM {}".format(tablename))
            print("Found {} records in {}".format(cur.rowcount, tablename))

            row = cur.fetchone()
            while row is not None:
                row = cur.fetchone()

    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
