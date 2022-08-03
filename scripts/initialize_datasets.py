from alembic import config
from google.cloud import bigquery
from pathlib import Path

PKG_DIR = Path(__file__).resolve().parents[1]

alembic_cfg_path = PKG_DIR / "alembic.ini"
schema_init_path = (
    PKG_DIR / "dp_kobi_database" / "schema_initialization_sql" / "schemas.sql"
)
alembic_cfg = config.Config(alembic_cfg_path)
project = alembic_cfg.get_main_option("gcp.project.id")

client = bigquery.Client(project=project)

bigquery_job = client.query(schema_init_path.read_text().format(project=project))
bigquery_job.result()
