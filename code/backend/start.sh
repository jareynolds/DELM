#!/bin/bash

# DELM - Design Experience Language Model - Start Script

echo "Starting DELM Server..."

cd "$(dirname "$0")"

# Check for virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if needed
if [ ! -f "venv/.installed" ]; then
    echo "Installing dependencies..."
    ./venv/bin/pip install -r requirements.txt
    touch venv/.installed
fi

# Seed database if empty
./venv/bin/python3 -c "
from src.vector_store import VectorStore
vs = VectorStore()
if vs.count() == 0:
    print('Seeding database...')
    from data.seed_patterns import seed_database
    from src.rag import RAGPipeline
    pipeline = RAGPipeline()
    seed_database(pipeline)
"

# Start the server
echo "Starting API server on http://127.0.0.1:3005"
./venv/bin/uvicorn src.api:app --host 127.0.0.1 --port 3005 --reload &

# Save PID
echo $! > .server.pid

echo "DELM server started with PID $(cat .server.pid)"
echo ""
echo "API Endpoints:"
echo "  POST /generate  - Generate UI components"
echo "  POST /patterns  - Add design patterns"
echo "  POST /search    - Search patterns"
echo "  GET  /health    - Health check"
