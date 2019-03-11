import argparse
import csv
import sys
import io
from datetime import datetime, timezone

import boto3
import psycopg2

MAX_CSV_ROWS = 10000
DELIMITER = '\t'


def flush(bucket, part_num, records):
    """Write CSV and upload to S3"""
    now = datetime.now(timezone.utc).isoformat()
    key = '{}.{}.tsv'.format(now, part_num)
    print('Flushing {} rows to {}'.format(len(records), key))

    with io.StringIO() as stream:
        writer = csv.writer(stream, delimiter=DELIMITER)
        for record in records:
            writer.writerow(record)
        data = stream.getvalue()
    bucket.put_object(Key=key, Body=data)


def main():
    parser = argparse.ArgumentParser(
        description='Archive PostgreSQL tables to S3')
    parser.add_argument(
        'dsn', help='PostgreSQL DSN (e.g. postgresql://localhost:5432/mydb)')
    parser.add_argument('tablename', help='Name of table to flush')
    parser.add_argument('bucket', help='AWS S3 bucket name')
    args = parser.parse_args()
    tablename = args.tablename

    bucket = boto3.resource('s3').Bucket(args.bucket)

    part_num = 0
    accumulated = []
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
                accumulated.append(row)
                if len(accumulated) >= MAX_CSV_ROWS:
                    flush(bucket, part_num, accumulated)
                    accumulated = []
                    part_num += 1

                row = cur.fetchone()

            flush(bucket, part_num, accumulated)

    print('Done.')
