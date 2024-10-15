from datetime import datetime
from sqlalchemy import Column , Integer , String , DateTime , Enum , ForeignKey
from ..datebase import Base
from app.enums import TokenStatus


class ResetPassword(Base):
    __tablename__ = "reset_password"

    id = Column(Integer , primary_key=True)
    employee_id = Column(Integer , ForeignKey("employees.id") , nullable=False )
    email = Column(String , nullable = False)
    toekn = Column(String , nullable = False)
    status = Column(Enum(TokenStatus) , nullable = False)
    created_on = Column(DateTime , nullable =False , default = datetime.now(datetime.utc))