.PHONY: start test install

# Default port for the application
PORT ?= 8000

# Start the FastAPI application
start:
	uvicorn main:app --reload --port $(PORT)

# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	pytest tests/

# Help command to show available commands
help:
	@echo "Available commands:"
	@echo "  make start      - Start the FastAPI application with hot reload"
	@echo "  make install    - Install Python dependencies"
	@echo "  make test       - Run tests"
	@echo "  make help       - Show this help message"
	@echo ""
	@echo "Options:"
	@echo "  PORT           - Port to run the application (default: 8000)"
	@echo "                   Example: make start PORT=3000" 