import uuid

import sqlalchemy.types as types
from melldechof.localtypes import Presence
from sqlalchemy.ext.compiler import compiles
import sqlalchemy.dialects.postgresql as pg


class DbPresence(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return Presence(value)


@compiles(DbPresence, "sqlite")
def compile_enum_sqlite(type_, compiler, **kw):
    length = max([len(item.value) for item in Presence])
    return f"VARCHAR({length})"


class UUID(types.TypeDecorator):
    impl = types.String

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(pg.UUID())
        else:
            return dialect.type_descriptor(types.String(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return str(value)
        else:
            return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value