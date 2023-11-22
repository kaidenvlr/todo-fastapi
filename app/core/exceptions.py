from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg if msg else "Bad request")


class NotFoundException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg if msg else "Not found")


class NonProcessableEntityException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=msg if msg else "Unprocessable Entity"
        )
