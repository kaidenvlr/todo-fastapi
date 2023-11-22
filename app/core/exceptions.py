from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg if msg else "Bad request")


class UnauthorizedException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=msg if msg else "Unauthorized",
            headers={"WWW-Authenticate": "Bearer"}
        )


class NotFoundException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg if msg else "Not found")


class NonProcessableEntityException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=msg if msg else "Unprocessable Entity"
        )
