# MonoBot


> All-in-one Discord bot for your server, completely free and open source

[![Discord](https://img.shields.io/discord/1476313144120049797?style=flat&logo=discord&logoColor=white&label=Join%20the%20Discord&color=738ad6)](https://discord.gg/nc7n3qemf5)

## Features

- **Counting Game** - Collaborative counting channel where users take turns incrementing a number
- **Join Logging** - Track which invite users join through with detailed logging
- **Moderation** - Clear messages with role-based permission control
- **Extensible Cogs System** - Easy to add new features

## Prerequisites

- Python 3.8 or higher
- A Discord bot token from [Discord Developer Portal](https://discord.com/developers/applications)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MonoBot
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   
   This will guide you through configuring:
   - Discord bot token
   - Moderation role IDs
   - Logging channel ID
   - Counting channel ID

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the bot:
```bash
python -m src.main
```

## Configuration

All configuration is stored in the config directory:

- **permissions.json** - Role IDs for moderation commands
- **logging.json** - Channel ID for join logs
- **counting.json** - Channel ID and state for counting game

## Commands

- `!ping` - Check if the bot is online
- `!clear <amount>` - Delete messages (requires moderation role)

## Project Structure

```
src/
├── main.py           # Bot entry point
├── config.py         # Configuration management
└── cogs/
    ├── counting.py   # Counting game cog
    ├── joinLogging.py # Join log tracking cog
    └── moderation.py # Moderation commands cog
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see [contributing.md](contributing.md) for guidelines.