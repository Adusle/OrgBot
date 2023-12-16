from aiogram import Router, F, types
from aiogram.types import Message
router = Router()

@router.message(F.text)
async def create_event(message: types.Message):
    await message.answer(text="Здарова")
