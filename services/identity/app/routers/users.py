from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def get_all_users():
    return {"message": "all users"}

@router.post("")
async def create_new_user():
    return {"message": "all users"}

@router.get("/{user_id}")
async def get_user_by_id():
    return {"message": "all users"}

@router.put("/{user_id}")
async def update_full_user_by_id():
    return {"message": "all users"}

@router.patch("/{user_id}")
async def partial_update_user_by_id():
    return {"message": "all users"}

@router.delete("/{user_id}")
async def delete_user():
    return {"message": "all users"}