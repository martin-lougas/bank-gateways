import uuid
import logging
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import class_mapper


from app.database.models import AuthorizationModel, PartnerModel
from app.auth.schema import LoginRequest
from app.helpers.exceptions.invalid_credentials_exception import InvalidCredentialsException
from app.helpers.exceptions.partner_not_found_exception import PartnerNotFoundException

logger = logging.getLogger(__name__)

def model_to_dict(model):
    mapper = class_mapper(model.__class__)
    columns = [column.key for column in mapper.columns]
    get_key_value = lambda c: (c, getattr(model, c))
    return dict(map(get_key_value, columns))


def get_partner_by_api_key(request: LoginRequest, database: Session) -> Optional[AuthorizationModel]:
    logger.info(f"Incoming request {request}")
    try:
        partner = get_partner_by_api_key(request, database)
        validate_credentials(request, partner)
    except InvalidCredentialsException as e:
        logger.error(e)
    except PartnerNotFoundException as e:
        logger.error(e)

    return get_partner_by_id(partner.partner_uuid, database)


def get_partner_by_api_key(request: LoginRequest, database: Session) -> Optional[AuthorizationModel]:
    logger.info(f"Getting partner by api key {request.secret_id}")
    partner = database.query(AuthorizationModel).filter(AuthorizationModel.secret_id == request.secret_id).first()
    if partner is None:
        logger.info(f"Partner not found for {request}")
        return None

    logger.info(f"Found partner {model_to_dict(partner)}")

    return partner


def get_partner_by_id(partner_uuid: uuid.UUID, database: Session) -> Optional[PartnerModel]:
    return (
        database.query(PartnerModel)
        .filter(PartnerModel.uuid == partner_uuid)
        .first()
    )


def validate_credentials(request: LoginRequest, parameters) -> bool:
    logger.info(f"Validating credentials {request} against {parameters}")
    if (
            request.secret_id != parameters.secret_id
            and request.secret_key != parameters.api_secret
    ):
        logger.info(f"Invalid credentials {request} against {parameters}")
    return True
