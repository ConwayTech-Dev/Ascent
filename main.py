from discord.ext import commands, tasks
import discord
import os
import requests
import re
import aiohttp
import json
import urllib
import pyjokes
import platform
import random
import math
import asyncio
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

loginToken = os.getenv("token")

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.typing = True

bot = commands.Bot(intents=intents)

coinFlips = ["IT'S HEADS!!", "IT'S TAILS!!"]

randQuotes = [
  "**“In all chaos there is a cosmos, in all disorder a secret order.”** ***-Carl Jung***",
  "**“You don't get in life what you want; you get in life what you are.”** ***-Les Brown***",
  "**“Do not worry about your difficulties in mathematics. I can assure you mine are still greater.”** ***-Albert Einstein***",
  "**“The strongest and sweetest songs yet remain to be sung.”** ***-Walt Whitman***",
  "**“The only way it gets better for you is when you get better. Better is not something you wish, it's something you become.”** ***-Jim Rohn***",
  "**“Things do not have meaning. We assign meaning to everything.”** ***-Tony Robbins***",
  "**“Be polite to all, but intimate with few.”** ***-Thomas Jefferson***",
  "**“Never settle for the crumbs of life.”** ***-Og Mandino***",
  "**“Truth is not something outside to be discovered, it is something inside to be realized.”** ***-Osho***",
  "**“Human happiness and moral duty are inseparably connected. ”** ***-George Washington***",
  "**“You are a function of what the whole universe is doing in the same way that a wave is a function of what the whole ocean is doing.”** ***-Alan Watts***",
  "**“If you do not change direction, you may end up where you are heading.”** ***-Lao Tzu***",
  "**“You must be the change you wish to see in the world.”** ***-Mahatma Gandhi***",
  "**“Whatever you are, be a good one.”** ***-Abraham Lincoln***",
  "**“In every walk with nature one receives far more than he seeks.”** ***-John Muir***",
  "**“Never interrupt your enemy when he is making a mistake.”** ***-Napoleon Bonaparte***",
  "**“The pain of parting is nothing to the joy of meeting again.”** ***-Charles Dickens***",
  "**“Enthusiasm is a vital element toward the individual success of every man or woman.”** ***-Conrad Hilton***",
  "**“You may delay, but time will not.”** ***-Benjamin Franklin***",
  "**“Everyone is a moon, and has a dark side which he never shows to anybody.”** ***-Mark Twain***",
  "**“If you truly love Nature, you will find beauty everywhere.”** ***-Vincent van Gogh***",
  "**“To affect the quality of the day, that is the highest of arts.”** ***-Henry David Thoreau***",
  "**“Monsters are real, and ghosts are real too. They live inside us, and sometimes, they win.”** ***-Stephen King***",
  "**“Keep smiling, because life is a beautiful thing and there's so much to smile about.”** ***-Marilyn Monroe***",
  "**“Believe and act as if it were impossible to fail.”** ***-Charles Kettering***",
  "**“I learned the value of hard work by working hard. ”** ***-Margaret Mead***",
  "**“Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.”** ***-Sun Tzu***",
  "**“There are no shortcuts to any place worth going.”** ***-Beverly Sills***",
  "**“Time heals what reason cannot.”** ***-Seneca***",
  "**“Failure is an option, fear is not.”** ***-James Cameron***",
  "**“Life is trying things to see if they work.”** ***-Ray Bradbury***",
  "**“People don't realize that now is all there ever is; there is no past or future except as memory or anticipation in your mind.”** ***-Eckhart Tolle***",
  "**“It doesn't matter if the glass is half empty or half full. Be grateful you have a glass - you're the only person that can decide what's in it.”** ***-Gurbaksh Chahal***",
  "**“Victory is always possible for the person who refuses to stop fighting.”** ***-Napoleon Hill***",
  "**“When you reach the end of your rope, tie a knot in it and hang on.”** ***-Franklin D. Roosevelt***",
  "**“There is always but never later.”** ***- Anonymous***",
  "**“If you hang on, and believe, it can happen.”** ***-Anonymous***",
  "**“Technology can hard and complicated to some, but to ones who are same, but more interested, will get to having the actual way of master.”**",
  "**“Don't spend major time on minor things.”** ***-Jim Rohn***",
  "**“Forget safety. Live where you fear to live.”** ***-Rumi***",
  "**Sometimes humans forget that they are humans.** ***-Someone***",
  "**“He who is not contented with what he has, would not be contented with what he would like to have.”** ***-Socrates***",
  "**“You use a glass mirror to see your face; you use works of art to see your soul.”** ***-George Bernard Shaw***",
  "**“Knowldege itself is power. Very much.”** ***-Unknown***",
  "**“Allow motion to equal emotion.”** ***-Elbert Hubbard***",
  "**“Success comes from knowing that you did your best to become the best that you are capable of becoming.”** ***-John Wooden***",
  "**Smuggling was carried out through holes and cracks in the walls... and through all the hidden places unfamiliar to the conquerors' foreign lives.** ***-Chaim A. Kaplan***",
  "**“The chief cause of failure and unhappiness is trading what you want most for what you want right now.”** ***-Zig Ziglar***",
  "**“A mistake is only an error, it becomes a mistake when you fail to correct it.”** ***-John Lennon***",
  "**“Confidence is contagious. So is lack of confidence.”** ***-Vince Lombardi***",
  "**“Only by acceptance of the past, can you alter it.”** ***-T.S. Eliot***"
]


