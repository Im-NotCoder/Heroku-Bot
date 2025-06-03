from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import config
import random

from config import START_IMAGES, OWNER

from PURVIBOTS import app



@app.on_message(filters.command(["start"]))
async def start(client: Client, message):
    user_mention = message.from_user.mention  # user mention
    random_image = random.choice(START_IMAGES)  

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴀʙᴏᴜᴛ ʙᴏᴛ", callback_data="about")],
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/purvi_support")
        ]
    ])

    await message.reply_photo(
        photo=random_image,
        caption=f"**๏ ʜᴇʟʟᴏ {user_mention} !!**\n\n**๏ ɪ ᴀᴍ ᴀ ʜᴇʀᴋᴏᴜ ᴄᴏɴᴛʀᴏʟʟᴇʀ ʙᴏᴛ. ɪ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴏɴᴛʀᴏʟ ʜᴇʀᴋᴏᴜ ᴀᴄᴄᴏᴜɴᴛ & ᴀᴘᴘs 🤖**\n\n**๏ ᴄʜᴇᴀᴋ ᴀʙᴏᴜᴛ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs.**",
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("about"))
async def about_callback(client: Client, query: CallbackQuery):
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/purvi_support"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/PURVI_UPDATES")
        ],
        [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back_to_start")]
    ])

    await query.message.edit_text(
        "**๏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ғᴏʀ ᴄᴏɴᴛʀᴏʟ ʜᴇʀᴋᴏᴜ ᴀᴘᴘs. ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org/) ʜᴇʟᴘ ᴡɪᴛʜ [ᴘʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram).**\n\n**<u>๏ sᴏᴍᴇ ᴄᴏᴍᴍᴀɴᴅ :-</u>**\n\n**/start :- sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.**\n**/help :- ᴄʜᴇᴀᴋ ʙᴏᴛs ʜᴇʟᴘ.**\n\n**<u>๏ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅ :-</u>**\n\n**/myhost :- ᴄᴏɴᴛʀᴏʟ ᴀᴘᴘs.**\n**/host :- ʜᴏsᴛ ɴᴇᴡ ᴀᴘᴘ.**\n\n**๏ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ғᴏʀ ɴᴇᴡ ᴜᴘᴅᴀᴛᴇs.**",
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(client: Client, query: CallbackQuery):
    user_mention = query.from_user.mention

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴀʙᴏᴜᴛ ʙᴏᴛ", callback_data="about")],
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/purvi_support")
        ]
    ])

    await query.message.edit_text(
        f"**๏ ʜᴇʟʟᴏ {user_mention} !!**\n\n**๏ ɪ ᴀᴍ ᴀ ʜᴇʀᴋᴏᴜ ᴄᴏɴᴛʀᴏʟʟᴇʀ ʙᴏᴛ. ɪ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴏɴᴛʀᴏʟ ʜᴇʀᴋᴏᴜ ᴀᴄᴄᴏᴜɴᴛ & ᴀᴘᴘs 🤖**\n\n**๏ ᴄʜᴇᴀᴋ ᴀʙᴏᴜᴛ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs.**",
        reply_markup=buttons
    )
