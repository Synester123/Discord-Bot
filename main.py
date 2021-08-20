
from http import client
import youtube_dl, os, mechanize
from urllib.parse import urlparse
from youtubesearchpython import VideosSearch
import feedparser
import random,  asyncio, nacl, ffmpeg
youtube_dl.utils.std_headers["Cookie"] = ""

import mechanize as mechanize
import discord
import datetime
import youtube_dl
import io
from urllib import parse, request
import re

from discord.ext import commands, tasks

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
global player
global player_repeat

gPlaylist = []
musik_stopped = False
musik_count = 0
player = ""
player_repeat = False


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
            embed.add_field(name=f"by {message.author} ({message.author.id})",
                            value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
        except:
            mod1 = await client.fetch_user(542265299387285505)
            embed = discord.Embed(title="Neue ModMail Anfrage", description=f"{message.content}")
            embed.add_field(name=f"by {message.author} ({message.author.id})",
                            value=f"!reply {message.author.id} {message.id}")
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


bot = commands.Bot(command_prefix='-', description="This is a Helper Bot")
client = commands.Bot(command_prefix="-")

def myafter(error):
    print(f"M-Error: {error}")
    fut = asyncio.run_coroutine_threadsafe(playit(), client.loop)
    fut.result()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="-Nhelp", url='https://www.twitch.tv/warmerkakaoo'))
    print('Wir sind eingelogt')



@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}")
    embed.add_field(name="Server erstellt am", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}", inline=False)
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name="Users", value=ctx.guild.member_count)
    embed.add_field(name="Channels", value=len(ctx.guild.channels))
    embed.add_field(name='Bot Deverlopers', value="<@810164383308709900>")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name}/GetOnMyPussy', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@bot.command()
async def clear(ctx, amount=5):
    try:
        await ctx.channel.purge(limit=amount)
    except:
        embed = discord.Embed(title=f"{ctx.author.name}", description="!ERROR!")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        embed = discord.Embed(title="muted", description=f"{member.mention} was muted ",
                              colour=discord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")



@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await member.send(f" you have unmutedd from: - {ctx.guild.name}")
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",
                              colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)


