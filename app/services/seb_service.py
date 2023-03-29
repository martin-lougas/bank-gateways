from app.models.account_statement import AccountStatementRequest
from http.client import HTTPSConnection
import ssl
from urllib.parse import urlencode

import logging

logging.basicConfig(level=logging.DEBUG)


cert_file = "app/cert/certificate.pem"
key_file = "app/cert/certificate.key"
url = "test.api.bgw.baltics.sebgroup.com"

context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)


def get_current_transactions(request: AccountStatementRequest):
    conn = HTTPSConnection(url, context=context)
    headers = {
        "content-type": "*/*",
        "orgid": f"{request.organizationId}",
        "accept": "application/xml"
    }

    payload = {
        "iban": request.iban,
        "currency": request.currency,
        "page": str(request.page),
        "size": str(request.size),
        "includeFutureDate": request.includeFutureDate
    }

    parameters = urlencode(payload, doseq=True).replace("+", "%20")
    
    conn.request("GET", f"/v1/accounts/{request.iban}/current-transactions?{parameters}", headers=headers)

    return conn.getresponse().read().decode()
