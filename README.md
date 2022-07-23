# Data Platform Database Migrations

Database migration management using Alembic and SQLalchemy for (hopefully) BigQuery data tables.

Note for revisions: some revisions will probably necessarily have to be executed with raw SQL. This
means that when creating an alembic revision (which generates a python file), the SQL file should
be named with the same revision tag (and name if possible, except with .sql ending). This SQL file
can then be loaded in automatically (and be properly tracked) during the merge / migration process
during the CI/CD github actions workflow. This should be done for both the upgrade and downgrades.
Alternatively, the raw SQL can be managed within the python file itself (which might be easier).


## TODOs

1. Set up branching (main, staging, and everything else later)
2. Create first DDL to create map, agent and patch tables for valorant data
3. Create tables in BQ for valorant scraping of vlr.gg
4. Setup workflow ci/cd for testing new merges on push (in staging env)
5. Setup workflow ci/cd for publishing changes to production (main branch)
