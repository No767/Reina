from sqlalchemy import Column, String, Text

from .db_base import Base


class HelpData(Base):

    __tablename__ = "help_data"
    uuid = Column(String, primary_key=True)
    name = Column(String)
    parent_name = Column(String)
    description = Column(Text)
    module = Column(String)

    def __iter__(self):
        yield "uuid", self.uuid
        yield "name", self.name
        yield "parent_name", self.parent_name
        yield "description", self.description
        yield "module", self.module

    def __repr__(self):
        return f"HelpData=(uuid={self.uuid!r}, name={self.name!r}, parent_name={self.parent_name!r}, description={self.description!r}, module={self.module!r})"
