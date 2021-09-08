from app.services.Storage import Storage
from app.services.Sign import Sign


def sign() -> Sign:
    """This function is called when the service is started."""
    return Sign()


def storage() -> Storage:
    """This function is called when the service is started."""
    return Storage