@bot.event
async def on_ready():
  print("Ascent is now active.")
  await bot.change_presence(status=discord.Status.online,
                            activity=discord.Activity(
                              type=discord.ActivityType.watching,
                              name="for Slash Commands"))
  print("Use Slash Commands to start!")


@bot.slash_command(name="version", description="Shows Ascent's version.")
async def version(ctx):
  vembed = discord.Embed(title="Ascent Version",
                         description="Ascent's software is v8.1.",
                         color=0x2dc7fb)
  vembed.set_author(
    name="Ascent",
    icon_url=
    "https://cdn.discordapp.com/avatars/794618348289392680/04695adb3abad70391fc0fb13a785075.png?size=256"
  )
  vembed.add_field(name="Date Released:",
                   value="January 30, 2023",
                   inline=False)
  vembed.add_field(
    name="New in v8.1:",
    value="Improved the v8.0 remake, fixing bug fixes and more.",
    inline=False)
  vembed.add_field(name="Client Build:", value="Ascent Stable", inline=True)
  vembed.add_field(name="Made by:", value="ConwayTech", inline=True)
  vembed.set_footer(
    text=
    "ID = 794618348289392680 | Last update before the most recent: January 30, 2023 | Fun Fact = use /ping to get the bot's latency!"
  )
  await ctx.reply(embed=vembed)


@bot.slash_command(name="ping", description="View Ascent's ping (latency).")
async def ping(ctx):
  pembed = discord.Embed(title="PONG!",
                         description="Check out Ascent's bot ping!.",
                         color=0xf00f3c)
  pembed.set_author(
    name="Ascent",
    icon_url=
    "https://cdn.discordapp.com/avatars/794618348289392680/04695adb3abad70391fc0fb13a785075.png?size=256"
  )
  pembed.add_field(name="Latency",
                   value=f'{round(bot.latency * 1000)}ms',
                   inline=True)
  await ctx.reply(embed=pembed)


# quote command
@bot.slash_command(name="quote", description="Responds with a random quote.")
async def quote(ctx):
  async with ctx.typing:
    asyncio.sleep(1.5)
  await ctx.reply(random.choice(randQuotes))


# ID command
@bot.slash_command(description="Find a user's Discord ID.")
async def id(ctx, *, member: discord.Member):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.reply(f"{member.mention}'s ID is {member.id}.")


# Gets a server's icon!
@bot.slash_command(description="Find a server's icon.")
async def servericon(ctx):
  await ctx.send(f"Here's the server icon for {ctx.guild.name}...")
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.send(f"{ctx.guild.icon_url}")


# Lenth Command
@bot.slash_command(description="View the length of a message.")
async def length(ctx):
  await ctx.reply(
    'Your message is {} characters long.'.format(len(ctx.message.content) - 8))


