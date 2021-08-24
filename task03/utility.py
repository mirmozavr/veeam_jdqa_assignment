import secrets
import string


def gen_id(size: int) -> str:
    return "".join(secrets.choice(string.digits) for i in range(size))


def gen_key(size: int) -> str:
    return secrets.token_urlsafe(size)


def gen_message():
    return "Random message: " + " ".join(
        secrets.token_urlsafe(secrets.randbelow(8))
        for _ in range(1 + secrets.randbelow(4))
    )
