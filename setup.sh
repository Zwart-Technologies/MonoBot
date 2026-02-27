#!/bin/bash

echo "=== MonoBot Setup Script ==="
echo ""

# Create config directory if it doesn't exist
if [ ! -d "config" ]; then
    echo "Creating config directory..."
    mkdir -p config
    echo "✓ Config directory created"
else
    echo "✓ Config directory already exists"
fi

# Setup .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "Setting up .env file..."
    read -p "Enter your Discord bot token: " TOKEN
    echo "TOKEN=$TOKEN" > .env
    echo "✓ .env file created"
else
    echo ""
    read -p ".env file already exists. Do you want to replace it? (y/N): " REPLACE_ENV
    if [ "$REPLACE_ENV" = "y" ] || [ "$REPLACE_ENV" = "Y" ]; then
        read -p "Enter your Discord bot token: " TOKEN
        echo "TOKEN=$TOKEN" > .env
        echo "✓ .env file updated"
    else
        echo "✓ Keeping existing .env file"
    fi
fi

# Setup permissions.json
if [ ! -f "config/permissions.json" ]; then
    echo ""
    echo "Setting up permissions.json..."
    read -p "Enter default moderation role ID: " DEFAULT_ROLE
    read -p "Enter clear command role ID (press Enter to use default): " CLEAR_ROLE
    CLEAR_ROLE=${CLEAR_ROLE:-$DEFAULT_ROLE}
    
    cat > config/permissions.json << EOF
{
    "moderation": {
        "default": "$DEFAULT_ROLE",
        "clear": "$CLEAR_ROLE"
    }
}
EOF
    echo "✓ permissions.json created"
else
    echo ""
    read -p "config/permissions.json already exists. Do you want to replace it? (y/N): " REPLACE_PERM
    if [ "$REPLACE_PERM" = "y" ] || [ "$REPLACE_PERM" = "Y" ]; then
        read -p "Enter default moderation role ID: " DEFAULT_ROLE
        read -p "Enter clear command role ID (press Enter to use default): " CLEAR_ROLE
        CLEAR_ROLE=${CLEAR_ROLE:-$DEFAULT_ROLE}
        
        cat > config/permissions.json << EOF
{
    "moderation": {
        "default": "$DEFAULT_ROLE",
        "clear": "$CLEAR_ROLE"
    }
}
EOF
        echo "✓ permissions.json updated"
    else
        echo "✓ Keeping existing permissions.json"
    fi
fi

# Setup logging.json
if [ ! -f "config/logging.json" ]; then
    echo ""
    echo "Setting up logging.json..."
    read -p "Enter logging channel ID: " LOGGING_CHANNEL
    
    cat > config/logging.json << EOF
{
    "loggingchannel": $LOGGING_CHANNEL
}
EOF
    echo "✓ logging.json created"
else
    echo ""
    read -p "config/logging.json already exists. Do you want to replace it? (y/N): " REPLACE_LOG
    if [ "$REPLACE_LOG" = "y" ] || [ "$REPLACE_LOG" = "Y" ]; then
        read -p "Enter logging channel ID: " LOGGING_CHANNEL
        
        cat > config/logging.json << EOF
{
    "loggingchannel": $LOGGING_CHANNEL
}
EOF
        echo "✓ logging.json updated"
    else
        echo "✓ Keeping existing logging.json"
    fi
fi

# Setup counting.json
if [ ! -f "config/counting.json" ]; then
    echo ""
    echo "Setting up counting.json..."
    read -p "Enter counting channel ID: " COUNTING_CHANNEL
    
    cat > config/counting.json << EOF
{"countingchannel": $COUNTING_CHANNEL, "count": 0, "lastCountUser": 0}
EOF
    echo "✓ counting.json created"
else
    echo ""
    read -p "config/counting.json already exists. Do you want to replace it? (y/N): " REPLACE_COUNT
    if [ "$REPLACE_COUNT" = "y" ] || [ "$REPLACE_COUNT" = "Y" ]; then
        read -p "Enter counting channel ID: " COUNTING_CHANNEL
        
        cat > config/counting.json << EOF
{"countingchannel": $COUNTING_CHANNEL, "count": 0, "lastCountUser": 0}
EOF
        echo "✓ counting.json updated"
    else
        echo "✓ Keeping existing counting.json"
    fi
fi

# Make the script executable
chmod +x setup.sh

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "Your bot is configured with:"
echo "  • Environment variables in .env"
echo "  • Permissions config in config/permissions.json"
echo "  • Logging config in config/logging.json"
echo "  • Counting config in config/counting.json"
echo ""
echo "To start the bot, run: python -m src.main"
echo ""