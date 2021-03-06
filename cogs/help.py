import discord
from discord.ext import commands

import time
from discord.ext.commands import errors, converter


class Help:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="help", aliases=['cmds'])
    async def _help(self, ctx, l:str = None, cmd:str = None):
        """This Command."""
        if ctx.message.author.bot: return
        elif not l:            
            embed = discord.Embed(description="**What can I help you with?**\n\n> **For help with a module**.. `siri help module|mdl <module>`\n> **For help with a command**.. `siri help command|cmd <command>`")
            embed.add_field(name="Current Modules..", value="`help`  `utility`  `crypto`  `bot`  `economy`")
            embed.set_footer(text="Siri | NOT affiliated with Apple", icon_url="https://vignette.wikia.nocookie.net/logopedia/images/d/d0/Siri.png/revision/latest?cb=20170730135120")
            embed.set_image(url="http://media.idownloadblog.com/wp-content/uploads/2016/06/iOS-10-Siri-waveform-image-001.png")
            await ctx.send(embed=embed)

        elif l == "Command" or l == "command" or l == "cmd":
            if not cmd:
                await ctx.send("<:WrongMark:473277055107334144> Please include the command name.")
            else:
                try:
                    _cmd = self.bot.get_command(cmd)
                    _help = "> <".join(_cmd.clean_params)
                    help = _help
                    h1 = _cmd.help
                    h2 = h1.replace("<>", "")
                    if _cmd.help is None:
                        embed2 = discord.Embed(description=f"> **Command:** `{cmd}`\n\n```siri {_cmd} <{help}>\n\nNo Description yet.```") 
                    else:
                        embed2 = discord.Embed(description=f"> **Command:** `{cmd}`\n\n```siri {_cmd} <{help}>\n\n{h2}```")
                    embed2.set_author(name="Siri", icon_url="https://vignette.wikia.nocookie.net/logopedia/images/d/d0/Siri.png/revision/latest?cb=20170730135120")
                    await ctx.send(embed=embed2)
                except:
                    await ctx.send(f"<:WrongMark:473277055107334144> No command called \"{cmd}\" found.")

        elif l == "Module" or l == "module" or l == "mdl":

            if cmd == "Utility" or cmd == "utility":
                modules = ["`article`", "`avatar`", "`chatbot`", "`colour`", "`define`","`discordstatus`", "`hastebin`","`IMDb`","`langdetect`", "`map`", "`news`","`shorten`", "`search`","`serverinfo`", "`userinfo`","`strawpoll`","`ticket`", "`translate`", "`weather`", "`wikipedia`"]
                name = "Utility"
                d = "Utility Commands"
            elif cmd == "Help" or cmd == "help":
                modules = ["`help`"]
                name = "Help"
                d = "Help Menu"
            elif cmd == "Crypto" or cmd == "crypto":
                modules = ["`btc`", "`ethereum`", "`litecoin`", "`ripple`"]
                name = "Crypto"
                d = "Get current crypto stats"
            elif cmd == "Bot" or cmd == "bot":
                modules = ["`servers`", "`stats`", "`support`", "`ping`"]
                name = "Bot"
                d = "Bot info/stats"
            elif cmd == "Economy" or cmd == "economy":
                modules = ["`balance`", "`bank create`", "`birthday`", "`buy`","`daily`", "`description`", "`eat`","`give`", "`profile`", "`setcolour`", "`shop`"]
                name = "Economy"
                d = "Economy Commands"
            else:
                return await ctx.send(f"<:WrongMark:473277055107334144> No module called \"{cmd}\" found.")

            try:
                md = " ".join(modules)
                embed3 = discord.Embed(description=f"> **Module:** `{name}`\n> **Description:** `{d}`\n> **Commands:** {md}")
                embed3.set_author(name="Siri", icon_url="https://vignette.wikia.nocookie.net/logopedia/images/d/d0/Siri.png/revision/latest?cb=20170730135120")
                await ctx.send(embed=embed3)
            except:
                pass
        else:
            pass

def setup(bot):
    bot.add_cog(Help(bot))
