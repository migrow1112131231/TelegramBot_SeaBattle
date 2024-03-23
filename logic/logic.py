from database import users
from config import Config, add_config
import copy

config = add_config()

ships = [
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0]
]

def reset_field(user_id: int) -> None:
    #таблица с нулями и единицами, где 1 - это корабль
    users[user_id]['ships'] = copy.deepcopy(ships)
    #таблица с нулями
    users[user_id]['field'] = [
        [0 for _ in range(config.sea_battle.size)]
        for _ in range(config.sea_battle.size)
    ]