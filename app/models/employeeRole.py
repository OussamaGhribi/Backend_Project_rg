from sqlalchemy import Column , Integer , foreignKey , Enum
from ..database import Base
from app.enums import RoleType

class EmployeeRole(Base):
    __tablename__ = "employee_roles"

    id = Column(Integer , primaryKey=True , nullable=False)
    employee_id = Column(Integer , ForeignKey=("employees.id"), nullable = False)
    role = Column(Enum(RoleType), nullable = False)