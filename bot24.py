import discord, asyncio, random, time
from itertools import cycle
import aiohttp
from copy import deepcopy
from discord import FFmpegPCMAudio
import youtube_dl, os, mechanize
from urllib.parse import urlparse
from youtubesearchpython import VideosSearch
import feedparser

youtube_dl.utils.std_headers["Cookie"] = ""

intents = discord.Intents.default()
intents.members = True
all_intents = []
if intents.bans:
    all_intents.append("bans = True")
else:
    all_intents.append("bans = False")
if intents.dm_messages:
    all_intents.append("dm_messages = True")
else:
    all_intents.append("dm_messages = False")
if intents.dm_reactions:
    all_intents.append("dm_reactions = True")
else:
    all_intents.append("dm_reactions = False")
if intents.dm_typing:
    all_intents.append("dm_typing = True")
else:
    all_intents.append("dm_typing = False")
if intents.emojis:
    all_intents.append("emojis = True")
else:
    all_intents.append("emojis = False")
if intents.guild_messages:
    all_intents.append("guild_messages = True")
else:
    all_intents.append("guild_messages = False")
if intents.guild_reactions:
    all_intents.append("guild_reactions = True")
else:
    all_intents.append("guild_reactions = False")
if intents.guild_typing:
    all_intents.append("guild_typing = True")
else:
    all_intents.append("guild_typing = False")
if intents.guilds:
    all_intents.append("guilds = True")
else:
    all_intents.append("guilds = False")
if intents.integrations:
    all_intents.append("integrations = True")
else:
    all_intents.append("integrations = False")
if intents.invites:
    all_intents.append("invites = True")
else:
    all_intents.append("invites = False")
if intents.members:
    all_intents.append("members = True")
else:
    all_intents.append("members = False")
if intents.messages:
    all_intents.append("messages = True")
else:
    all_intents.append("messages = False")
if intents.presences:
    all_intents.append("presences = True")
else:
    all_intents.append("presences = False")
if intents.reactions:
    all_intents.append("reactions = True")
else:
    all_intents.append("reactions = False")
if intents.typing:
    all_intents.append("typing = True")
else:
    all_intents.append("typing = False")
if intents.value:
    all_intents.append("value = True")
else:
    all_intents.append("value = False")
if intents.voice_states:
    all_intents.append("voice_states = True")
else:
    all_intents.append("voice_states = False")
if intents.webhooks:
    all_intents.append("webhooks = True")
else:
    all_intents.append("webhooks = False")
print(f"Intents: {all_intents}\n")

client = discord.Client(intents=intents)

verboten = ["arsch", "penis", "fuck"]
katze = ["Katzen haben 4 Füße!", "Katzen sind Tiere!", "Katzen sind lebewesen!"]
fights = ["fight1.gif", "fight2.gif", "fight3.gif", "fight4.gif", "fight5.gif", "fight6.gif", "fight7.gif", "fight8.gif", "fight9.gif"]
status = ["Status 1", "Status 2", "Status 3"]
status2 = [0, 1, 2]
status3 = [discord.Status.online, discord.Status.idle, discord.Status.dnd]
modmail_mods = [542265299387285505]

global banns_channel
global banns_channel_obj
banns_channel = []
banns_channel_obj = []
global gPlaylist
global musik_stopped
global musik_count
global player
global player_repeat
gPlaylist = []
musik_stopped = False
musik_count = 0
player = ""
player_repeat = False

async def playit():
    global gPlaylist
    global musik_stopped
    global musik_count
    global player
    global player_repeat
    try:
        if not player_repeat:
            gPlaylist.pop(0)
        print(gPlaylist)
        player.stop()
        await asyncio.sleep(1)
        sourcex = gPlaylist[0]
        br = mechanize.Browser()
        try:
            br.open(sourcex)
        except:
            pass
        try:
            title = br.title()
        except:
            a = urlparse(sourcex)
            title = os.path.basename(a.path)
        try:
            ydl_opts = {"format": "bestaudio"}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(gPlaylist[0], download=False)
                URL = info["formats"][0]["url"]
        except:
            URL = gPlaylist[0]
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
        client.voice_clients[0].play(source, after=myafter)
        embed = discord.Embed(title="Jetzt spielt:", description=f"[{title}]({sourcex})", color=3566847)
        if not player_repeat:
            player_message = await client.get_channel(829007032895668267).send(embed=embed)
            await player_message.add_reaction("⏏️")
            await player_message.add_reaction("⏹️")
            await player_message.add_reaction("⏯️")
            await player_message.add_reaction("⏭️")
            await player_message.add_reaction("🔁")
    except:
        if not musik_stopped:
            if musik_count > 1:
               embed = discord.Embed(title="Playlist beendet!", color=3566847)
               await client.get_channel(829007032895668267).send(embed=embed)
        else:
            await asyncio.sleep(6)
            musik_stopped = False
        

def myafter(error):
    print(f"M-Error: {error}")
    fut = asyncio.run_coroutine_threadsafe(playit(), client.loop)
    fut.result()

async def auto_unban():
    global banns_channel
    global banns_channel_obj
    while True:
        unix = int(time.time())
        if str(unix) in banns_channel:
            ind = banns_channel.index(str(unix))
            user = banns_channel[ind+1]
            try:
                userx = await client.fetch_user(int(user))
                guild = client.get_guild(785155679295111208)
            except:
                pass
            try:
                await guild.unban(userx, reason="Time up")
            except:
                pass
            try:
                n = discord.utils.get(banns_channel_obj, content=str(unix))
                banns_channnel_obj.remove(n)
            except:
                pass
            try:
                await n.delete()
            except:
                pass
            try:
                banns_channel.remove(str(unix))
            except:
                pass
            try:
                banns_channel.remove(str(user))
            except:
                pass
            try:
                n = discord.utils.get(banns_channel_obj, content=str(user))
                banns_channnel_obj.remove(n)
            except:
                pass
            try:
                await n.delete()
            except:
                pass
        await asyncio.sleep(0.8)

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    msgs2 = cycle(status2)
    msgs3 = cycle(status3)

    while True:
        current_status = next(msgs)
        current_status2 = next(msgs2)
        current_status3 = next(msgs3)
        if current_status == "Status 1":
            await client.change_presence(activity=discord.Game(name=current_status), status=discord.Status.online)
            await asyncio.sleep(10)

        if current_status == "Status 2":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Status 2"), status=discord.Status.idle)
            await asyncio.sleep(10)

        if current_status == "Status 3":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Status 3"), status=discord.Status.dnd)
            await asyncio.sleep(10)

@client.event
async def on_member_join(member):
    await client.get_channel(785155679295111211).send(f"{member.mention} ist dem Server beigetreten!")
    await member.send("Willkommen!")
    rang = discord.utils.get(member.guild.roles, id=825356033601437706)
    await member.add_roles(rang)

@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 826101634315583608:
        guild = payload.guild_id
        guild = client.get_guild(guild)
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == "👍":
            role = guild.get_role(826102077536731146)
            await member.add_roles(role)
        if payload.emoji.id == 826101978408550400:
            role = guild.get_role(826102056737177652)
            await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == 826101634315583608:
        guild = payload.guild_id
        guild = client.get_guild(guild)
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == "👍":
            role = guild.get_role(826102077536731146)
            await member.remove_roles(role)
        if payload.emoji.id == 826101978408550400:
            role = guild.get_role(826102056737177652)
            await member.remove_roles(role)