@bot.slash_command()
@commands.has_permissions(manage_roles=True, manage_messages=True)
async def traineemod(ctx, *, member: discord.Member):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.send(
    f"WORKING, really, I am! Congrats to **{member}** on becoming a TRAINEE MODERATOR!🎉"
  )
  traembed = discord.Embed(
    title="Congrats!",
    description=
    f"You've been made a trainee moderator in {ctx.guild.name}! Niceee, bruh!",
    color=0x067793)
  traembed.set_author(name="Thanks for choosing Ascent!")
  traembed.set_thumbnail(
    url=
    "https://cdn.discordapp.com/attachments/791828615423721512/801149866255450142/TakeMyMoney.png"
  )
  traembed.add_field(name="Who Promoted You:",
                     value=f"{ctx.author}",
                     inline=True)
  traembed.add_field(name="Congratulations!",
                     value="Do well as an ALL new mod!",
                     inline=True)
  traembed.add_field(
    name="Fun Fact:",
    value="Use `bruh repeat ___` to repeat messages multiple times!",
    inline=True)
  traembed.set_footer(
    text=
    "Ascent, the ultimate Discord moderation and fun bot | Created by @ConwayTech#5626"
  )
  await member.send(embed=traembed)


@bot.slash_command(aliases=["basicpoll"])
async def poll(ctx, *, polq):
  polembed = discord.Embed(
    title="Poll Coming!!",
    description=f"Eh, a poll? Here's the YES or NO question: {polq}",
    timestamp=ctx.message.created_at)
  pmsg = await ctx.channel.send(embed=polembed)
  await pmsg.add_reaction('👍')
  await pmsg.add_reaction('👎')
  await pmsg.add_reaction('❌')
  await pmsg.add_reaction('✔')


async def poke(ctx, member: discord.Member = None):
  if member is not None:
    dmchannel = member.dm_channel
    if dmchannel is None:
      dmchannel = await member.create_dm()
    await dmchannel.send(f"%s POKED you, in {ctx.guild.name}... lol!!" %
                         ctx.author.name)
  else:
    await ctx.send(
      "Please @Mention the user who you would like to poke... you didn't choose anybody."
    )


@bot.slash_command(aliases=["yt_thumbnail", "youtubethumbnail"])
async def youtube_thumbnail(ctx, video_id):
  await ctx.reply(
    "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg" +
    f"\nThere's that YouTube thumbnail for you, {ctx.author.mention}")


@bot.slash_command()
async def softban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await member.unban()
  await ctx.send(f"Done. We've SOFTBANNED {member}, successfully!")


@bot.slash_command()
async def repeat(
    ctx,
    times: int,
    content='...you have to specify what you want to actually repeat lol'):
  for i in range(times):
    await ctx.send(content)


@bot.slash_command()
@commands.cooldown(1, 6, commands.BucketType.user)
async def versionstats(ctx):
  dpyv = discord.__version__
  pyv = platform.python_version()
  await ctx.send(
    f"Ascent's [**Discord.py**](https://discordpy.readthedocs.io) version: \n{dpyv} \nAscent's [**Python**](https://python.org) version: \n{pyv}"
  )


# thx to a GitHub page - userinfo command
@bot.slash_command(
  pass_context=True,
  aliases=["user_info", "memberinfo", "member_info", "myuserinfo"])
@commands.guild_only()
@commands.cooldown(1, 8, commands.BucketType.user)
async def userinfo(ctx):
  async with ctx.typing():
    await asyncio.sleep(1)
  userinfoembed = discord.Embed(title=f"{ctx.author}'s Info...",
                                timestamp=ctx.created_at,
                                color=0x176cd5)
  userinfoembed.add_field(name="Current Status:",
                          value=ctx.author.status,
                          inline=False)
  userinfoembed.add_field(name="Username:", value=ctx.author.name)
  userinfoembed.add_field(name="ID:", value=ctx.author.id, inline=True)
  userinfoembed.add_field(name="Highest Role (in this server):",
                          value="'" + ctx.author.top_role + "'",
                          inline=False)
  userinfoembed.add_field(name="Roles:",
                          value=len(ctx.author.roles),
                          inline=True)
  userinfoembed.add_field(name="Joined:",
                          value=ctx.author.joined_at,
                          inline=False)
  userinfoembed.add_field(name="Created At:",
                          value=ctx.author.created_at,
                          inline=True)
  userinfoembed.set_thumbnail(url=ctx.author.avatar_url)
  await ctx.send(embed=userinfoembed)


# creates a text channel
@bot.slash_command(
  aliases=["create_text_channel", "new_text_channel", "newtextchannel"],
  help="Make a new text channel (Guilds ONLY)!")
