from sqlalchemy import Column, Integer, String
from .database import Base


class DiscordBot(Base):
    __tablename__ = 'discord_bots'

    user_id = Column(
        Integer, primary_key=True, autoincrement=False, unique=True, index=True
    )
    name = Column(String)
