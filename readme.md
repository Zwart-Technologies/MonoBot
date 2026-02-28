# MonoBot


> All-in-one Discord bot for your server, completely free and open source

[![Discord](https://img.shields.io/discord/1476313144120049797?style=flat&logo=discord&logoColor=white&label=Join%20the%20Discord&color=738ad6)](https://discord.gg/nc7n3qemf5)

## Prerequisites

- Python 3.8 or higher
- A Discord bot token from [Discord Developer Portal](https://discord.com/developers/applications)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MonoBot
   ```

2. Create a venv

   Linux / Macos
   ``` bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows
   ``` bat
   python3 -m venv venv
   venv/Scripts/Activate.bat
   pip install -r requirements.txt
   ```


3. **Run the setup script**

   Linux / Macos
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   
   This will guide you through configuring:
   - Discord bot token
   - Moderation role IDs
   - Logging channel ID
   - Counting channel ID
   
   Windows
   
   No setup script is currently available for windows, here are the steps to configure the bot:

   1. rename the config.example folder to config \
      ``` cmd
      move config.example config
      ```
   
   2. Set these values; `default` in `config/permissions.json` under moderation, `loggingchannel` in `config/logging.json` and `countingchannel` in `config/counting.json` 
   3. rename `.env.example` to `.env`: 
      ```  cmd
      move .env.example .env
      ```
   4. set your discord bot token in ./.env
      ``` .env
      TOKEN=your_discord_bot_token
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


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see [contributing.md](contributing.md) for guidelines.