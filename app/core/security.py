from passlib.context import CryptContext
from itsdangerous import URLSafeSerializer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
serializer = URLSafeSerializer("super-secret")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_token(user_id: int) -> str:
    return serializer.dumps(user_id)

def decode_token(token: str) -> int | None:
    try:
        return serializer.loads(token)
    except Exception:
        return None
