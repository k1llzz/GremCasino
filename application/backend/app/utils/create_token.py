from datetime import datetime, timedelta
from jose import jwt


def create_acces_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "L2QMijyRgXKo4mjG8N7NQKGqilWko/V8xRaVBjXlgAw=", "HS256"
    )
    return encoded_jwt
