import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

class TwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=os.getenv('TWITCH_IRC_TOKEN'),
            client_id=os.getenv('TWITCH_CLIENT_ID'),
            nick=os.getenv('TWITCH_BOT_NICKNAME'),
            prefix='!',
            initial_channels=[os.getenv('TWITCH_CHANNEL')]
        )

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

def start_twitch_bot():
    bot = TwitchBot()
    bot.run()
