import discord
from discord.ext import commands
from typing import Optional
import src.config

class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int) -> None:
        guild = ctx.guild


        if not guild:
            await ctx.reply("This command is only usable in guilds")
            return

        if not await isUserAllowedToUseCommand(ctx, "clear"):
            await ctx.reply("You do not have permissions to do that")
            return

        if not isinstance(ctx.channel, discord.TextChannel):
            return

        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    async def setnick(self, ctx: commands.Context, nick: str, user: Optional[discord.User]):
        guild = ctx.guild
        if guild is None:
                await ctx.reply("This command is only usable in guilds")
                return
        
        if not await isUserAllowedToUseCommand(ctx, "setnick"):
            await ctx.reply("You do not have permissions to do that")
            return
        
        if user is None:
            member = await guild.fetch_member(ctx.author.id)
            if member is None:
                return
            
            if not isinstance(member, discord.Member):
                await ctx.reply("User not found")
                return

            await member.edit(nick=nick)
            await ctx.message.add_reaction("✅")
        else:
            member = await guild.fetch_member(user.id)
            if not member:
                await ctx.reply("User not found")
                return
            
            await member.edit(nick=nick)
            await ctx.message.add_reaction("✅")

    @commands.command()
    async def ban(self, ctx: commands.Context, user: discord.User, reason: Optional[str]):
        print("ban request received")
        guild = ctx.guild
        if guild is None:
                await ctx.reply("This command is only usable in guilds")
                return
        
        if not await isUserAllowedToUseCommand(ctx, "ban"):
            await ctx.reply("You do not have permissions to do that")
            return
        
        member = await guild.fetch_member(user.id)
        if not member:
            await ctx.reply("User not found")
            return
        
        await member.ban(reason=reason)
        await ctx.message.add_reaction("✅")


    @commands.command()
    async def unban(self, ctx: commands.Context, user: discord.User):
        guild = ctx.guild
        if guild is None:
                await ctx.reply("This command is only usable in guilds")
                return
        
        if not await isUserAllowedToUseCommand(ctx, "unban"):
            await ctx.reply("You do not have permissions to do that")
            return
        
        await guild.unban(user)
        await ctx.message.add_reaction("✅")
    
    @commands.command()
    async def kick(self, ctx: commands.Context, user: discord.User, reason: Optional[str]):
        guild = ctx.guild
        if guild is None:
                await ctx.reply("This command is only usable in guilds")
                return
        
        if not await isUserAllowedToUseCommand(ctx, "kick"):
            await ctx.reply("You do not have permissions to do that")
            return
        
        member = await guild.fetch_member(user.id)
        if not member:
            await ctx.reply("User not found")
            return
        
        await member.kick(reason=reason)
        await ctx.message.add_reaction("✅")

    @commands.command()
    async def vkick(self, ctx: commands.Context, user: discord.User, reason: Optional[str]):
        guild = ctx.guild
        if guild is None:
                await ctx.reply("This command is only usable in guilds")
                return
        
        if not await isUserAllowedToUseCommand(ctx, "vkick"):
            await ctx.reply("You do not have permissions to do that")
            return
        
        member = await guild.fetch_member(user.id)
        if not member:
            await ctx.reply("User not found")
            return
        
        if member.voice != None:
            if member.voice.channel != None:
                await member.move_to(None, reason=reason)
                await ctx.message.add_reaction("✅")
        
async def isUserAllowedToUseCommand(ctx: commands.Context, permission: str) -> bool:
    guild = ctx.guild
    if guild is None:
            return False
    
    perm = src.config.getModerationPermission(permission)
    if not perm:
        return False
    
    minimumRole = guild.get_role(int(perm))
    if minimumRole is None:
        try:
            minimumRole = await guild.fetch_role(int(perm))
        except (discord.NotFound, discord.HTTPException):
            return False
        
    if not minimumRole:
        return False
    
    ctxAuthor = guild.get_member(ctx.author.id)
    if ctxAuthor is None:
        try:
            ctxAuthor = await guild.fetch_member(ctx.author.id)
        except (discord.NotFound, discord.HTTPException):
            return False
        
    if not ctxAuthor:
        return False
    
    if ctxAuthor.top_role < minimumRole:
        return False
    
    return True

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))