@commands.guild_only()
async def createtextchannel(ctx, channelname):
  await ctx.guild.create_text_channel(channelname)
  await ctx.send(
    f"We've successfully created a channel that's called '{channelname}'... check it out!"
  )


# guess the number!
@bot.slash_command(name="guess_the_number",
                   aliases=["guessthenumber", "number_guessing_game"])
async def guess_the_number(ctx):
  number = random.randint(0, 10)
  for i in range(0, 6):
    await ctx.send('Guess my number from one to ten!')
    response = await bot.wait_for('message')
    guess = int(response.content)
    if guess > number:
      await ctx.send('My number is bigger...')
    elif guess < number:
      await ctx.send('My number is smaller...')
    else:
      await ctx.send('YOU GUESSED MY NUMBER! Good job!')


# 8Ball command
@bot.slash_command(aliases=['8ball'], help="SHAKE that Magic 8Ball!")
async def eightball(ctx, *, question):
  responses = [
    "***It is certain.***", "***It is decidedly so.***",
    "***Without a doubt.***", "***Yes – definitely.***",
    "***You may rely on it.***", "***As I see it, yes.***",
    "***Most likely.***", "***Outlook good.***", "***Yes.***",
    "***Signs point to yes.***", "***Reply hazy, try again.***",
    "***Ask again later.***", "***Better not tell you now.***",
    "***Cannot predict now.***", "***Concentrate and ask again.***",
    "***Don't count on it.***", "***My reply is no.***",
    "***My sources say no.***", "***Outlook not so good.***",
    "***Very doubtful.***"
  ]
  await ctx.reply(
    f'🎱Your Question: {question}\n The 8Ball has an answer...\n{random.choice(responses)}🎱'
  )


# User Welcome
@bot.slash_command(aliases=["say_hi_to", "say_hello_to"])
async def welcome(ctx, *, member: discord.Member):
  await member.send(
    f"HEY THERE, {member.Mention}! Good. Now you're here. Welcome, WELCOME, to {ctx.guildname}!"
  )


# jokes
@bot.slash_command(help="Tell a joke!")
async def pyjoke(ctx):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.reply("*" + pyjokes.get_joke() + "*")


# dad joke command
@bot.slash_command(help="Tell an *amazing* dad joke!")
async def dadjoke(ctx):
  djapi = 'https://icanhazdadjoke.com/'
  async with aiohttp.request('GET', djapi, headers={'Accept':
                                                    'text/plain'}) as r:
    result = await r.text()
    await ctx.reply('`' + result + '`')


@bot.slash_command(
  pass_context=True,
  usage=
  "bruh warn [that member you want to punish] + [reason] (put none if you have no reason...)"
)
@commands.has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx, member: discord.Member, *, reason):
  if member == bot:
    ctx.reply("Don't even TRY to warn me lol")
  if reason == None:
    warnembed = discord.Embed(
      title="You Have Been WARNED.",
      description=
      "You've been warned. Please watch out; more warns can result in kicks.",
      color=0xa30a0a)
    warnembed.set_author(
      name=f"You were WARNED in the Server {ctx.guild.name}.")
    warnembed.set_thumbnail(
      url=
      "https://cdn.discordapp.com/attachments/791828615423721512/800524933221580820/Pepehammer.png"
    )
    warnembed.add_field(name="Who Warned You:",
                        value=f"{ctx.author}",
                        inline=True)
    warnembed.add_field(name="Reason", value=f"N/A", inline=True)
    await member.send(embed=warnembed)
    await ctx.reply(
      f"The NAUGTY NAUGTY {member} has SUCESSFULLY been warned! I wonder, I sure do wonder why..."
    )
  else:
    warnembed = discord.Embed(
      title="You Have Been WARNED.",
      description=
      "You've been warned. Please watch out; more warns can result in kicks.",
      color=0xa30a0a)
    warnembed.set_author(
      name=f"You were WARNED in the Server {ctx.guild.name}.")
    warnembed.set_thumbnail(
      url=
      "https://cdn.discordapp.com/attachments/791828615423721512/800524933221580820/Pepehammer.png"
    )
    warnembed.add_field(name="Who Warned You:",
                        value=f"{ctx.author}",
                        inline=True)
    warnembed.add_field(name="Reason", value=f"{reason}", inline=True)
    await member.send(embed=warnembed)
    await ctx.send(
      f"The NAUGTY NAUGTY {member} has SUCESSFULLY been warned! I wonder, I sure do wonder why..."
    )


