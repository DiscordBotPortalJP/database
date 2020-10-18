from pydantic import BaseModel


class DiscordBotBase(BaseModel):
    user_id: int
    name: str


class DiscordBotCreate(DiscordBotBase):
    pass


class DiscordBot(DiscordBotBase):
    class Config:
        orm_mode = True
