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
#    License can be found in <https://github.com/1Danish-00/CompressorBot/blob/main/License> .


from .funcn import *


async def screenshot(e):
    await e.edit("`Generating Screenshots...`")
    COUNT.append(e.chat_id)
    wah = e.pattern_match.group(1).decode("UTF-8")
    key = decode(wah)
    out, dl, thum, dtime = key.split(";")
    os.mkdir(wah)
    tsec = await genss(dl)
    fps = 10 / tsec
    ncmd = f"ffmpeg -i '{dl}' -vf fps={fps} -vframes 10 '{wah}/pic%01d.png'"
    process = await asyncio.create_subprocess_shell(
        ncmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    await process.communicate()
    try:
        pic = glob.glob(f"{wah}/*")
        await e.client.send_file(e.chat_id, pic)
        await e.client.send_message(
            e.chat_id,
            "**Please Check Your Screenshots Above!** 😊",
            buttons=[
                [
                    Button.inline("SKIP", data=f"skip{wah}"),
                    Button.inline("COMPRESS", data=f"sencc{wah}"),
                ],
                [Button.inline("GENERATE SAMPLE VIDEO", data=f"gsmpl{wah}")],
            ],
        )
        COUNT.remove(e.chat_id)
        shutil.rmtree(wah)
    except Exception:
        COUNT.remove(e.chat_id)
        shutil.rmtree(wah)


async def stats(e):
    try:
        wah = e.pattern_match.group(1).decode("UTF-8")
        wh = decode(wah)
        out, dl, thum, dtime = wh.split(";")
        ot = hbs(int(Path(out).stat().st_size))
        ov = hbs(int(Path(dl).stat().st_size))
        ans = f"Downloaded:\n{ov}\n\nCompressing:\n{ot}\n\nGet Updates @AsmSafone! "
        await e.answer(ans, cache_time=0, alert=True)
    except BaseException:
        await e.answer("Something Went Wrong 🤔\nPlease Resend That Media!", cache_time=0, alert=True)


async def encc(e):
    es = dt.now()
    COUNT.append(e.chat_id)
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    nn = await e.edit(
        "`Compressing...`",
        buttons=[
            [Button.inline("STATUS", data=f"stats{wah}")],
            [Button.inline("CANCEL PROCESS", data=f"skip{wah}")],
        ],
    )
    cmd = f"ffmpeg -i '{dl}' -preset ultrafast -vcodec libx265 -crf 28 '{out}' -y"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    er = stderr.decode()
    try:
        if er:
            await e.edit(str(er) + "\n\n**ERROR** Contact @I_Am_Only_One_1 👑")
            COUNT.remove(e.chat_id)
            os.remove(dl)
            os.remove(out)
            return
    except BaseException:
        pass
    stdout.decode()
    ees = dt.now()
    ttt = time.time()
    await nn.delete()
    nnn = await e.client.send_message(e.chat_id, "`Uploading...`")
    ds = await e.client.send_file(
        e.chat_id,
        file=f"{out}",
        force_document=True,
        thumb=thum,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, nnn, ttt, "uploading..", file=f"{out}")
        ),
    )

    org = int(Path(dl).stat().st_size)
    com = int(Path(out).stat().st_size)
    pe = 100 - ((com / org) * 100)
    per = str(f"{pe:.2f}") + "%"
    eees = dt.now()
    x = dtime
    xx = ts(int((ees - es).seconds) * 1000)
    xxx = ts(int((eees - ees).seconds) * 1000)
    a1 = f"https://nekobin.com/{code(await info(dl))}"
    a2 = f"https://nekobin.com/{code(await info(out))}"
    dk = await ds.reply(
        f"Original Size : {hbs(org)}\nCompressed Size : {hbs(com)}\nCompressed Percentage : {per}\n\nMediainfo: [Before]({a1})♾[After]({a2})\n\nDownloaded in {x}\nCompressed in {xx}\nUploaded in {xxx}\nBy @I_Am_Only_One_1 👑",
        link_preview=False,
    )
    await ds.forward_to(LOG)
    await dk.forward_to(LOG)
    await nnn.delete()
    COUNT.remove(e.chat_id)
    os.remove(dl)
    os.remove(out)


async def sample(e):
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    COUNT.append(e.chat_id)
    out, dl, thum, dtime = wh.split(";")
    ss, dd = await duration_s(dl)
    xxx = await e.edit(
        "`Generating Sample Video...`",
        buttons=[
            [Button.inline("STATUS", data=f"stats{wah}")],
            [Button.inline("CANCEL PROCESS", data=f"skip{wah}")],
        ],
    )
    ncmd = f"ffmpeg -i '{dl}' -preset ultrafast -ss {ss} -to {dd} -c:v libx265 -crf 28 '{out}'"
    process = await asyncio.create_subprocess_shell(
        ncmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    er = stderr.decode()
    try:
        if er:
            await e.edit(str(er) + "\n\n**ERROR** Contact @I_Am_Only_One_1 👑")
            COUNT.remove(e.chat_id)
            os.remove(dl)
            os.remove(out)
            return
    except BaseException:
        pass
    stdout.decode()
    ttt = time.time()
    try:
        ds = await e.client.send_file(
            e.chat_id,
            file=f"{out}",
            force_document=False,
            thumb=thum,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, xxx, ttt, "uploading..", file=f"{out}")
            ),
            buttons=[
                [
                    Button.inline("SCREENSHOTS", data=f"sshot{wah}"),
                    Button.inline("COMPRESS", data=f"sencc{wah}"),
                ],
                [Button.inline("SKIP", data=f"skip{wah}")],
            ],
        )
        os.remove(out)
        COUNT.remove(e.chat_id)
        await xxx.delete()
    except BaseException:
        os.remove(out)
        COUNT.remove(e.chat_id)


