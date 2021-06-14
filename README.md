# നിശാഗന്ധി 
![nishagandhibot](https://telegra.ph/file/6ab78bdbbb4d1226b99ec.jpg)
Telegram Voice Chat Bot with Channel Support.

A Telegram Bot to Play Audio in Voice Chats With Youtube and Deezer support.
Supports Live streaming from youtube

official group : [കണിമംഗലം]()

```
Please fork this repository don't import code
Made with Python3
(C) @Full_Crual_Mind
Copyright permission under MIT License
License -> https://github.com/sakhaavvaavaj93/nishagandhibot/master/LICENSE

```

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sakhaavvaavaj93/nishagandhibot)


### Deploy to VPS

```sh
git clone https://github.com/sakhaavvaavaj93/nishagandhibot
cd nishagandhibot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 main.py
```

# Vars:
1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get from my.telegram.org
3. `BOT_TOKEN` : @Botfather
4. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://repl.it/@subinps/getStringName)
5. `CHAT` : ID of Channel/Group where the bot plays Music.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
7. `ADMINS` : ID of users who can use admin commands.
8. `ARQ_API` : Get it for free from [@ARQRobot](https://telegram.dog/ARQRobot), This is required for /dplay to work.
8. `STREAM_URL` : Stream URL of radio station or a youtube live video to stream when the bot starts or with /radio command.

- Enable the worker after deploy the project to Heroku
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy.(24*7 Music even if heroku restarts, radio stream restarts automatically.)  
- To play a song use /play as a reply to audio file or a youtube link.
- Use /play <song name> to play song from youtube and /dplay <song name> to play from Deezer.
- Use /help to know about other commands.

**Features**

- Playlist, queue
- Supports Live streaming from youtube
- Supports both deezer and youtube to search songs.
- Play from telegram file supported.
- Starts Radio after if no songs in playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Automatic restart even if heroku restarts.

### Note

```
Contributions are welcomed, But Kanging and editing a few lines wont make you a Developer.
Fork the repo, Do not Import code.

```
#### Support
[coding king](https://t.me/rosebakthan_bot)

Connect Me On [Telegram](https://telegram.dog/nishagandhibot)

## Credits 
- [Hari-Mowgli](https://t.me/Chegue666)
- [heaven hater](https://t.me/heavenhater_007)
- [lidhiya](https://t.me/Itz_me_lidhuz)