@bot.command()
async def website(ctx):
    embed = discord.Embed(color=0x00ffe0)
    embed.add_field(name="Bot Website", value="sssss")
    embed.add_field(name="Standart Commands", value="`-Nhelp`\r\n"
                                                    "`-youtube`\r\n"
                                                    "`-userinfo`\r\n"
                                                    "`-serverinfo`", inline=False)
    embed.add_field(name="Mod Commands", value="`-ban`\r\n"
                                               "`-kick`\r\n"
                                               "`-tempban`\r\n"
                                               "`-mute`\r\n"
                                               "`-clear`\r\n"
                                               "`-tempmute`\r\n"
                                               "`-role-info`\r\n"
                                               "`-slowmode`\r\n"
                                               "`-unban`\r\n"
                                               "`-unmute`\r\n"
                                               "`-warn`\r\n", inline=False)
    embed.add_field(name="Music Commands", value="-musik", inline=False)
    embed.set_footer(text=f'{ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)



@bot.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    embed = discord.Embed(color=0x00ffe0)
    embed.add_field(name="Slowmode", value=f"Slomode wurde auf {seconds} gestellt!")

    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.content.startswith("-userinfo"):
        embed = discord.Embed(title=message.author.name, color=0x00ffe0)
        embed.add_field(name="Beigetreten am", value=message.author.joined_at, inline=False)
        embed.add_field(name="Account erstellt am", value=message.author.created_at, inline=False)
        embed.add_field(name="Name#tag", value=message.author, inline=False)
        embed.add_field(name="ID", value=message.author.id, inline=False)
        embed.add_field(name="Nick", value=message.author.nick, inline=False)
        embed.add_field(name="Höchster Rang", value=message.author.top_role, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{message.author.name}/GetOnMyPussy', icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("-embed"):
        embed = discord.Embed(title="Ein Embed!", description="ist doch deutlich schöner!", color=0x4b49d8)
        embed.set_footer(text="Footer!")
        embed.set_image(url="https://media.discordapp.net/attachments/858380252359295017/878234917186715658/f929762526a03a67bd9ea88e93633d84.png?width=676&height=676")
        embed.set_thumbnail(
            url="https://images-ext-2.discordapp.net/external/BxhRAnrziwzyS4-U-NniIrlomeNY2OJf2S4fjiq6qPA/https/static-cdn.jtvnw.net/jtv_user_pictures/61f85a70-33e9-4144-b08a-bee144d444dc-profile_image-300x300.jpg")
        embed.add_field(name="Feld 1", value="Wert 1", inline=False)
        embed.add_field(name="Feld 2", value="Wert 2", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("-musik"):
            await message.channel.trigger_typing()
            await asyncio.sleep(0.05)
            embed = discord.Embed(title="Musik - Commands", color=3566847)
            embed.add_field(name="-play URL", value="Spiele den Song bei der URL", inline=False)
            embed.add_field(name="-playlist", value="Listet die Playlist", inline=False)
            embed.add_field(name="-playlist add URL", value="Fügt die URL der Playlist hinzu", inline=False)
            embed.add_field(name="-playlist add URL1, URL2", value="Fügt die URLs der Playlist hinzu", inline=False)
            embed.add_field(name="-playlist remove URL", value="Löscht die URL aus der Playlist", inline=False)
            embed.add_field(name="-playlist clear", value="Leert die Playlist", inline=False)
            embed.add_field(name="-play playlist", value="Spielt die Playlist ab", inline=False)
            embed.add_field(name="-join", value="Bot joint deinem Voice-Channel", inline=False)
            embed.add_field(name="-leave", value="Bot verlässt seinen Voice-Channel", inline=False)
            embed.add_field(name="-pause", value="Pausiert den Song", inline=False)
            embed.add_field(name="-resume", value="Setzt den Song fort", inline=False)
            embed.add_field(name="-stop", value="Stoppt alle Songs und leert die Playlist", inline=False)
            embed.add_field(name="-skip", value="Überspringt den Song", inline=False)
            embed.add_field(name="-repeat", value="Wiederholt den Song in Dauerschleife", inline=False)
            embed.add_field(name="-reactions", value="Erklärt die Reactions", inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("-join"):
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

    if message.content.startswith("-leave"):
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

    if message.content.startswith("-play") and not message.content.startswith(
            "-playlist") and not message.content == "-play playlist":
            player_repeat = False
            await message.channel.trigger_typing()
            musik_count = 1
            gPlaylist.clear()
            source = message.content.replace("-play ", "")
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
                pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL,
                                                                              before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"),
                                                       1)
                player.play(pplayer, after=myafter)
            except:
                player.stop()
                pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL,
                                                                              before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"),
                                                       1)
                player.play(pplayer, after=myafter)
            embed = discord.Embed(title="Jetzt spielt:", description=f"[{title}]({source})")
            player_message = await message.channel.send(embed=embed)
            await player_message.add_reaction("⏏️")
            await player_message.add_reaction("⏹️")
            await player_message.add_reaction("⏯️")
            await player_message.add_reaction("⏭️")
            await player_message.add_reaction("🔁")

    if message.content.startswith("-pause"):
            try:
                player.pause()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Pausiert!")
            await message.channel.send(embed=embed)

    if message.content.startswith("-resume"):
            try:
                player.resume()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Fortgesetzt!")
            await message.channel.send(embed=embed)

    if message.content.startswith("-repeat"):
            if player_repeat:
                player_repeat = False
                embed = discord.Embed(title="Wiederholung nicht mehr aktiv!")
                await message.channel.send(embed=embed)
            else:
                player_repeat = True
                embed = discord.Embed(title="Wiederholung aktiv!")
                await message.channel.send(embed=embed)

    if message.content.startswith("-stop"):
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

    if message.content == "-play playlist" or message.content == "-playlist play":
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
                    pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL,
                                                                                  before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"),
                                                           1)
                    player.play(pplayer, after=myafter)
                except:
                    player.stop()
                    pplayer = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL,
                                                                                  before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"),
                                                           1)
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

    if message.content.startswith("-playlist add"):
            source = message.content.replace("-playlist add ", "")
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
                        done_tasks, pending_tasks = await asyncio.wait(pending_tasks,
                                                                       return_when=asyncio.FIRST_COMPLETED)
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
            embed = discord.Embed(title=f"Zur Playlist hinzugefügt:!", description=f"[{title}]({source})",
                                  color=3566847)
            player_message = await message.channel.send(embed=embed)
            await player_message.add_reaction("▶️")

    if message.content.startswith("!playlist remove"):
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
                embed = discord.Embed(title=f"Aus der Playlist entfernt:!", description=f"[{title}]({source})",
                                      color=3566847)
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(title="Nicht in der Playlist gefunden!", color=16711680)
                await message.channel.send(embed=embed)
                return
            return

    if message.content.startswith("!random") or message.content.startswith("!playlist random"):
            random.shuffle(gPlaylist)
            embed = discord.Embed(title="Gemischt!", color=3566847)
            await message.channel.send(embed=embed)

    if message.content.startswith("!playlist clear"):
            gPlaylist.clear()
            embed = discord.Embed(title=f"Playlist geleert!", color=3566847)
            await message.channel.send(embed=embed)

    if message.content == "!playlist":
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
            try:
                player.stop()
            except:
                embed = discord.Embed(title="Derzeit läuft nichts!", color=16711680)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title=f"Übersprungen!")
            await message.channel.send(embed=embed)



@bot.command()
async def leave(context):
        await context.voice_client.disconnect()


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

bot.run("ODc3MTQyMzM0NDczNjM3OTI4.YRuUdQ.yLJ_uifxuPLxsh7cjx2tW3JVIdI")