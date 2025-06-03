from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import config 
from config import START_IMAGES
from PURVIBOTS import app



@app.on_message(filters.command(["help"]))
async def help_command(client: Client, message):
    random_image = random.choice(START_IMAGES)  

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/purvi_support"),
        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_help")]
    ])

    await message.reply_photo(
        photo=random_image,
        caption=(
            "**<u>๏ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅ :-</u>**\n\n"
            "**/start :- sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.**\n"
            "**/help :- ᴄʜᴇᴀᴋ ʙᴏᴛs ʜᴇʟᴘ.**\n\n"
            "**<u>๏ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅ :-</u>**\n\n"
            "**/myhost :- ᴄᴏɴᴛʀᴏʟ ᴀᴘᴘs.**\n"
            "**/host :- ʜᴏsᴛ ɴᴇᴡ ᴀᴘᴘ.**\n\n"
            "**๏ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ғᴏʀ ɴᴇᴡ ᴜᴘᴅᴀᴛᴇs.**"
        ),
        reply_markup=buttons
    )

# ❌ Close बटन का Callback
@app.on_callback_query(filters.regex("close_help"))
async def close_callback(client: Client, query: CallbackQuery):
    await query.message.delete()
