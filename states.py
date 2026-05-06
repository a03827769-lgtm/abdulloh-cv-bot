from aiogram.fsm.state import State, StatesGroup

class HireMeStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_project = State()
    waiting_for_budget = State()
    waiting_for_contact = State()
class AdminStates(StatesGroup):
    waiting_for_broadcast = State()
