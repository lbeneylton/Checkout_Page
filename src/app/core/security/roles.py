from fastapi import Depends, HTTPException, Path
from src.app.auth.dependencies import get_current_user


def require_role(required_role: str):

    def checker(user=Depends(get_current_user)):

        if user.role != required_role:
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )

        return user

    return checker


def require_owner(
    user_id: int = Path(...),
    user=Depends(get_current_user)
):

    if user.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

    return user
