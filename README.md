# flush

Archive PostgreSQL tables to S3.

CLI tool that flushes (exports and deletes) all database rows of a PostgreSQL table into a CSV in a specified S3 bucket. Useful for archiving data and saving money in small infrastructure environments.

## Usage

Ensure you are using correct AWS credentials (as if you were using BOTO: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).

Then:

```
pip install flush
flush postgres://localhost:5432/mydatabase tablename mybucket --truncate
```
