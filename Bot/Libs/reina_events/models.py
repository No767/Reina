from tortoise import fields
from tortoise.models import Model


class ReinaEvents(Model):
    uuid = fields.CharField(max_length=255, pk=True)
    user_id = fields.BigIntField()
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    date_added = fields.DatetimeField(null=True, auto_now_add=True)
    event_date = fields.DatetimeField(null=True)
    event_passed = fields.BooleanField(default=False)

    class Meta:
        table = "events"

    def __str__(self):
        return self.name