@bot.slash_command(
  pass_context=True,
  usage=
  "bruh [warn or help] [that member you want to punish] + [reason] (put 'none' if you have no reason...)",
  help="Warn someone or send a SECRET MESSAGE!")
async def secretmessage(ctx, member: discord.Member, *, message: str):
  if message == None:
    await ctx.send(
      "HEY, c'mon! You forgot to put in that reason I need!! If you don't want a reason, type in `none` for your reason."
    )
    return
  else:
    await ctx.send(
      f"PASSIN' NOTES IN CLASS?? AHHAHAHA! We've sent that SO secret message to your friend {member.mention}."
    )
    await member.send(
      f"HEY, {ctx.author} came to send you a SECRET message in {ctx.guild.name}: They just said this... not much: '{message}'"
    )
    async with ctx.typing():
      await asyncio.sleep(1)
    await ctx.send(
      f"We've sent a secret message to your friend {member}, sucessfully! He/she has been DMed."
    )


@bot.slash_command(aliases=["today_weather_pasadena"],
                   help="Tells you the weather in Pasadena.")
async def pasadena(ctx):
  async with ctx.typing():
    await asyncio.sleep(2)
  response = requests.get('http://wttr.in/Pasadena,+CA', stream=True)
  remove_ansi = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
  enbm = "```" + remove_ansi.sub('', response.text[38:322]) + "```"
  wemb = discord.Embed(title=response.text[16:38], description=enbm)
  await ctx.send(embed=wemb)


@bot.slash_command(aliases=["today_weather_lacanada"])
async def lacanadaweather(ctx):
  async with ctx.typing():
    await asyncio.sleep(2)
  response = requests.get('http://wttr.in/La+Canada,+Flintridge', stream=True)
  remove_ansi = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
  enbm = "```" + remove_ansi.sub('', response.text[38:322]) + "```"
  wemb = discord.Embed(title=response.text[16:38], description=enbm)
  await ctx.send(embed=wemb)


@bot.slash_command(aliases=["flip_a_coin"], help="Flip a coin!")
@commands.cooldown(1, 8, commands.BucketType.user)
async def coinflip(ctx):
  await ctx.send(
    "WE ARE FLIPPING, please wait! I wonder which side the coin will go on...")
  async with ctx.typing():
    await asyncio.sleep(2)
  await ctx.send(f"What a suprise. {random.choice(coinFlips)}")


# Emoji Command
@bot.slash_command(description="Get info on an emoji")
async def emoji_info(ctx, emoji: discord.Emoji = None):
  if not emoji:
    await ctx.invoke(bot.get_command("help"), entity="emoji_info")
  try:
    emoji = await emoji.guild.fetch_emoji(emoji.id)
  except discord.NotFound:
    return await ctx.reply("`Emoji not found inside this server...`")

  emoji_is_managed = "Yes" if emoji.managed else "No"
  emoji_is_animated = "Yes" if emoji.animated else "No"
  emojiREQUIRESCOLONS = "Yes" if emoji.require_colons else "No"
  emojiCreationTime = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
  emojiRequirements = "Everyone can use this emoji" if not emoji.roles else " ".join(
    role.name for role in emoji.roles)

  emojiDESC = f"""
     __**General**__
     **- Name:** {emoji.name}
     **- ID:** {emoji.id}
     **- URL:** [Link to Emoji]({emoji.url})
     **- Uploader:** {emoji.user.name}
     **- Time Created:** {emojiCreationTime}
     **- Usable By:** {emojiRequirements}
     __**Other Info**__
     **- Animated:** {emoji_is_animated}
     **- Managed:** {emoji_is_managed}
     **- Requires Colon:** {emojiREQUIRESCOLONS}
     **- Server Name:** {emoji.guild.name}
     **- Server ID:** {emoji.guild.id}
     """

  emoembed = discord.Embed(title=f"Emoji Info For: `{emoji.name}`",
                           description=emojiDESC,
                           color=0xadd8e6)
  emoembed.set_thumbnail(url=emoji.url)

  await ctx.reply(embed=emoembed)


