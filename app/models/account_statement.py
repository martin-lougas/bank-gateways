from typing import Optional
from pydantic import BaseModel


class AccountStatementRequest(BaseModel):
    organizationId: str
    iban: str
    currency: str
    page: int
    size: int
    transactionIdGreaterThan: Optional[int] = None
    includeFutureDate: str
