from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/signup")
def signup():
    # Регистрация пользователя
    pass

@app.post("/login")
def login():
    # Авторизация пользователя
    pass

@app.post("/game/21/start")
def start_game_21():
    # Начало новой игры 21
    pass

@app.post("/game/21/move")
def move_game_21():
    # Выполнение хода в игре 21
    pass

@app.get("/game/21/results")
def get_game_21_results():
    # Получение результатов игры 21
    pass

@app.post("/game/slots/spin")
def spin_slots_game():
    # Кручение барабанов в игре со слотами
    pass

@app.get("/game/slots/results")
def get_slots_game_results():
    # Получение результатов игры со слотами
    pass

@app.post("/add_balance/{user_id}")
def add_balance(user_id: str, amount: int):
    # Добавление Баланса
    pass