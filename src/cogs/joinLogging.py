import discord
from discord.ext import commands
import src.config

invite_cache = {}

class JoinLogging(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Cache invites when the bot starts"""
        for guild in self.bot.guilds:
            try:
                invites = await guild.invites()
                invite_cache[guild.id] = {invite.code: invite.uses for invite in invites}
                print(f"Cached {len(invites)} invites for {guild.name}")
            except discord.Forbidden:
                print(f"Missing permissions to view invites in {guild.name}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print("member joined")
        guild = member.guild
        try:
            new_invites = await guild.invites()
        except discord.Forbidden:
            print(f"Missing permissions to view invites in {guild.name}")
            return

        old_invites = invite_cache.get(guild.id, {})

        print("checking invites")

        loggingChannelId = int(src.config.getLogging("loggingchannel"))
            
        channel = guild.get_channel(loggingChannelId)
        if not isinstance(channel, discord.TextChannel):
            return

        print("checking invites 1")

        for invite in new_invites:
            if invite.code in old_invites:
                if invite.uses > old_invites[invite.code]:                    
                    await channel.send(f"{member} joined using invite {invite.code} created by {invite.inviter}")
            else:
                await channel.send(f"{member} joined using a new invite {invite.code} created by {invite.inviter}")

        print("checking invites 2")
        # Update the cache
        invite_cache[guild.id] = {invite.code: invite.uses for invite in new_invites}

async def setup(bot: commands.Bot):
    await bot.add_cog(JoinLogging(bot))