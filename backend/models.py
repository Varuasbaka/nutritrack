from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    full_name = Column(String(255))
    due_date = Column(DateTime, nullable=True)  # Optional for pregnancy tracking

    growth_records = relationship("GrowthRecord", back_populates="user")
    reminders = relationship("Reminder", back_populates="user")
    notes = relationship("Note", back_populates="user")

class GrowthRecord(Base):
    __tablename__ = "growth_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, default=datetime.utcnow)
    age_months = Column(Integer)  # Baby age in months
    weight_kg = Column(Float)
    height_cm = Column(Float)
    head_circumference_cm = Column(Float)

    user = relationship("User", back_populates="growth_records")

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    reminder_date = Column(DateTime)
    type = Column(String(50))  # 'vaccine' or 'appointment'
    completed = Column(Boolean, default=False)

    user = relationship("User", back_populates="reminders")

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notes")