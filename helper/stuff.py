#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"👋🏻 **Hello {ok.user.first_name},**\n\nI'm **Video Compressor Pro** 🗳\nI Can Encode & Compress Your Videos. Reduce Size of Videos With Negligible Quality Change! You Can Generate Sample Videos/ Screenshots Too 🤗!",
        buttons=[
            [Button.inline("⚙️ HELP ⚙️", data="ihelp")],
            [
                Button.url("📢 CHANNEL", url="t.me/AsmSafone"),
                Button.url("SUPPORT 💬", url="t.me/SafoTheBot"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "🗳 **Video Compressor Pro Bot :**\n\n☑️ Can Compress Your Videos With Negligible Quality Change.\n☑️ Can Generate Sample Videos & Screenshots Too.\n☑️ Just Send or Forward Video To Get Available Options.\n☑️ Due To Quality Settings Bot Takes Time To Compress.\n☑️ So, Be Patience & Send Videos One By One After Completing. Please Don't Spam To The Bot. Otherwise You'll Be Ban For Permanent!\n\n🏷 **Developer: @I_Am_Only_One_1** 👑"
    )


async def ihelp(event):
    await event.edit(
        "🗳 **Video Compressor Pro Bot :**\n\n☑️ Can Compress Your Videos With Negligible Quality Change.\n☑️ Can Generate Sample Videos & Screenshots Too.\n☑️ Just Send or Forward Video To Get Available Options.\n☑️ Due To Quality Settings Bot Takes Time To Compress.\n☑️ So, Be Patience & Send Videos One By One After Completing. Please Don't Spam To The Bot. Otherwise You'll Be Ban For Permanent!\n\n🏷 **Developer: @I_Am_Only_One_1** 👑",
        buttons=[Button.inline("🔙 BACK", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"👋🏻 **Hello {ok.user.first_name},**\n\nI'm **Video Compressor Pro** 🗳\nI Can Encode & Compress Your Videos. Reduce Size of Videos With Negligible Quality Change! You Can Generate Sample Videos/ Screenshots Too 🤗!",
        buttons=[
            [Button.inline("⚙️ HELP ⚙️", data="ihelp")],
            [
                Button.url("📢 CHANNEL", url="t.me/AsmSafone"),
                Button.url("SUPPORT 💬", url="t.me/SafoTheBot"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "**Select Compression Mode :**",
        buttons=[
            [
                Button.inline("DEFAULT", data=f"encc{key}"),
                Button.inline("CUSTOM", data=f"ccom{key}"),
            ],
            [Button.inline("BACK", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "**Select Required Option :**",
        buttons=[
            [
                Button.inline("COMPRESS", data=f"sencc{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("GENERATE SAMPLE VIDEO", data=f"gsmpl{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Okay, Send Your Custom Name For That File:")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Custom File Name : {g}\n\nNow, Send Thumbnail Picture For it."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Set Successfully!")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
