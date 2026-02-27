import discord, src.config
from discord.ext import commands

class Counting(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        global count, lastCountUser, countingChannel
        count = int(src.config.getCounting("count"))
        lastCountUser = int(src.config.getCounting("lastCountUser"))
        countingChannel = int(src.config.getCounting("countingchannel"))
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        global count, lastCountUser
        
        # Process commands for all channels
        await self.bot.process_commands(message)
        
        # Only handle counting game in the counting channel
        if message.channel.id != countingChannel:
            return

        if message.content.isdigit() and message.content == str(count + 1) and message.author.id != lastCountUser:
            count += 1
            lastCountUser = message.author.id
            src.config.saveCounting(count, lastCountUser)
            await message.add_reaction("✅")
        elif message.content.isdigit():
            await message.add_reaction("❌")
            channel = self.bot.get_channel(countingChannel)
            if not isinstance(channel, discord.TextChannel):
                return
            await channel.send(f"{message.author} broke the chain at {count}, start again at 1")
            lastCountUser = 0
            count = 0
            src.config.saveCounting(count, lastCountUser)

async def setup(bot: commands.Bot):
    await bot.add_cog(Counting(bot))