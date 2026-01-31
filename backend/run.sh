#!/bin/bash
# Run the Kundali API server

cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "../.venv" ] && [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    if [ -d "../.venv" ]; then
        source ../.venv/bin/activate
    else
        source .venv/bin/activate
    fi
fi

# Set PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Run the server
echo "Starting Kundali API server..."
echo "API docs available at: http://localhost:8000/api/v1/docs"
echo ""

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
