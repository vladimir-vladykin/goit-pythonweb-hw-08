from fastapi import APIRouter

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/")
async def get_contacts():
    return {"test": "test"}


@router.get("/{contact_id}")
async def get_contact(contact_id: int):
    return {"contact_id": contact_id}
