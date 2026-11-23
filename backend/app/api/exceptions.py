from fastapi import HTTPException, status

register_exception = HTTPException(
    status_code = status.HTTP_400_BAD_REQUEST,
    detail="This user already exists!"
)

login_exception = HTTPException(
    status_code = status.HTTP_400_BAD_REQUEST,
    detail="Incorrect Username or Password."
)