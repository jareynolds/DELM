#!/bin/bash

# DELM - Stop Script

echo "Stopping DELM Server..."

cd "$(dirname "$0")"

# Kill the server process
if [ -f .server.pid ]; then
    PID=$(cat .server.pid)
    if ps -p $PID > /dev/null 2>&1; then
        kill $PID
        echo "Stopped server process $PID"
    else
        echo "Server process $PID not running"
    fi
    rm .server.pid
else
    pkill -f "uvicorn src.api:app" 2>/dev/null && echo "Stopped uvicorn process" || echo "No uvicorn process found"
fi

# Clean up cache files
echo "Cleaning up cache files..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
rm -rf .pytest_cache 2>/dev/null
echo "Cleanup complete!"
