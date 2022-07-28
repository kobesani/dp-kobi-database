"""empty message

Revision ID: a394a9f52463
Revises: 
Create Date: 2022-07-26 22:49:55.304453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a394a9f52463"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "agents",
        sa.Column("agent_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("origin", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.Column("release", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("agent_id"),
        schema="dp_kobi",
    )
    op.create_table(
        "maps",
        sa.Column("map_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("release", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("map_id"),
        schema="dp_kobi",
    )
    op.create_table(
        "patches",
        sa.Column("patch", sa.Integer(), nullable=False),
        sa.Column("release", sa.Date(), nullable=False),
        sa.Column("size", sa.String(), nullable=True),
        sa.Column("highlights", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("patch"),
        schema="dp_kobi",
    )
    op.create_table(
        "valorant_matches_test",
        sa.Column("match_id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("event", sa.String(), nullable=True),
        sa.Column("stakes", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("map_stats", sa.Boolean(), nullable=False),
        sa.Column("player_stats", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("match_id"),
        schema="dp_kobi",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("valorant_matches", schema="dp_kobi")
    op.drop_table("patches", schema="dp_kobi")
    op.drop_table("maps", schema="dp_kobi")
    op.drop_table("agents", schema="dp_kobi")
    # ### end Alembic commands ###