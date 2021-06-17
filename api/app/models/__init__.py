import datetime

from sqlalchemy import Column, Integer, TIMESTAMP, MetaData
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class BaseModelMixin:
    id = Column(Integer, primary_key=True)
    created_on = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updated_on = Column(TIMESTAMP(timezone=True), onupdate=datetime.datetime.now)
