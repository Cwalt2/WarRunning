# Full path to Python from your virtual environment
PYTHON=/home/user/environment/bin/python3

# Full path to your main script
SCRIPT=/home/user/WarRunning/main.py

# Full path to your logs
LOG_DIR=/home/cwalt/WarRunning/logs
LOG_FILE=$LOG_DIR/auto_start_output.log

# Create logs directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Start the script with nohup in the background
nohup sudo "$PYTHON" "$SCRIPT" > "$LOG_FILE" 2>&1 &