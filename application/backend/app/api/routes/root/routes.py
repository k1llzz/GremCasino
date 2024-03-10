from fastapi import APIRouter, status


router = APIRouter()


@router.get("/health")
def health():
    return status.HTTP_200_OK
