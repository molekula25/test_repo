from aiogram.fsm.state import State, StatesGroup


class CareerChoice(StatesGroup):
    job = State()
    grade = State()
    price = State()

__all__ = ['CareerChoice']