# random animals...
@bot.slash_command(description="Pull from the internet a random dog pic!")
async def dog(ctx):
  async with ctx.typing():
    await asyncio.sleep(4)
    async with aiohttp.ClientSession() as cs:
      async with cs.get("http://random.dog/woof") as r:
        data = await r.json()

        dogembed = discord.Embed(title="Woof, Woof!")
        dogembed.set_image(url=data['file'])
        dogembed.set_footer(
          text="We fetched that dog image from http://random.dog/.")
        dogembed.add_field(name="There. A random picture of a cat.",
                           value="I hope you like the picture :)",
                           inline=False)
        await ctx.reply(embed=dogembed)


@bot.slash_command(description="Send a random picture of a cat!")
async def cat(ctx):
  async with ctx.typing():
    await asyncio.sleep(4)
    async with aiohttp.ClientSession() as cs:
      async with cs.get("http://aws.random.cat/meow") as r:
        data = await r.json()

        catembed = discord.Embed(title="Meow, Meow!")
        catembed.set_image(url=data['file'])
        catembed.set_footer(
          text="We fetched that cat image from http://random.cat/.")
        catembed.add_field(name="There. A random picture of a cat.",
                           value="I hope you like the picture :)",
                           inline=False)
        await ctx.send(embed=catembed)


# "Hack" someone
@bot.slash_command(description="Hack someone... definitely not fake!")
@commands.guild_only()
@commands.cooldown(1, 8, commands.BucketType.user)
async def hack(ctx, *, member: discord.Member):
  if member is None:
    await ctx.reply("...you can't hack an invisible person!! Try again...")
  elif member is bot:
    bothackembed = discord.Embed(
      title="YOU CAN'T TRICK ME...",
      description=
      "Ya can't trick me!! Back off, you're not allowed to hack Ascent.. did you actually think I would let that happen? NOPE lol"
    )

    await ctx.reply(embed=bothackembed)
  else:
    hackingembed = discord.Embed(title=f"Hacking {member}...",
                                 description="Almost Done!")
    hackingembed.set_thumbnail(
      url=
      "https://cdn.discordapp.com/attachments/791828615423721512/798341642624696380/WindowsTerminalLogo.png"
    )
    hackingembed.add_field(name="Speed", value="2GB Data/sec", inline=True)
    hackingembed.add_field(name="Time Left",
                           value="Around 2/3 secs",
                           inline=True)
    hackingembed.set_footer(text="*Just for Fun*")

    await ctx.send(embed=hackingembed)
    async with ctx.typing():
      await asyncio.sleep(2)

    hackedembed = discord.Embed(
      title="All Done!",
      description=f"You HACKED {member}... congrats!",
      color=0x9a0404)
    hackedembed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
    hackedembed.add_field(name="*Email*",
                          value=f"`{member}{random.choice(emaildomain)}`",
                          inline=False)
    hackedembed.add_field(name="*Discord Password*",
                          value=f"`{random.choice(dispasses)}`",
                          inline=True)
    hackedembed.add_field(name="*Email Password*",
                          value=f"`{random.choice(epasses)}`",
                          inline=True)
    hackedembed.add_field(name="*IP Address*",
                          value=f"`{random.choice(ipfakes)}`",
                          inline=False)
    hackedembed.set_footer(text="*Just for Fun... 👍😃👍* | You're a HACKER!")

    await ctx.send(embed=hackedembed)
    await ctx.add_reaction("🤣")

    hackdmembed = discord.Embed(
      title="That's SUCH an OOF lol 🤣",
      description=
      f"OOF, {member} has successfully been HACKED! What a noob... 😂",
      color=0x9a0404)

    await ctx.author.reply(embed=hackdmembed)


@bot.slash_command(aliases=["guild_count"])
async def server_count(ctx):
  await ctx.reply(
    f"Ascent is currently online and in {len(bot.guilds)} servers.")


@bot.slash_command(description="Send the lenny face in chat!")
async def lenny_face(ctx):
  await ctx.reply("( ͡° ͜ʖ ͡°)")


@bot.slash_command(description="Send the invisible character in chat!")
async def invisible_character(ctx):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.reply("⠀⠀⠀⠀⠀")


# KICK command
@bot.slash_command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.reply(
    f'{member} has been kicked by {ctx.message.author} for reason "{reason}"')


# BAN command
@bot.slash_command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(
    f'{member} has been BANNED! Rut row, I wonder why. Anyways, in order to get that user back, open Server Settings and UNBAN that user.'
  )


