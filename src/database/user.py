from tortoise import Model
from tortoise.fields import IntField, CharField


class User(Model):
    id: IntField = IntField(pk=True)
    uid: IntField = IntField(null=True)
    username: CharField = CharField(max_length=32, null=True)

    class Meta:
        table = "users"
        db_table = "users"
        db_table_comment = "User data table"
