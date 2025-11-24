#!/bin/bash

# ESLM UI Design Application - Start Script

echo "Starting ESLM UI Design Application..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

# Start the development server
echo "Starting development server on http://localhost:5174"
npm run dev &

# Save the PID for stop script
echo $! > .server.pid

echo "Server started with PID $(cat .server.pid)"
echo "Access the application at http://localhost:5174"
