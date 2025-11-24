#!/bin/bash

# ESLM UI Design Application - Stop Script

echo "Stopping ESLM UI Design Application..."

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
    # Try to find and kill vite process
    pkill -f "vite" 2>/dev/null && echo "Stopped vite process" || echo "No vite process found"
fi

# Clean up temp and cache files
echo "Cleaning up temporary and cache files..."

# Remove Vite cache
rm -rf node_modules/.vite 2>/dev/null && echo "  - Removed Vite cache"

# Remove build output
rm -rf dist 2>/dev/null && echo "  - Removed dist folder"

# Remove TypeScript build info
rm -f tsconfig.tsbuildinfo 2>/dev/null && echo "  - Removed TypeScript build info"

# Remove any .tmp files
find . -name "*.tmp" -type f -delete 2>/dev/null

# Remove any log files
rm -f *.log 2>/dev/null && echo "  - Removed log files"

echo "Cleanup complete!"