@client.event
async def on_ready():
    global banns_channel
    global banns_channel_obj
    banns_channel_id = client.get_channel(827198257712070756)
    async for message in banns_channel_id.history(limit=None):
        banns_channel.append(message.content)
    banns_channel_obj = await banns_channel_id.history(limit=None).flatten()
    
    print(f"Bot {client.user.name} ({client.user.id})")
    #await client.change_presence(activity=discord.Game(name="Text, der angezeigt werden soll..."), status=discord.Status.invisible)

@client.event
async def on_message(message):
    global banns_channel
    global banns_channel_obj
    global gPlaylist
    global musik_stopped
    global musik_count
    global player
    global player_repeat
    if message.author == client.user:
        return
    if message.author.bot:
        return

    try:
        embed = discord.Embed(title="Nachricht erstellt!", color=0x00ff2a)
        embed.add_field(name="Ersteller", value=f"{message.author.mention}", inline=False)
        embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
        embed.add_field(name="Inhalt", value=f"{message.content}", inline=False)
        embed.add_field(name="Goto", value=f"[Hier]({message.jump_url})", inline=False)
        await client.get_channel(826834093991657483).send(embed=embed)
    except:
        pass
    
    if type(message.channel) == discord.DMChannel:
        if message.content.startswith("!reply") and message.author.id in modmail_mods:
            name = message.content.replace("!reply ", "")
            namel = name.split()
            id1 = int(namel[0])
            id2 = int(namel[1])
            name = name.replace(namel[0], "")
            name = name.replace(namel[1], "")
            to = await client.fetch_user(id1)
            msg = await to.fetch_message(id2)
            name = name.lstrip()
            await message.author.send(f"Nachricht an {to} verschickt!")
            mmangehängt = message.attachments
            try:
                try:
                    bild1 = mmangehängt[0]
                    bild1 = bild1.url
                    embed = discord.Embed(title="Nachricht von den Mods:", description=f"{name}\n{bild1}")
                except:
                    embed = discord.Embed(title="Nachricht von den Mods:", description=name)
                await msg.reply(embed=embed)
            except:
                await message.author.send("Nicht möglich!")
            return

        embed = discord.Embed(title="Danke für deine Nachricht!")
        try:
            await message.channel.send(embed=embed)
        except:
            return
        mmangehängt = message.attachments
        try:
            bild1 = mmangehängt[0]
            bild1 = bild1.url
            mod1 = await client.fetch_user(542265299387285505)
            embed = discord.Embed(title="Neue ModMail Anfrage", description=f"{message.content}\n{bild1}")
            embed.add_field(name=f"by {message.author} ({message.author.id})", value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
        except:
            mod1 = await client.fetch_user(542265299387285505)
            embed = discord.Embed(title="Neue ModMail Anfrage", description=f"{message.content}")
            embed.add_field(name=f"by {message.author} ({message.author.id})", value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
        return

    if not discord.utils.get(message.author.roles, id=826120825350520863) is None:
        await message.delete()
        m = await message.channel.send("Du bist gemutet!")
        await asyncio.sleep(3)
        await m.delete()

    content_raw = message.content.lower()
    for word in verboten:
        if word in content_raw:
            await message.delete()
            msg = await message.channel.send(f"Hey, das Wort {word} ist nicht erlaubt!")
            await asyncio.sleep(5)
            await msg.delete()

    if "discord.gg" in message.content:
        await message.delete()
        msg = await message.channel.send(f"Hey, Einladungen sind nicht erlaubt!")
        await asyncio.sleep(5)
        await msg.delete()

    if message.content.startswith("!kick"):
        pass

    if message.content.startswith("!ban"):
        if not discord.utils.get(message.author.roles, id=825356069789892610) is None:
            if message.content == "!ban":
                embed = discord.Embed(title="Syntax: !ban USERID LÄNGE GRUND", color=0x00ff74)
                await message.channel.send(embed=embed)
            else:
                name = message.content.replace("!ban ", "")
                names = name.split()
                name4 = names[0]
                lange = langel = names[1]
                names.remove(lange)
                names.remove(name4)
                name3 = ""
                namerun = 0
                for i in names:
                    namerun += 1
                    if namerun == 1:
                        name3 = i
                    else:
                        name3 = f"{name3} {i}"
                langel = langel.replace("d", "")
                langel = langel.replace("h", "")
                langel = langel.replace("m", "")
                langel = langel.replace("s", "")
                langel = langel.replace("y", "")
                if "s" in lange and not lange == "perm":
                    try:
                        lange = int(lange.replace("s", ""))
                        langel = langel + " " + "second(s)!"
                    except:
                        await message.reply("Ungültige Länge!")
                        return
                elif "m" in lange and not lange == "perm":
                    try:
                        lange = int(lange.replace("m", ""))
                        lange = lange * 60
                        langel = langel + " " + "minute(s)!"
                    except:
                        await message.reply("Ungültige Länge!")
                        return
                elif "h" in lange and not lange == "perm":
                    try:
                        lange = int(lange.replace("h", ""))
                        lange = lange * 60 * 60
                        langel = langel + " " + "hour(s)!"
                    except:
                        await message.reply("Ungültige Länge!")
                        return
                elif "d" in lange and not lange == "perm":
                    try:
                        lange = int(lange.replace("d", ""))
                        lange = lange * 60 * 60 * 24
                        langel = langel + " " + "day(s)!"
                    except:
                        await message.reply("Ungültige Länge!")
                        return
                elif "y" in lange and not lange == "perm":
                    try:
                        lange = int(lange.replace("y", ""))
                        lange = lange * 60 * 60 * 24 * 365
                        langel = langel + " " + "year(s)!"
                    except:
                        await message.reply("Ungültige Länge!")
                        return
                elif lange == "perm":
                    lange = 9999999999999
                    langel = "PERMANENT"

                else:
                    await message.reply("Ungültige Länge!")
                unix = int(time.time())
                try:
                    endzeit = unix + lange
                except:
                    await message.reply("Ungültige Länge!")
                try:
                    name4 = int(name4)
                except:
                    await message.reply("Ungültige ID")
                try:
                    name2 = await client.fetch_user(name4)
                except:
                    await message.reply("Nicht gefunden!")
                if name3 == "":
                    await message.reply("Bitte gebe einen Grund ein!")
                try:
                    embed = discord.Embed(title="Du wurdest gebannt!", color=0xff0000)
                    embed.add_field(name="Grund:", value=name3, inline=False)
                    embed.add_field(name="Länge", value=langel, inline=False)
                    await name2.send(embed=embed)
                except:
                    await message.reply("DMs sind deaktiviert!")
                try:
                    await message.guild.unban(name2, reason=name3)
                except:
                    pass
                await message.guild.ban(name2, reason=name3 + " | " + langel)
                try:
                    n = discord.utils.get(banns_channel_obj, content=str(name2.id))
                    banns_channel_obj.remove(n)
                except:
                    pass
                try:
                    await n.delete()
                except:
                    pass
                if not langel == "PERMANENT":
                    n2 = await client.get_channel(827198257712070756).send(name2.id)
                    n1 = await client.get_channel(827198257712070756).send(endzeit)
                    banns_channel.append(str(endzeit))
                    banns_channel.append(str(name2.id))
                    banns_channel_obj.append(n1)
                    banns_channel_obj.append(n2)

    if message.content.startswith("!unban"):
        nachricht = message.content.replace("!unban ", "")
        nachrichtl = nachricht.split()
        userid = nachrichtl[0]
        user = await client.fetch_user(int(userid))
        await message.guild.unban(user)

    if message.content.startswith("!move"):
        if not discord.utils.get(message.author.roles, id=825356069789892610) is None:
            msg = message.content.replace("!move ", "")
            msgl = msg.split()
            if len(msgl) > 2:
                embed = discord.Embed(title="Zu viele Argumente!")
                await message.channel.send(embed=embed)
                return
            msg1 = msgl[0]
            msg2 = msgl[1]
            try:
                movemsg = await message.channel.fetch_message(int(msg1))
            except:
                embed = discord.Embed(title="Nicht gefunden!")
                await message.channel.send(embed=embed)
                return
            msg2 = msg2.replace(">", "")
            msg2 = msg2.replace("<", "")
            msg2 = msg2.replace("#", "")
            try:
                channel = client.get_channel(int(msg2))
            except:
                embed = discord.Embed(title="Kanal nicht gefunden!")
                await message.channel.send(embed=embed)
                return
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                if webhook.name == "Move":
                    break
            try:
                webhook = webhook
            except:
                embed = discord.Embed(title="Webhook nicht gefunden!")
                await message.channel.send(embed=embed)
                return
            try:
                await webhook.send(movemsg.content, username=movemsg.author.name, avatar_url=movemsg.author.avatar_url, embed=movemsg.embeds[0], file=movemsg.attachments[0])
            except:
                try:
                    await webhook.send(movemsg.content, username=movemsg.author.name, avatar_url=movemsg.author.avatar_url, embed=movemsg.embeds[0])
                except:
                    try:
                        await webhook.send(movemsg.content, username=movemsg.author.name, avatar_url=movemsg.author.avatar_url, file=movemsg.attachments[0])
                    except:
                        await webhook.send(movemsg.content, username=movemsg.author.name, avatar_url=movemsg.author.avatar_url)
            await message.delete()
            await movemsg.delete()

    if message.content.startswith("!syncwebhook"):
        if not discord.utils.get(message.author.roles, id=825356069789892610) is None:
            guild = message.guild
            c = []
            for channel in guild.channels:
                await message.channel.trigger_typing()
                if type(channel) == discord.channel.VoiceChannel:
                    continue
                if type(channel) == discord.channel.CategoryChannel:
                    continue
                for webhook in await channel.webhooks():
                    c.append(webhook.name)
                if not "Move" in c:
                    await channel.create_webhook(name="Move", reason="WebHook sync")
                c = []
                await asyncio.sleep(3)
            embed = discord.Embed(title="Fertig!")
            await message.channel.send(embed=embed)
    
    if message.content.startswith("!hallo"):
        await message.reply("Auch hallo!")

    if message.content.startswith("!test"):
        if not discord.utils.get(message.author.roles, id=825356069789892610) is None:
            await message.reply("Das ist nur ein Test!")

    if message.content.startswith("!mute"):
        selector = message.mentions[0]
        role = discord.utils.get(message.guild.roles, id=826120825350520863)
        await member.add_roles(role)

    if message.content.startswith("!unmute"):
        selector = message.mentions[0]
        role = discord.utils.get(message.guild.roles, id=826120825350520863)
        await member.remove_roles(role)

    if message.content.startswith("!embed"):
        embed = discord.Embed(title="Ein Embed!", description="ist doch deutlich schöner!", color=0x4b49d8)
        embed.set_footer(text="Footer!")
        embed.set_image(url="https://i.stack.imgur.com/zeJPU.png")
        embed.set_thumbnail(url="https://images.idgesg.net/images/article/2017/07/random-vladimer_shioshvili-100729292-large.jpg")
        embed.set_author(name="Hallo Welt!")
        embed.add_field(name="Feld 1", value="Wert 1", inline=False)
        embed.add_field(name="Feld 2", value="Wert 2", inline=False)
        await message.channel.send(embed=embed)
 
    if message.content.startswith("!clear"):
        if not discord.utils.get(message.author.roles, id=825356069789892610) is None:
            anzahl = message.content.replace("!clear ", "")
            try:
                del_msgs = await message.channel.purge(limit=int(anzahl)+1)
                embed = discord.Embed(title=f"{len(del_msgs)-1} Nachrichten wurden gelöscht!", color=0x9b9ae5)
                msg = await message.channel.send(embed=embed)
                await asyncio.sleep(3)
                await msg.delete()
            except:
                embed = discord.Embed(title="Ungültige Zahl!", color=0xf30c01)
                msg = await message.channel.send(embed=embed)
                await asyncio.sleep(3)
                await msg.delete()
        else:
            await message.channel.send("Keine Rechte!")

    if message.content.startswith("!katze"):
        antwort = random.choice(katze)
        msg = await message.channel.send(antwort)
        await msg.add_reaction("😆") 

    if message.content.startswith("!fight"):
        selected = random.choice(fights)
        try:
            selector = message.mentions[0]
        except:
            await message.channel.send("Bitte erwähne jemanden!")
            return
        await message.channel.send(f"{message.author.name} kämpft gegen {selector.name}.", file=discord.File(selected, filename="fight.gif"))

    if message.content.startswith("!me"):
        try:
            m = message.mentions[0]
            embed = discord.Embed(title=m.name, color=0x00ffe0)
            embed.add_field(name="Beigetreten am", value=m.joined_at, inline=False)
            embed.add_field(name="Account erstellt am", value=m.created_at, inline=False)
            embed.add_field(name="Name#tag", value=m, inline=False)
            embed.add_field(name="ID", value=m.id, inline=False)
            embed.add_field(name="Nick", value=m.nick, inline=False)
            embed.add_field(name="Höchster Rang", value=m.top_role, inline=False)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title=message.author.name, color=0x00ffe0)
            embed.add_field(name="Beigetreten am", value=message.author.joined_at, inline=False)
            embed.add_field(name="Account erstellt am", value=message.author.created_at, inline=False)
            embed.add_field(name="Name#tag", value=message.author, inline=False)
            embed.add_field(name="ID", value=message.author.id, inline=False)
            embed.add_field(name="Nick", value=message.author.nick, inline=False)
            embed.add_field(name="Höchster Rang", value=message.author.top_role, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("!webhook"):
        nachricht = message.content.replace("!webhook ", "")
        nachrichtl = nachricht.split()
        url = nachrichtl[0]
        nachrichtl.remove(url)
        text = nachricht.replace(url, "")
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(session))
            await webhook.send(text, username=message.author.name)

    if message.content.startswith("!xwebhook"):
        nachricht = message.content.replace("!xwebhook ", "")
        for webhook in await message.channel.webhooks():
            if webhook.name == "WH":
                await webhook.send(nachricht, username=message.author.name)

    if message.content.startswith("!giveaway start"):
        if message.content == "!giveaway start":
            embed = discord.Embed(title="Syntax: !giveaway start [Item zum verlosen]", color=3566847)
            await message.channel.send(embed=embed)
        else:
            name1 = message.content
            giveawayrang = discord.utils.get(message.guild.roles, id=827558021785714738)
            name1 = name1.replace("!giveaway start ", "")
            embed = discord.Embed(title="Giveaway", description=name1, color=3566847)
            embed.add_field(name="Gestartet von", value=message.author.mention, inline=False)
            embed.add_field(name="Reagiere mit <:verify:826101978408550400>, um teilzunehmen!", value="__________", inline=False)
            wdl = await message.guild.get_channel(828639579745288223).send(embed=embed)
            await wdl.edit(content=giveawayrang.mention)
            await wdl.add_reaction(":verify:826101978408550400")
            embed = discord.Embed(title=f"Du hast das Giveaway von **{name1}** erfolgreich gestartet!", color=3566847)
            await message.channel.send(embed=embed)

    if message.content.startswith("!giveaway del"):
        if message.content == "!giveaway del":
            embed = discord.Embed(title="Syntax: !giveaway del [ID der Giveawaynachricht]", color=3566847)
            await message.channel.send(embed=embed)
        else:
            name1 = message.content.replace("!giveaway del ", "")
            chl = client.get_channel(828639579745288223)
            try:
                nachricht = await chl.fetch_message(name1)
            except:
                embed = discord.Embed(title="Nicht gefunden!", color=16711680)
                await message.channel.send(embed=embed)
                return
            if str(message.author.id) in str(nachricht.embeds[0].fields) or not discord.utils.get(message.author.roles, id=825356069789892610) is None:
                await nachricht.delete()
                embed = discord.Embed(title="Giveaway gelöscht!", color=3566847)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="Dies ist nicht dein Giveaway!", color=16711680)
                await message.channel.send(embed=embed)

    if message.content.startswith("!giveaway stop"):
        if message.content == "!giveaway stop":
            embed = discord.Embed(title="Syntax: !giveaway stop [ID der Giveawaynachricht] [Anzahl der Gewinner]", color=3566847)
            await message.channel.send(embed=embed)
        else:
            gesendet = message.content.split()
            try:
                name1 = gesendet[2]
            except:
                embed = discord.Embed(title="Ungültige ID!", color=16711680)
                await message.channel.send(embed=embed)
                return
            try:
                name2 = int(gesendet[3])
            except:
                embed = discord.Embed(title="Anzahl der Gewinner fehlt!", color=16711680)
                await message.channel.send(embed=embed)
                return
            chl = client.get_channel(828639579745288223)
            try:
                nachricht = await chl.fetch_message(name1)
                vitem = nachricht.embeds[0].description
            except:
                embed = discord.Embed(title="Nicht gefunden!", color=16711680)
                await message.channel.send(embed=embed)
                return
            if "Giveaway beendet!" in nachricht.content:
                embed = discord.Embed(title="Das Giveaway wurde bereits beendet!", color=16711680)
                await message.channel.send(embed=embed)
                return
            if str(message.author.id) in str(nachricht.embeds[0].fields) or not discord.utils.get(message.author.roles, id=825356069789892610) is None:
                reactors = []
                for reaction in nachricht.reactions:
                    async for user in reaction.users():
                        reactors.append(user)
                    alle_liste = []
                    for member in reactors:
                        alle_liste.append(int(member.id))
                alle_liste.remove(825377881546686474)
                alle_member_server = []
                for i in message.guild.members:
                    alle_member_server.append(i.id)
                for i in alle_liste:
                    if not i in alle_member_server:
                        alle_liste.remove(i)
                try:
                    alle_gewinner = []
                    alle_gewinnerx = ""
                    if name2 > 1:
                        for i in range(name2):
                            gewinner = random.choice(alle_liste)
                            alle_liste.remove(gewinner)
                            alle_gewinner.append(gewinner)
                            if i == 0:
                                gewinnerx = client.get_user(gewinner).name
                                alle_gewinnerx = gewinnerx
                            else:
                                gewinnerx = client.get_user(gewinner).name
                                alle_gewinnerx = alle_gewinnerx + ", " + gewinnerx
                        for i in alle_gewinner:
                            erwähnung = client.get_user(i)
                            await client.get_channel(828639579745288223).send(f"**Giveaway beendet!**\n{erwähnung.mention} hat **{vitem}** gewonnen!\n{nachricht.jump_url}")
                    else:
                        alle_gewinner = random.choice(alle_liste)
                        alle_gewinnerx = gewinnerx = client.get_user(alle_gewinner).name
                        erwähnung = client.get_user(alle_gewinner)
                        await client.get_channel(828639579745288223).send(f"**Giveaway beendet!**\n{erwähnung.mention} hat **{vitem}** gewonnen!\n{nachricht.jump_url}")
                    embed = discord.Embed(title=f"Du hast das Giveaway von **{vitem}** erfolgreich beendet!", color=3566847)
                    await message.channel.send(embed=embed)
                    await nachricht.edit(content=f"**Giveaway beendet!**\nGewinner: **{alle_gewinnerx}**")
                except:
                    embed = discord.Embed(title="Auslosung nicht möglich. Noch nicht genug Teilnehmer!", color=16711680)
                    await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="Dies ist nicht dein Giveaway!", color=16711680)
                await message.channel.send(embed=embed)

    if message.content.startswith("!giveaway reroll"):
        if message.content == "!giveaway reroll":
            embed = discord.Embed(title="Syntax: !giveaway reroll [ID der Giveawaynachricht] [ID des zu ersetzenden Gewinners]", color=3566847)
            await message.channel.send(embed=embed)
        else:
            gesendet = message.content.split()
            try:
                name1 = gesendet[2]
            except:
                embed = discord.Embed(title="Ungültige ID!", color=16711680)
                await message.channel.send(embed=embed)
                return
            try:
                name2 = int(gesendet[3])
            except:
                embed = discord.Embed(title="Anzahl der Gewinner fehlt!", color=16711680)
                await message.channel.send(embed=embed)
                return
            chl = client.get_channel(828639579745288223)
            try:
                nachricht = await chl.fetch_message(name1)
                vitem = nachricht.embeds[0].description
            except:
                embed = discord.Embed(title="Nicht gefunden!", color=16711680)
                await message.channel.send(embed=embed)
                return
            print(nachricht.content)
            if not "Giveaway beendet!" in nachricht.content:
                embed = discord.Embed(title="Das Giveaway wurde noch nicht beendet!", color=16711680)
                await message.channel.send(embed=embed)
                return
            if str(message.author.id) in str(nachricht.embeds[0].fields) or not discord.utils.get(message.author.roles, id=825356069789892610) is None:
                vorher_gewinner = nachricht.content.replace("**Giveaway beendet!**", "")
                vorher_gewinner = vorher_gewinner.replace("\n", "")
                vorher_gewinner = vorher_gewinner.replace("Gewinner: ", "")
                vorher_gewinner = vorher_gewinner.replace("*", "")
                vorher_gewinner = vorher_gewinner.lstrip()
                vorher_gewinner = vorher_gewinner.split(", ")
                gewinner2 = []
                for member in message.guild.members:
                    if member.name in vorher_gewinner:
                        gewinner2.append(member.id)
                if not int(name2) in gewinner2:
                    embed = discord.Embed(title="Dieser User hat nicht gewonnen!", color=16711680)
                    await message.channel.send(embed=embed)
                    return
                gewinner1 = deepcopy(gewinner2)
                gewinner2.remove(int(name2))
                neue_gewinner = ""
                ti = 0
                for i in gewinner2:
                    if ti == 0:
                        neue_gewinner = client.get_user(i).name
                    else:
                        neue_gewinner = neue_gewinner + ", " + client.get_user(i).name
                    ti += 1
                reactors = []
                for reaction in nachricht.reactions:
                    async for user in reaction.users():
                        reactors.append(user)
                    alle_liste = []
                    for member in reactors:
                        alle_liste.append(int(member.id))
                alle_liste.remove(825377881546686474)
                alle_liste.remove(int(name2))
                for i in gewinner1:
                    try:
                        alle_liste.remove(i)
                    except:
                        pass
                if alle_liste == []:
                    embed = discord.Embed(title="Keine weiteren Teilnehmner!", color=16711680)
                    await message.channel.send(embed=embed)
                    return
                gewinner = random.choice(alle_liste)
                gewinnerx = client.get_user(gewinner).name
                erwähnung = client.get_user(gewinner)
                if neue_gewinner == "":
                    texta = gewinnerx + "**"
                    einzeln = True
                else:
                    texta = neue_gewinner + ", " + gewinnerx + "**"
                    einzeln = False
                if einzeln:
                    await client.get_channel(828639579745288223).send(f"**Giveaway beendet!**\nNeuer Gewinner: {erwähnung.mention} hat **{vitem}** gewonnen!")
                if not einzeln:
                    await client.get_channel(828639579745288223).send(f"**Giveaway beendet!**\nNeuer Gewinner: {erwähnung.mention} hat **{vitem}** gewonnen!")
                embed = discord.Embed(title=f"Du hast beim Giveaway von **{vitem}** einen neuen Gewinner bestimmt!")
                await message.channel.send(embed=embed)
                await nachricht.edit(content=f"**Giveaway beendet!**\nGewinner: **{texta}")
            else:
                embed = discord.Embed(title="Dies ist nicht dein Giveaway!", color=16711680)
                await message.channel.send(embed=embed)

    if message.content.startswith("!team"):
        members = message.guild.members
        await asyncio.sleep(0.5)
        rang_rot = discord.utils.get(message.guild.roles, id=846401421732610098)
        rang_blau = discord.utils.get(message.guild.roles, id=846401511936360460)
        for member in members:
            await asyncio.sleep(0.5)
            if member.bot:
                members.remove(member)
        for member in members:
            await member.remove_roles(rang_rot)
            await member.remove_roles(rang_blau)

        team_rot = []
        team_blau = []
        while not members == []:
            member = random.choice(members)
            team_rot.append(member)
            members.remove(member)

            member = random.choice(members)
            team_blau.append(member)
            members.remove(member)

            for member in team_rot:
                await member.add_roles(rang_rot)

            for member in team_blau:
                await member.add_roles(rang_blau)

            print(team_rot)
            print(team_blau)

    if message.content.startswith("!musik"):
        if message.channel.id == 829007032895668267:
            await message.channel.trigger_typing()
            await asyncio.sleep(0.05)
            embed = discord.Embed(title="Musik - Commands", color=3566847)
            embed.add_field(name="!play URL", value="Spiele den Song bei der URL", inline=False)
            embed.add_field(name="!playlist", value="Listet die Playlist", inline=False)
            embed.add_field(name="!playlist add URL", value="Fügt die URL der Playlist hinzu", inline=False)
            embed.add_field(name="!playlist add URL1, URL2", value="Fügt die URLs der Playlist hinzu", inline=False)
            embed.add_field(name="!playlist remove URL", value="Löscht die URL aus der Playlist", inline=False)
            embed.add_field(name="!playlist clear", value="Leert die Playlist", inline=False)
            embed.add_field(name="!play playlist", value="Spielt die Playlist ab", inline=False)
            embed.add_field(name="!join", value="Bot joint deinem Voice-Channel", inline=False)
            embed.add_field(name="!leave", value="Bot verlässt seinen Voice-Channel", inline=False)
            embed.add_field(name="!pause", value="Pausiert den Song", inline=False)
            embed.add_field(name="!resume", value="Setzt den Song fort", inline=False)
            embed.add_field(name="!stop", value="Stoppt alle Songs und leert die Playlist", inline=False)
            embed.add_field(name="!skip", value="Überspringt den Song", inline=False)
            embed.add_field(name="!repeat", value="Wiederholt den Song in Dauerschleife", inline=False)
            embed.add_field(name="!reactions", value="Erklärt die Reactions", inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("!reactions"):
        if message.channel.id == 829007032895668267:
            await message.channel.trigger_typing()
            await asyncio.sleep(0.05)
            embed = discord.Embed(title="Musik - Reactions", color=3566847)
            embed.add_field(name=":play_pause:", value="Pausiert den Song oder setzt ihn fort", inline=False)
            embed.add_field(name=":track_next:", value="Überspringt den Song", inline=False)
            embed.add_field(name=":stop_button:", value="Stoppt alle Songs und leert die Playlist", inline=False)
            embed.add_field(name=":eject:", value="Bot verlässt seinen Voice-Channel", inline=False)
            embed.add_field(name=":arrow_forward:", value="Spielt die Playlist ab", inline=False)
            embed.add_field(name=":repeat:", value="Wiederholt den Song in Dauerschleife", inline=False)
            embed.add_field(name=":recycle:", value="Leert die Playlist", inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("!join"):
        if message.channel.id == 829007032895668267:
            try:
                channel = message.author.voice.channel
            except:
                embed = discord.Embed(title="Du bist in keinem Voice-Channel!", color=16711680)
                await message.channel.send(embed=embed)
                return
            voice = discord.utils.get(client.voice_clients, guild=message.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            embed = discord.Embed(title=f"Channel {channel} beigetreten!")
            await message.channel.send(embed=embed)

    if message.content.startswith("!leave"):
        if message.channel.id == 829007032895668267:
            musik_stopped = True
            gPlaylist.clear()
            voice = discord.utils.get(client.voice_clients, guild=message.guild)
            if voice and voice.is_connected():
                await voice.disconnect()
                embed = discord.Embed(title=f"Channel {voice.channel.name} verlassen!")
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="Ich bin in keinem Voice-Channel!", color=16711680)
                await message.channel.send(embed=embed)

    if message.content.startswith("!play") and not message.content.startswith("!playlist") and not message.content == "!play playlist":
        if message.channel.id == 829007032895668267:
            player_repeat = False
            await message.channel.trigger_typing()
            musik_count = 1
            gPlaylist.clear()
            source = message.content.replace("!play ", "")
            br = mechanize.Browser()
            try:
                br.open(source)
            except:
                videossearch = VideosSearch(source, limit=5)
                result = videossearch.result()
                desc = ""
                count = 0
                p_list = []
                for res in result["result"]:
                    p_list.append(res["link"])
                    count += 1
                    desc = desc + f"{count}. [{res['title']}]({res['link']})\n"
                embed = discord.Embed(title="Auf YouTube suchen:", description=desc)
                x = await message.channel.send(embed=embed)
                await x.add_reaction("1️⃣")
                await x.add_reaction("2️⃣")
                await x.add_reaction("3️⃣")
                await x.add_reaction("4️⃣")
                await x.add_reaction("5️⃣")
                def checkmsg(m):
                    return m.channel == message.channel
                def checkreaction(reaction, user):
                    return reaction.message.channel == message.channel and not user.id == 825377881546686474
                pending_tasks = [client.wait_for("reaction_add", check=checkreaction),
                                 client.wait_for("message", check=checkmsg)]
                done_tasks, pending_tasks = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
                try:
                    for task in done_tasks:
                        reaction, user = await task
                except:
                    for task in done_tasks:
                        msg2 = await task
                try:
                    if msg2.content == "1":
                        source = p_list[0]
                    elif msg2.content == "2":
                        source = p_list[1]
                    elif msg2.content == "3":
                        source = p_list[2]
                    elif msg2.content == "4":
                        source = p_list[3]
                    elif msg2.content == "5":
                        source = p_list[4]
                    else:
                        await x.delete()
                        return
                except:
                    if reaction.emoji == "1️⃣":
                        source = p_list[0]
                    elif reaction.emoji == "2️⃣":
                        source = p_list[1]
                    elif reaction.emoji == "3️⃣":
                        source = p_list[2]
                    elif reaction.emoji == "4️⃣":
                        source = p_list[3]
                    elif reaction.emoji == "5️⃣":
                        source = p_list[4]
                    else:
                        await x.delete()
                        return
                br.open(source)
            try:
                title = br.title()
                if title == "- YouTube":
                    embed = discord.Embed(title="YouTube Video nicht gefunden!", color=16711680)
                    await message.channel.send(embed=embed)
                    return
            except:
                a = urlparse(source)
                title = os.path.basename(a.path)
            try:
                channel = message.author.voice.channel
            except:
                embed = discord.Embed(title="Du bist in keinem Voice-Channel!", color=16711680)
                await message.channel.send(embed=embed)
                return
            try:
                ydl_opts = {"format": "bestaudio"}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(source, download=False)
                    URL = info["formats"][0]["url"]
            except:
                URL = source
            gPlaylist.append(source)
            player = discord.utils.get(client.voice_clients, guild=message.guild)
            if player and player.is_connected():
                await player.move_to(channel)
            else:
                player = await channel.connect()
            try:
                pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
                player.play(pplayer, after=myafter)
            except:
                player.stop()
                pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
                player.play(pplayer, after=myafter)
            embed = discord.Embed(title="Jetzt spielt:", description=f"[{title}]({source})")
            player_message = await message.channel.send(embed=embed)
            await player_message.add_reaction("⏏️")
            await player_message.add_reaction("⏹️")
            await player_message.add_reaction("⏯️")
            await player_message.add_reaction("⏭️")
            await player_message.add_reaction("🔁")

    if message.content.startswith("!pause"):
        if message.channel.id == 829007032895668267:
            try:
                player.pause()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Pausiert!")
            await message.channel.send(embed=embed)

    if message.content.startswith("!resume"):
        if message.channel.id == 829007032895668267:
            try:
                player.resume()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Fortgesetzt!")
            await message.channel.send(embed=embed)

    if message.content.startswith("!repeat"):
        if message.channel.id == 829007032895668267:
            if player_repeat:
                player_repeat = False
                embed = discord.Embed(title="Wiederholung nicht mehr aktiv!")
                await message.channel.send(embed=embed)
            else:
                player_repeat = True
                embed = discord.Embed(title="Wiederholung aktiv!")
                await message.channel.send(embed=embed)

    if message.content.startswith("!stop"):
        if message.channel.id == 829007032895668267:
            musik_stopped = True
            gPlaylist.clear()
            try:
                player.stop()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Beendet!")
            await message.channel.send(embed=embed)

    if message.content == "!play playlist" or message.content == "!playlist play":
        if message.channel.id == 829007032895668267:
            if not gPlaylist == []:
                player_repeat = False
                await message.channel.trigger_typing()
                musik_count = 2
                try:
                    channel = message.author.voice.channel
                except:
                    embed = discord.Embed(title="Du bist in keinem Voice-Channel!", color=16711680)
                    await message.channel.send(embed=embed)
                    return
                player = discord.utils.get(client.voice_clients, guild=message.guild)
                if player and player.is_connected():
                    await player.move_to(channel)
                else:
                    player = await channel.connect()
                player.stop()
                await asyncio.sleep(1)
                sourcex = gPlaylist[0]
                br = mechanize.Browser()
                try:
                    br.open(sourcex)
                except:
                    pass
                try:
                    title = br.title()
                except:
                    a = urlparse(sourcex)
                    title = os.path.basename(a.path)
                try:
                    ydl_opts = {"format": "bestaudio"}
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(sourcex, download=False)
                        URL = info["formats"][0]["url"]
                except:
                    URL = gPlaylist[0]
                try:
                    pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
                    player.play(pplayer, after=myafter)
                except:
                    player.stop()
                    pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
                    player.play(pplayer, after=myafter)
                embed = discord.Embed(title=f"Jetzt spielt:", description=f"[{title}]({sourcex})")
                player_message = await message.channel.send(embed=embed)
                await player_message.add_reaction("⏏️")
                await player_message.add_reaction("⏹️")
                await player_message.add_reaction("⏯️")
                await player_message.add_reaction("⏭️")
                await player_message.add_reaction("🔁")
            else:
                embed = discord.Embed(title="Die Playlist ist leer!", color=16711680)
                await message.channel.send(embed=embed)
                return

    if message.content.startswith("!playlist add"):
        if message.channel.id == 829007032895668267:
            source = message.content.replace("!playlist add ", "")
            sl = source.split()
            if sl[0] == "random":
                source = source.replace("random ", "")
                setrandom = True
            sourcel = source.split(",")
            try:
                setrandom = setrandom
            except:
                setrandom = False
            if source.startswith("https://www.youtube.com/playlist?"):
                playlist_id = source.replace("https://www.youtube.com/playlist?list=", "")
                feed = feedparser.parse(f"https://www.youtube.com/feeds/videos.xml?playlist_id={playlist_id}")
                entries = feed.entries
                if setrandom:
                    random.shuffle(entries)
                hinzu = ""
                c = 0
                for entry in entries:
                    c += 1
                    if c % 2 == 0:
                        await message.channel.trigger_typing()
                    await asyncio.sleep(0.1)
                    i = entry["link"]
                    musik_count += 1
                    i = i.lstrip()
                    br = mechanize.Browser()
                    try:
                        br.open(i)
                    except:
                        pass
                    try:
                        title = br.title()
                        if title == "- YouTube":
                            embed = discord.Embed(title="YouTube Video nicht gefunden!", color=16711680)
                            await message.channel.send(embed=embed)
                            return
                    except:
                        a = urlparse(source)
                        title = os.path.basename(a.path)
                    gPlaylist.append(i)
                    hinzu = f"{hinzu}- [{title}]({i})\n"
                if setrandom:
                    embed = discord.Embed(title="Zur Playlist hinzugefügt: (random)", description=hinzu)
                else:
                    embed = discord.Embed(title="Zur Playlist hinzugefügt:", description=hinzu)
                m = await message.channel.send(embed=embed)
                await m.add_reaction("▶️")
                return
            if len(sourcel) > 1:
                hinzu = ""
                if setrandom:
                    random.shuffle(sourcel)
                for i in sourcel:
                    musik_count += 1
                    i = i.lstrip()
                    br = mechanize.Browser()
                    try:
                        br.open(i)
                    except:
                        videossearch = VideosSearch(i, limit=5)
                        result = videossearch.result()
                        desc = ""
                        count = 0
                        p_list = []
                        for res in result["result"]:
                            p_list.append(res["link"])
                            count += 1
                            desc = desc + f"{count}. [{res['title']}]({res['link']})\n"
                        embed = discord.Embed(title="Auf YouTube suchen:", description=desc)
                        x = await message.channel.send(embed=embed)
                        await x.add_reaction("1️⃣")
                        await x.add_reaction("2️⃣")
                        await x.add_reaction("3️⃣")
                        await x.add_reaction("4️⃣")
                        await x.add_reaction("5️⃣")
                        def checkmsg(m):
                            return m.channel == message.channel
                        def checkreaction(reaction, user):
                            return reaction.message.channel == message.channel and not user.id == 825377881546686474
                        pending_tasks = [client.wait_for("reaction_add", check=checkreaction),
                                         client.wait_for("message", check=checkmsg)]
                        done_tasks, pending_tasks = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
                        try:
                            for task in done_tasks:
                                reaction, user = await task
                        except:
                            for task in done_tasks:
                                msg2 = await task
                        try:
                            if msg2.content == "1":
                                i = p_list[0]
                            elif msg2.content == "2":
                                i = p_list[1]
                            elif msg2.content == "3":
                                i = p_list[2]
                            elif msg2.content == "4":
                                i = p_list[3]
                            elif msg2.content == "5":
                                i = p_list[4]
                            else:
                                await x.delete()
                                return
                        except:
                            if reaction.emoji == "1️⃣":
                                i = p_list[0]
                            elif reaction.emoji == "2️⃣":
                                i = p_list[1]
                            elif reaction.emoji == "3️⃣":
                                i = p_list[2]
                            elif reaction.emoji == "4️⃣":
                                i = p_list[3]
                            elif reaction.emoji == "5️⃣":
                                i = p_list[4]
                            else:
                                await x.delete()
                                return
                        br.open(i)
                    try:
                        title = br.title()
                        if title == "- YouTube":
                            embed = discord.Embed(title="YouTube Video nicht gefunden!", color=16711680)
                            await message.channel.send(embed=embed)
                            return
                    except:
                        a = urlparse(source)
                        title = os.path.basename(a.path)
                    gPlaylist.append(i)
                    hinzu = f"{hinzu}- [{title}]({i})\n"
                if setrandom:
                    embed = discord.Embed(title="Zur Playlist hinzugefügt: (random)", description=hinzu)
                else:
                    embed = discord.Embed(title="Zur Playlist hinzugefügt:", description=hinzu)
                player_message = await message.channel.send(embed=embed)
                await player_message.add_reaction("▶️")
                return
            musik_count += 1
            br = mechanize.Browser()
            try:
                br.open(source)
            except:
                videossearch = VideosSearch(source, limit=5)
                result = videossearch.result()
                desc = ""
                count = 0
                p_list = []
                for res in result["result"]:
                    p_list.append(res["link"])
                    count += 1
                    desc = desc + f"{count}. [{res['title']}]({res['link']})\n"
                embed = discord.Embed(title="Auf YouTube suchen:", description=desc)
                x = await message.channel.send(embed=embed)
                await x.add_reaction("1️⃣")
                await x.add_reaction("2️⃣")
                await x.add_reaction("3️⃣")
                await x.add_reaction("4️⃣")
                await x.add_reaction("5️⃣")
                def checkmsg(m):
                    return m.channel == message.channel
                def checkreaction(reaction, user):
                    return reaction.message.channel == message.channel and not user.id == 825377881546686474
                pending_tasks = [client.wait_for("reaction_add", check=checkreaction),
                                 client.wait_for("message", check=checkmsg)]
                done_tasks, pending_tasks = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
                try:
                    for task in done_tasks:
                        reaction, user = await task
                except:
                    for task in done_tasks:
                        msg2 = await task
                try:
                    if msg2.content == "1":
                        source = p_list[0]
                    elif msg2.content == "2":
                        source = p_list[1]
                    elif msg2.content == "3":
                        source = p_list[2]
                    elif msg2.content == "4":
                        source = p_list[3]
                    elif msg2.content == "5":
                        source = p_list[4]
                    else:
                        await x.delete()
                        return
                except:
                    if reaction.emoji == "1️⃣":
                        source = p_list[0]
                    elif reaction.emoji == "2️⃣":
                        source = p_list[1]
                    elif reaction.emoji == "3️⃣":
                        source = p_list[2]
                    elif reaction.emoji == "4️⃣":
                        source = p_list[3]
                    elif reaction.emoji == "5️⃣":
                        source = p_list[4]
                    else:
                        await x.delete()
                        return
            try:
                title = br.title()
                if title == "- YouTube":
                    embed = discord.Embed(title="YouTube Video nicht gefunden!", color=16711680)
                    await message.channel.send(embed=embed)
                    return
            except:
                a = urlparse(source)
                title = os.path.basename(a.path)
            gPlaylist.append(source)
            embed = discord.Embed(title=f"Zur Playlist hinzugefügt:!", description=f"[{title}]({source})", color=3566847)
            player_message = await message.channel.send(embed=embed)
            await player_message.add_reaction("▶️")

    if message.content.startswith("!playlist remove"):
        if message.channel.id == 829007032895668267:
            source = message.content.replace("!playlist remove ", "")
            br = mechanize.Browser()
            try:
                br.open(source)
            except:
                embed = discord.Embed(title="Keine gültige mp3-Datei gefunden!", color=16711680)
                await message.channel.send(embed=embed)
                return
            try:
                title = br.title()
                if title == "- YouTube":
                    embed = discord.Embed(title="YouTube Video nicht gefunden!", color=16711680)
                    await message.channel.send(embed=embed)
                    return
            except:
                a = urlparse(source)
                title = os.path.basename(a.path)
            try:
                gPlaylist.remove(source)
                musik_count -= 1
                embed = discord.Embed(title=f"Aus der Playlist entfernt:!", description=f"[{title}]({source})", color=3566847)
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(title="Nicht in der Playlist gefunden!", color=16711680)
                await message.channel.send(embed=embed)
                return
            return

    if message.content.startswith("!random") or message.content.startswith("!playlist random"):
        if message.channel.id == 829007032895668267:
            random.shuffle(gPlaylist)
            embed = discord.Embed(title="Gemischt!", color=3566847)
            await message.channel.send(embed=embed)

    if message.content.startswith("!playlist clear"):
        if message.channel.id == 829007032895668267:
            gPlaylist.clear()
            embed = discord.Embed(title=f"Playlist geleert!", color=3566847)
            await message.channel.send(embed=embed)

    if message.content == "!playlist":
        if message.channel.id == 829007032895668267:
            desc = ""
            if gPlaylist == []:
                embed = discord.Embed(title="Die Playlist ist leer!", color=3566847)
                await message.channel.send(embed=embed)
                return
            count = 0
            for i in gPlaylist:
                count += 1
                desc = f"{desc}{count}. {i}\n"
            embed = discord.Embed(title="Playlist:", description=desc, color=3566847)
            player_message = await message.channel.send(embed=embed)
            await player_message.add_reaction("▶️")
            await player_message.add_reaction("♻️")

    if message.content.startswith("!skip"):
        if message.channel.id == 829007032895668267:
            try:
                player.stop()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Übersprungen!")
            await message.channel.send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    global player
    global musik_stopped
    global gPlaylist
    global player_repeat
    if not user.id == 825377881546686474:
        if reaction.message.author.id == 825377881546686474:
            if reaction.emoji == "⏯️":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Jetzt spielt:":
                    if player.is_playing():
                        player.pause()
                    elif player.is_paused():
                        player.resume()
                    await reaction.message.remove_reaction("⏯️", user)
            if reaction.emoji == "⏭️":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Jetzt spielt:":
                    try:
                        player.stop()
                    except:
                        pass
                    await reaction.message.remove_reaction("⏭️", user)
            if reaction.emoji == "⏹️":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Jetzt spielt:":
                    musik_stopped = True
                    gPlaylist.clear()
                    try:
                        player.stop()
                    except:
                        pass
                    await reaction.message.remove_reaction("⏹️", user)
            if reaction.emoji == "⏏️":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Jetzt spielt:":
                    musik_stopped = True
                    gPlaylist.clear()
                    voice = discord.utils.get(client.voice_clients, guild=reaction.message.guild)
                    if voice and voice.is_connected():
                        await voice.disconnect()
                    await reaction.message.remove_reaction("⏏️", user)
            if reaction.emoji == "▶️":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Zur Playlist hinzugefügt:" or embed_title == "Playlist:":
                    if not gPlaylist == []:
                        player_repeat = False
                        await reaction.message.channel.trigger_typing()
                        musik_count = 2
                        try:
                            channel = user.voice.channel
                        except:
                            embed = discord.Embed(title="Du bist in keinem Voice-Channel!", color=16711680)
                            await reaction.message.channel.send(embed=embed)
                            await reaction.message.remove_reaction("▶️", user)
                            return
                        player = discord.utils.get(client.voice_clients, guild=reaction.message.guild)
                        if player and player.is_connected():
                            await player.move_to(channel)
                        else:
                            player = await channel.connect()
                        player.stop()
                        await asyncio.sleep(1)
                        sourcex = gPlaylist[0]
                        br = mechanize.Browser()
                        try:
                            br.open(sourcex)
                        except:
                            pass
                        try:
                            title = br.title()
                        except:
                            a = urlparse(sourcex)
                            title = os.path.basename(a.path)
                        try:
                            ydl_opts = {"format": "bestaudio"}
                            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                info = ydl.extract_info(sourcex, download=False)
                                URL = info["formats"][0]["url"]
                        except:
                            URL = gPlaylist[0]
                        try:
                            pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
                            player.play(pplayer, after=myafter)
                        except:
                            player.stop()
                            pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), 1)
                            player.play(pplayer, after=myafter)
                        embed = discord.Embed(title=f"Jetzt spielt:", description=f"[{title}]({sourcex})")
                        player_message = await reaction.message.channel.send(embed=embed)
                        await player_message.add_reaction("⏏️")
                        await player_message.add_reaction("⏹️")
                        await player_message.add_reaction("⏯️")
                        await player_message.add_reaction("⏭️")
                        await player_message.add_reaction("🔁")
                    await reaction.message.remove_reaction("▶️", user)
                    await reaction.message.remove_reaction("▶️", client.user)
            if reaction.emoji == "♻️":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Playlist:":
                    if not gPlaylist == []:
                        gPlaylist.clear()
                        embed = discord.Embed(title="Playlist geleert!")
                        await reaction.message.channel.send(embed=embed)
                    await reaction.message.remove_reaction("♻️", user)
            if reaction.emoji == "🔁":
                embed_title = reaction.message.embeds[0].title
                if embed_title == "Jetzt spielt:":
                    if player_repeat:
                        player_repeat = False
                        embed = discord.Embed(title="Wiederholung nicht mehr aktiv!")
                        await reaction.message.channel.send(embed=embed)
                    else:
                        player_repeat = True
                        embed = discord.Embed(title="Wiederholung aktiv!")
                        await reaction.message.channel.send(embed=embed)
                    await reaction.message.remove_reaction("🔁", user)

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 785155679295111208:
        if not discord.utils.get(member.roles, name="Muted") is None:
            try:
                await member.move_to(None)
                try:
                    if before.channel.members == [] and not before.channel.id == 826115028763148289:
                        if before.channel.category_id == 785155679295111210:
                            await before.channel.delete()
                except:
                    pass
                try:
                    if before.channel.members == [] and not before.channel.id == 826115072455737354:
                        if before.channel.category_id == 826114944901709874:
                            await before.channel.delete()
                except:
                    pass
            except:
                pass
            try:
                await member.edit(mute=True)
                await member.edit(deafen=True)
            except:
                pass
            return
        if after.mute:
            await member.edit(mute=False)
        if after.deaf and not member.bot:
            await member.edit(deafen=False)
        if after.deaf == False and member.bot:
            await member.edit(deafen=True)
        channel = after.channel
        try:
            if before.channel.members == [] and not before.channel.id == 826115028763148289:
                if before.channel.category_id == 785155679295111210:
                    await before.channel.delete()
        except:
            pass
        try:
            if before.channel.members == [] and not before.channel.id == 826115072455737354:
                if before.channel.category_id == 826114944901709874:
                    await before.channel.delete()
        except:
            pass

        try:
            if channel.id == 826115028763148289:
                guild = after.channel.guild
                private_channels = discord.utils.get(guild.categories, id=785155679295111210)
                voice_channel = await guild.create_voice_channel(member.name, overwrites=None, category=private_channels)
                await member.move_to(voice_channel)
                await voice_channel.set_permissions(member, connect=True, speak=True, move_members=True, manage_roles=True, manage_channels=True, view_channel=True)
        except:
            return


        try:
            if channel.id == 826115072455737354:
                guild = after.channel.guild
                musik_channels = discord.utils.get(guild.categories, id=826114944901709874)
                musikchannels = []
                for channel in musik_channels.channels:
                    musikchannels.append(channel.name)
                if not "Musik 1" in musikchannels and not "Musik 2" in musikchannels and not "Musik 3" in musikchannels:
                    channelname = "Musik 1"
                zahlen = []
                for name in musikchannels:
                    zahl = name.replace("Musik ", "")
                    try:
                        zahl = int(zahl)
                    except:
                        continue
                    zahlen.append(zahl)
                if not zahlen == []:
                    MINT = zahlen[0]
                    MAXI = zahlen[0]
                    for zahl in zahlen:
                        if zahl < MINT:
                            MINT = zahl
                        elif zahl > MAXI:
                            MAXI = zahl
                    channelname = f"Musik {MAXI+1}"
                else:
                    channelname = "Musik 1"
                voice_channel = await guild.create_voice_channel(channelname, overwrites=None, category=musik_channels)
                await member.move_to(voice_channel)
                await voice_channel.set_permissions(member, connect=True, speak=False, view_channel=True)
        except:
            pass