async def encod(event):
    if not event.is_private:
        return
    user = await event.get_chat()
    if not event.media:
        return
    try:
        if "video" not in event.media.document.mime_type.split("/"):
            return
    except BaseException:
        return
    try:
        oc = event.fwd_from.from_id.user_id
        occ = (await event.client.get_me()).id
        if oc == occ:
            return await event.reply("`This Video File Is Already Compressed! 😕`")
    except BaseException:
        pass
    if (event.media.document.size) < 1024 * 1024 * 3:
        return await event.reply(
            "You Sending Less Than 3MB of Video To Compress!\nGreat...Seriously? 😑"
        )
    xxx = await event.reply("`Downloading...`")
    # pp = []
    # async for x in event.client.iter_participants("AsmSafone"):
    #    pp.append(x.id)
    # if (user.id) not in pp:
    #    return await xxx.edit(
    #        "U Must Subscribe This Channel To Use This Bot",
    #        buttons=[Button.url("JOIN CHANNEL", url="t.me/AsmSafone")],
    #    )
    if len(COUNT) > 3 and user.id != OWNER:
        llink = (await event.client(cl(LOG))).link
        return await xxx.edit(
            "**Server Overloaded 😢** \nAlready 5 Compression Running!😑",
            buttons=[Button.url("🤖 Check Working Status 🤖", url=llink)],
        )
    if user.id in COUNT and user.id != OWNER:
        return await xxx.edit(
            "Already Your 1 Request Processing\nPlease Wait Until Finish That! 😊"
        )
    COUNT.append(user.id)
    s = dt.now()
    ttt = time.time()
    await event.forward_to(LOG)
    gg = await event.client.get_entity(user.id)
    name = f"[{get_display_name(gg)}](tg://user?id={user.id})"
    await event.client.send_message(
        LOG, f"🎬 **Compressing Video:** {len(COUNT)} \n**Started For:** {name} ✅"
    )
    dir = f"downloads/{user.id}/"
    if not os.path.isdir(dir):
        os.mkdir(dir)
    try:
        dl = await event.client.download_media(
            event.media,
            dir,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, xxx, ttt, "Downloading")
            ),
        )
    except BaseException:
        os.remove(dl)
        COUNT.remove(user.id)
        return
    es = dt.now()
    kk = dl.split("/")[-1]
    aa = kk.split(".")[-1]
    rr = f"encode/{user.id}"
    if not os.path.isdir(rr):
        os.mkdir(rr)
    bb = kk.replace(f".{aa}", " @AsmSafone.mkv")
    out = f"{rr}/{bb}"
    thum = "68ba9706cdf78f28b4a8c.jpg"
    dtime = ts(int((es - s).seconds) * 1000)
    hehe = f"{out};{dl};{thum};{dtime}"
    key = code(hehe)
    await xxx.delete()
    inf = f"https://nekobin.com/{code(await info(dl))}"
    COUNT.remove(user.id)
    await event.client.send_message(
        event.chat_id,
        f"Select An Option: ([mediainfo]({inf}))",
        link_preview=False,
        buttons=[
            [
                Button.inline("COMPRESS", data=f"sencc{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("GENERATE SAMPLE VIDEO", data=f"gsmpl{key}")],
        ],
    )


async def customenc(e, key):
    es = dt.now()
    COUNT.append(e.chat_id)
    wah = key
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    nn = await e.edit(
        "`Compressing...`",
        buttons=[
            [Button.inline("STATUS", data=f"stats{wah}")],
            [Button.inline("CANCEL PROCESS", data=f"skip{wah}")],
        ],
    )
    cmd = f"ffmpeg -i '{dl}' -preset ultrafast -vcodec libx265 -crf 28 '{out}' -y"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    er = stderr.decode()
    try:
        if er:
            await e.edit(str(er) + "\n\n**ERROR** Contact @I_Am_Only_One_1 👑")
            COUNT.remove(e.chat_id)
            os.remove(dl)
            os.remove(out)
            return
    except BaseException:
        pass
    stdout.decode()
    ees = dt.now()
    ttt = time.time()
    await nn.delete()
    nnn = await e.client.send_message(e.chat_id, "`Uploading...`")
    try:
        ds = await e.client.send_file(
            e.chat_id,
            file=f"{out}",
            force_document=True,
            thumb=thum,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, nnn, ttt, "uploading..", file=f"{out}")
            ),
        )
    except BaseException:
        COUNT.remove(e.chat_id)
        os.remove(dl)
        os.remove(out)
        return
    org = int(Path(dl).stat().st_size)
    com = int(Path(out).stat().st_size)
    pe = 100 - ((com / org) * 100)
    per = str(f"{pe:.2f}") + "%"
    eees = dt.now()
    x = dtime
    xx = ts(int((ees - es).seconds) * 1000)
    xxx = ts(int((eees - ees).seconds) * 1000)
    a1 = f"https://nekobin.com/{code(await info(dl))}"
    a2 = f"https://nekobin.com/{code(await info(out))}"
    dk = await ds.reply(
        f"Original Size : {hbs(org)}\nCompressed Size : {hbs(com)}\nCompressed Percentage : {per}\n\nMediainfo: [Before]({a1})♾[After]({a2})\n\nDownloaded in {x}\nCompressed in {xx}\nUploaded in {xxx}\nBy @I_Am_Only_One_1 👑",
        link_preview=False,
    )
    await ds.forward_to(LOG)
    await dk.forward_to(LOG)
    await nnn.delete()
    COUNT.remove(e.chat_id)
    os.remove(dl)
    os.remove(out)
