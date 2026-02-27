import discord
from discord.ext import commands
import src.config

class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int) -> None:
        print("clear recieved")
        perm = src.config.getModerationPermission("clear")
        guild = ctx.guild

        print("clear recieved 1")

        if not guild:
            await ctx.reply("This command is only usable in guilds")
            return

        author = await guild.fetch_member(ctx.author.id)
        minimumRole = await guild.fetch_role(int(perm))

        if not minimumRole or not author:
            return

        if author.top_role < minimumRole:
            await ctx.reply("You do not have permissions to do that")
            return

        if not isinstance(ctx.channel, discord.TextChannel):
            print("no text channel found")
            return

        await ctx.channel.purge(limit=amount+1)

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))