@client.event
async def on_guild_channel_create(channel):
    try:
        await channel.create_webhook(name="Move", reason="WebHook sync")
    except:
        pass
    
    embed = discord.Embed(title="Channel erstellt!", color=0x00ff2a)
    embed.add_field(name="Name", value=f"{channel.name}", inline=False)
    embed.add_field(name="ID", value=f"{channel.id}", inline=False)
    embed.add_field(name="Typ", value=f"{channel.type}", inline=False)
    embed.add_field(name="NSFW", value=f"{channel.is_nsfw()}", inline=False)
    await client.get_channel(826834073421873192).send(embed=embed)

@client.event
async def on_guild_role_create(role):
    embed = discord.Embed(title="Rang erstellt!", color=0x00ff2a)
    embed.add_field(name="Name", value=f"{role.name}", inline=False)
    embed.add_field(name="ID", value=f"{role.id}", inline=False)
    embed.add_field(name="Farbe", value=f"{role.color}", inline=False)
    embed.add_field(name="Erwähnbar", value=f"{role.mentionable}", inline=False)
    await client.get_channel(826834073421873192).send(embed=embed)

client.loop.create_task(auto_unban())
client.loop.create_task(change_status())
client.run("ODI1Mzc3ODgxNTQ2Njg2NDc0.YF9DDQ.uiK7EeWu4ZpMunKKDfKSU90alLo")
