import argparse

import boto3


def main():
    parser = argparse.ArgumentParser(
        description='Archive PostgreSQL tables to S3')
    parser.add_argument(
        'dsn', help='PostgreSQL DSN (e.g. postgresql://localhost:5432/mydb)')
    args = parser.parse_args()

    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

    print(args.dsn)
