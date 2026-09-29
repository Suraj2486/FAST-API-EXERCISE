from passlib.context import CryptContext
from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from app.db import Base
from app.models import user
import enum

class TicketPriority(str, enum(Enum)):
    LOW = "LOW"
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = "Critical"

class TicketStatus(str, enum(Enum)):
    REPORTED = "Reported"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    WAITING_FOR_USER = "Waiting for User"
    RESOLVED = "Resolved"
    CLOSED = "Closed"


class Ticket(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    location = Column(String, nullable = False)
    priority = Column(enum(TicketPriority), nullable = False)
    status = Column(enum(TicketStatus), nullable = False, default = "Reported")
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    technician_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    user = relationship("User")