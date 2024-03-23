from dataclasses import dataclass
from environs import Env

@dataclass
class TelegramBot:
    token:str

@dataclass
class SeaBattle:
    size:int

@dataclass
class Config:
    telegram_bot:TelegramBot
    sea_battle:SeaBattle

def add_config():
    env = Env()
    env.read_env()

    return Config(
        telegram_bot=TelegramBot(
            token=env('BOT_TOKEN')
        ),
        sea_battle=SeaBattle(
            size=env.int('SEA_BATTLE_SIZE')
        )
    )