# server purging + clearing msgs
@bot.slash_command(aliases=["purge", "delete_msgs"])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
  await ctx.channel.purge(limit=amount)
  await ctx.send(
    f"```Rightio, {amount} message(s) have been DELETED... forever.```")


@bot.slash_command(name="guildinfo",
                   aliases=["serverinfo"],
                   help="Find info about the server!")
async def guildinfo(ctx):
  giembed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Server Data/Info",
                          color=discord.Color.blue())
  giembed.add_field(name="Server Created At:",
                    value=f"{ctx.guild.created_at}",
                    inline=True)
  giembed.add_field(name="Server Owner:",
                    value=f"{ctx.guild.owner}",
                    inline=True)
  giembed.add_field(name="Server Region:",
                    value=f"{ctx.guild.region}",
                    inline=False)
  giembed.add_field(name="Server ID:", value=f"{ctx.guild.id}", inline=True)
  await ctx.send(embed=giembed)


@bot.slash_command(help="I say what you say!")
async def echo(ctx, *, echo):
  await ctx.send(f"I repeat...\n\n{echo}")


@bot.slash_command()
async def help_secrets(ctx):
  async with ctx.typing():
    await asyncio.sleep(1)
  helpsecretsembed = discord.Embed(
    title="Ascent Easter Eggs!! 😲",
    description="You've used `bruh help_secret`.")
  helpsecretsembed.add_field(
    name="...I'm not going to tell you the SECRET easter eggs...",
    value="You have to find them yourself! :)",
    inline=False)
  helpsecretsembed.set_footer(
    text=
    "ID = 794618348289392680 | Fun Fact: use bruh clientid to find Ascent's ID!!"
  )
  await ctx.send(embed=helpsecretsembed)


# YT command
@bot.slash_command(aliases=["searchyt"])
async def youtube(ctx, *, search):
  query_string = urllib.parse.urlencode({'search_query': search})
  html_content = urllib.request.urlopen('https://www.youtube.com/results?' +
                                        query_string)
  search_results = re.findall(r"watch\?v=(\S{11})",
                              html_content.read().decode())

  await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


@bot.slash_command(aliases=["useravatar", "user_avatar", "get_the_avatar_of"],
                   usage="bruh avatar [that user you want the avatar from]")
async def avatar(ctx, member: discord.Member):
  await ctx.channel.send("Eh, the avatar? OK, getting it...")
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.channel.send(f"**{member}**'s current Discord profile picture:")
  userAvatar = member.avatar_url
  await ctx.channel.send(userAvatar)


# Slowmode Setting
@bot.slash_command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
  await ctx.channel.edit(slowmode_delay=seconds)
  await ctx.send(f"Slowmode in this channel is now {seconds}.")


# Internal calculator
@bot.slash_command(aliases=["+"], help="ADD NUMBERS!")
async def add(ctx, num1, num2):
  async with ctx.typing():
    await asyncio.sleep(1)
  ctx.reply(
    math.float(num1) + math.float(num2) +
    ", according to Ascent's internal calculator, is the correct answer...")


@bot.command(aliases=["-"], help="SUBTRACT NUMBERS!")
async def subtract(ctx, num1, num2):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.reply(
    float(num1) - float(num2) +
    ", according to Ascent's internal calculator, is the correct answer...")


@bot.command(aliases=["*"], help="MULTIPLY NUMBERS!")
async def multiply(ctx, left, right):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.reply(
    float(left) * float(right) +
    ", according to Ascent's internal calculator, is the correct answer...")


@bot.command(
  help=
  "ADD NUMBERS! (Note that using slash on this command will not work because of it intruding on Discord's regular Slash Command api.)"
)
async def divide(ctx, left, right):
  async with ctx.typing():
    await asyncio.sleep(1)
  await ctx.reply(
    float(left) / float(right) +
    ", according to Ascent's internal calculator, is the correct answer...")


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    return
  elif isinstance(error, commands.EmojiNotFound):
    await ctx.send("We couldn't find that emoji, please try again...")
  elif isinstance(error, discord.Forbidden):
    errorfembed = discord.Embed(
      title="An error occurred...",
      description=
      "I don't have the correct permissions to perform that command.")
    await ctx.reply(embed=errorfembed)
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(
      f"That command (the {str(error.cooldown.type).split('.')[-1]} command) is currently on cooldown. Please try again in a {error.retry_after:,.2f} seconds."
    )


bot.run(loginToken)
