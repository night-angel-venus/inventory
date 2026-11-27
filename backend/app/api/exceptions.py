from fastapi import HTTPException, status

register_exception = HTTPException(
    status_code = status.HTTP_400_BAD_REQUEST,
    detail="This user already exists!"
)

login_exception = HTTPException(
    status_code = status.HTTP_400_BAD_REQUEST,
    detail="Incorrect Username or Password."
)

create_item_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="This item already exists"
)

update_item_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="This item does not exist"
)