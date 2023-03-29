from app.models.account_statement import AccountStatementRequest
from app.services.seb_service import get_current_transactions


def get_intraday_statement(request: AccountStatementRequest):
    return get_current_transactions(request)
