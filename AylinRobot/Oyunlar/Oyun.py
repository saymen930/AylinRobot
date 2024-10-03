import os
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters


@app.on_message(filters.command("zar"))
async def roll_dice(bot, message):
    await app.send_dice(message.chat.id, "🎲")


@app.on_message(filters.command("ok"))                                      
async def roll_arrow(bot, message):
    await app.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("top"))
async def roll_goal(bot, message):
    await app.send_dice(message.chat.id, "⚽️")

@app.on_message(filters.command("jackpot"))
async def roll_luck(bot, message):
    await app.send_dice(message.chat.id, "🎰")

@app.on_message(filters.command("basket"))
async def roll_throw(bot, message):
    await app.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command(["bowling"]))
async def roll_bowling(bot, message):
    await app.send_dice(message.chat.id, "🎳")
