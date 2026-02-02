from typing import TypeVar, Type, Optional

from pydantic import BaseModel, ValidationError

from krypt.dals.models.base import Base

T = TypeVar('T', bound=BaseModel)

def db_model_to_dto(db_model: Base, dto_type: Type[T]) -> Optional[T]:
    """
    Safe mapping from database models to pydantic models
    
    :param db_model: The database model instance. 
    :type db_model: Base
    :param dto_type: The required Pydantic model output type
    :type dto_type: Type[T]
    :return: A safely cast Pydantic model instance or None if casting failed.
    :rtype: T | None
    """
    if not db_model:
        return None

    try:
        return dto_type.model_validate(db_model)
    except ValidationError:
        return None
