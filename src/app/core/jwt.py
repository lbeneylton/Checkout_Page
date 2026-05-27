from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JoseError

from src.app.core.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


def create_access_token(data: dict, expire_minutes=30) -> bytes:
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)

    payload.update({
        "exp": int(expire.timestamp())
    })

    header = {"alg": ALGORITHM}

    token = jwt.encode(header, payload, SECRET_KEY)
    return token


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY)
        payload.validate()  # valida expiração (exp)

        return payload
    except JoseError:
        return None
