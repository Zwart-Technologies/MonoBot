import discord, dotenv, os, asyncio, src.config, signal
from discord.ext import commands


dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx: commands.Context):
    if ctx.author.bot:
        return
    await ctx.reply("pong")

async def main():
    src.config.LoadPermissions()
    src.config.LoadLogging()
    src.config.LoadCounting()
    await bot.load_extension("src.cogs.moderation")
    await bot.load_extension("src.cogs.joinLogging")
    await bot.load_extension("src.cogs.counting")
    await bot.start(str(os.getenv("TOKEN")))

async def shutdown():
    print("Shutting down...")
    
    # Close database connections here
    # await db.close()

    await bot.close()
    print("Bot shutdown complete.")

def handle_signal():
    asyncio.create_task(shutdown())

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, handle_signal)
    
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()