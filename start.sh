#!/bin/bash
# Kundali App - Single Launch Script
# Starts both backend and frontend with proper environment

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
CONDA_ENV="kundli_app"
CONDA_PYTHON="/Users/uddalakdatta/miniconda3/envs/${CONDA_ENV}/bin/python"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Starting Kundali Application...${NC}"

# Check if conda environment exists
if [ ! -f "$CONDA_PYTHON" ]; then
    echo -e "${RED}❌ Error: Conda environment '${CONDA_ENV}' not found${NC}"
    echo -e "${YELLOW}Please create it with: conda create -n ${CONDA_ENV} python=3.11${NC}"
    exit 1
fi

# Function to cleanup background processes on exit
cleanup() {
    echo -e "\n${YELLOW}🛑 Shutting down services...${NC}"
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null || true
    fi
    echo -e "${GREEN}✅ All services stopped${NC}"
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start Backend
echo -e "${GREEN}📡 Starting Backend (port 8002)...${NC}"
cd "$PROJECT_ROOT/backend"
$CONDA_PYTHON -m uvicorn app.main:app --port 8002 --reload --host 0.0.0.0 &
BACKEND_PID=$!

# Wait for backend to be ready
echo -e "${YELLOW}⏳ Waiting for backend to initialize...${NC}"
sleep 3

# Check if backend started successfully
if ! kill -0 $BACKEND_PID 2>/dev/null; then
    echo -e "${RED}❌ Backend failed to start${NC}"
    exit 1
fi

# Start Frontend
echo -e "${GREEN}🎨 Starting Frontend (port 3000)...${NC}"
cd "$PROJECT_ROOT/frontend"
npm start &
FRONTEND_PID=$!

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ✅ Kundali App is running!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "  ${YELLOW}Frontend:${NC}  http://localhost:3000"
echo -e "  ${YELLOW}Backend:${NC}   http://localhost:8002"
echo -e "  ${YELLOW}API Docs:${NC}  http://localhost:8002/docs"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "  Press ${RED}Ctrl+C${NC} to stop all services"
echo ""

# Wait for any process to exit
wait
