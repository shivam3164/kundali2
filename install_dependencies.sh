#!/bin/bash

# STRICTLY CHECK CONDA ENVIRONMENT
if [ "$CONDA_DEFAULT_ENV" != "kundli_app" ]; then
    echo "❌ ERROR: Wrong Conda environment!"
    echo "You are currently in: '$CONDA_DEFAULT_ENV'"
    echo "You MUST be in 'kundli_app' to proceed."
    echo ""
    echo "Run the following command first:"
    echo "    conda activate kundli_app"
    echo ""
    exit 1
fi

echo "✅ Environment 'kundli_app' detected."

# Check if uv is installed (faster installer), otherwise use pip
if command -v uv &> /dev/null; then
    echo "🚀 using uv for faster installation..."
    uv pip install -r backend/requirements.txt
else
    echo "Using pip for installation..."
    pip install -r backend/requirements.txt
fi


echo "Installing Frontend Dependencies..."
cd frontend
if command -v npm &> /dev/null; then
    npm install
else
    echo "npm not found. Please install Node.js and npm to run the frontend."
fi
cd ..

echo "Installation complete."
