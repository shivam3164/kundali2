#!/bin/bash

# STRICTLY CHECK CONDA ENVIRONMENT
if [ "$CONDA_DEFAULT_ENV" != "kundli_app" ]; then
    echo "❌ ERROR: Wrong Conda environment!"
    echo "You are currently in: '$CONDA_DEFAULT_ENV'"
    echo "You MUST be in 'kundli_app' to proceed."
    echo "Run: conda activate kundli_app"
    exit 1
fi

# Function to kill background processes on exit
trap 'kill $(jobs -p)' EXIT

echo "Starting Backend Server..."
cd backend
# Ensure we are in the correct directory for python path
# backend/app/main.py -> module app.main
uvicorn app.main:app --reload --host 0.0.0.0 --port 8002 &
BACKEND_PID=$!
cd ..

echo "Waiting for Backend to initialize..."
sleep 5

echo "Starting Frontend..."
cd frontend
if command -v npm &> /dev/null; then
    # Use PORT 4000 to avoid conflicts with other running apps (like local_causalities on 3000)
    PORT=4000 BROWSER=none npm start &
    FRONTEND_PID=$!
    cd ..
    
    echo "App is running."
    echo "Backend: http://localhost:8002"
    echo "Frontend: http://localhost:4000"
    
    wait $BACKEND_PID $FRONTEND_PID
else
    echo "npm not found. Frontend cannot start."
    kill $BACKEND_PID
fi
