
from pyrogram import Client, idle, filters
import os
from threading import Thread
import sys
from config import Config
from utils import mp
import asyncio
from pyrogram.raw import functions, types


CHAT=Config.CHAT
bot = Client(
    "nishagandhibot",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.startupradio()
        await asyncio.sleep(2)
        await mp.startupradio()

def stop_and_restart():
        bot.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)
    
bot.run(main())
bot.start()
bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Check if bot alive"
            ),
            types.BotCommand(
                command="help",
                description="Shows help message"
            ),
            types.BotCommand(
                command="play",
                description="Play song from youtube/audiofile"
            ),
            types.BotCommand(
                command="dplay",
                description="Play song from Deezer"
            ),
            types.BotCommand(
                command="player",
                description="Shows current playing song with controls"
            ),
            types.BotCommand(
                command="playlist",
                description="Shows the playlist"
            ),
            types.BotCommand(
                command="skip",
                description="Skip the current song"
            ),
            types.BotCommand(
                command="join",
                description="Join VC"
            ),
            types.BotCommand(
                command="leave",
                description="Leave from VC"
            ),
            types.BotCommand(
                command="vc",
                description="Ckeck if VC is joined"
            ),
            types.BotCommand(
                command="stop",
                description="Stops Playing"
            ),
            types.BotCommand(
                command="radio",
                description="Start radio / Live stream"
            ),
            types.BotCommand(
                command="stopradio",
                description="Stops radio/Livestream"
            ),
            types.BotCommand(
                command="replay",
                description="Replay from beggining"
            ),
            types.BotCommand(
                command="clean",
                description="Cleans RAW files"
            ),
            types.BotCommand(
                command="pause",
                description="Pause the song"
            ),
            types.BotCommand(
                command="resume",
                description="Resume the paused song"
            ),
            types.BotCommand(
                command="mute",
                description="Mute in VC"
            ),
            types.BotCommand(
                command="unmute",
                description="Unmute in VC"
            ),
            types.BotCommand(
                command="restart",
                description="Restart the bot"
            )
        ]
    )
)


@bot.on_message(filters.command("reload") & filters.user(Config.ADMINS))
def restart(client, message):
    message.reply_text("Restarting...")
    Thread(
        target=stop_and_restart
        ).start()

idle()
bot.stop()
