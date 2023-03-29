from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid
from app.database.database import Base


class PartnerModel(Base):
    __tablename__ = "partner"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    authorization = relationship("AuthorizationModel", back_populates="partner", foreign_keys="[AuthorizationModel.partner_uuid]")


class AuthorizationModel(Base):
    __tablename__ = "authorization"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    partner_uuid = Column(UUID(as_uuid=True), ForeignKey("partner.uuid"), nullable=False)
    status = Column(String, nullable=False)
    secret_id = Column(UUID(as_uuid=True), nullable=False)
    api_secret = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    partner = relationship("PartnerModel", back_populates="authorization")
