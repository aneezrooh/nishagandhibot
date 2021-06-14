
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam *നിശാഗന്ധി* which plays music in Channels and Groups 24*7\n\nI can even Stream Youtube Live in Your Voicechat\n\nDeploy Your Own bot from source code below\n\nHit /help to know about available commands.</b>"
HELP = """

<b>Add the bot and User account in your Group with admin rights.

Start a VoiceChat

Use /play <song name> or use /play as a reply to an audio file or youtube link.

You can also use /dplay <song name> to play a song from Deezer.</b>

**Common Commands**:

**/play**  Reply to an audio file or YouTube link to play it or use /play <song name>.
**/dplay** Play music from Deezer, Use /dplay <song name>
**/player**  Show current playing song.
**/help** Show help for commands
**/playlist** Shows the playlist.

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/mute**  Mute in VC.
**/unmute**  Unmute in VC.
**/restart** Restarts the Bot.
"""

nishagandhi_img = "https://telegra.ph/file/99c7a652091d21bd4fd73.jpg"

@Client.on_message(filters.command('start'))
async def start(client, message): (
    update.effective_message.reply_photo(
                nishagandhi_img,
    buttons = [
        [
        InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/stenzle'),
        InlineKeyboardButton('🤖 Other Bots', url='https://t.me/stenzle/5'),
    ],
    [
        InlineKeyboardButton('👨🏼‍💻 Developer', url='https://t.me/onnupodaappa_bot'),
        InlineKeyboardButton('🧩 Source', url='https://github.com/sakhaavvaavaj93/thamburattiubot'),
    ],
    [
        InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
    HOME_TEXT,
    reply_markup=reply_markup
)

@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/stenzle'),
            InlineKeyboardButton('🤖 Other Bots', url='https://t.me/stenzle/5'),
        ],
        [
            InlineKeyboardButton('👨🏼‍💻 Developer', url='https://t.me/onnupodaappa_bot'),
            InlineKeyboardButton('🧩 Source', url='https://github.com/sakhaavvaavaj93/nishagandhibot'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
