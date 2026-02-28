# Contributing to MonoBot

Thank you for your interest in contributing to MonoBot! We welcome contributions from everyone. This document provides guidelines and instructions for contributing to the project.

## Getting Started

1. **Choose what to do**:
   You can think of something to contribute yourself or do something on the [todo list](todo.md)

2. **Fork the repository** on GitHub
3. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/MonoBot.git
   cd MonoBot
   ```
4. **Create a virtual environment** and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- Use meaningful variable and function names
- Keep lines under 100 characters when possible

### AI Usage

AI tools (such as GitHub Copilot) are permitted in your contributions. However, please ensure that:
- Generated code is readable and maintainable
- You understand all code you submit
- The code doesn't compromise code quality or security
- Pull requests with unreadable or unmaintainable AI-generated code will not be accepted

### Testing

- Test your changes locally with a test Discord server
- Ensure the bot starts without errors: `python -m src.main`
- Test all affected features manually

### Commit Messages

Use clear, descriptive commit messages:
```
feat: add new counting game feature
fix: resolve issue with join logging
docs: update installation instructions
```

Use these prefixes:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Test additions/modifications

## Adding New Features

1. **Create a new cog** in `src/cogs/` following the existing structure
2. **Register the cog** in `src/main.py`
3. **Add configuration** to `config/` if needed
4. **Document** your feature in the README
5. **Test thoroughly** before submitting

### Cog Structure

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mycommand(self, ctx):
        """Description of what the command does"""
        # Implementation

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

## Submitting Changes

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
2. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference any related issues (e.g., "Fixes #123")
3. **Respond to feedback** from reviewers

## Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Any error messages or logs

## Questions?

Feel free to ask questions by opening an issue or starting a discussion. We're here to help!

## License

By contributing to MonoBot, you agree that your contributions will be licensed under its GNU General Public License v3.0.

Thank you for helping make MonoBot better!
