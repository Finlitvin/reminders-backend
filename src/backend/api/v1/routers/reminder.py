from fastapi import APIRouter
from fastapi import status

router = APIRouter()


@router.get(
    "/test",
    status_code=status.HTTP_200_OK,
    name="nesting:load",
)
async def test():
    return {"test": "hello"}
