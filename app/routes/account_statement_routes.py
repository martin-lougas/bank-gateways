from fastapi import APIRouter, status, Response, HTTPException

from app.models.account_statement import AccountStatementRequest
from app.services.account_statement_service import get_intraday_statement

router = APIRouter(
    tags=["Account Statements"],
    prefix="/account-statements"
)


@router.get("/intraday-report", status_code=status.HTTP_200_OK)
async def get_intraday_report(account_statement_request: AccountStatementRequest):
    try:
        response = get_intraday_statement(account_statement_request)
        return Response(response, media_type="application/xml")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e
