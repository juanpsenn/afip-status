from datetime import datetime

from tortoise import fields
from tortoise.models import Model

from src.v1.databases.settings import TZ_AR


class Status(Model):
    app = fields.CharField(2)
    db = fields.CharField(2)
    auth = fields.CharField(2)
    fetched_at = fields.DatetimeField(default=lambda: datetime.now(TZ_AR))
