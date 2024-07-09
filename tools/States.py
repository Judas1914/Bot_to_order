from settings import *

# States
class Form(StatesGroup):
    Type_of_work = State()
    Date = State()
    Time = State()
    Tasks = State()
    Htowrite = State()
    Lectur = State()
    Info = State()
