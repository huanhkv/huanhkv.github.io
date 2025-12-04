.PHONY: help install build serve clean rebuild all

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON := uv run python
BACKEND_DIR := backend
DIST_DIR := frontend/dist
PORT := 8000
PYTHON_VENV := $(BACKEND_DIR)/.venv/bin/python

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Reideen's Blog - Build System$(NC)"
	@echo ""
	@echo "$(GREEN)Available targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""

install: ## Install dependencies using uv
	@echo "$(BLUE)📦 Installing dependencies...$(NC)"
	@cd $(BACKEND_DIR) && uv sync
	@echo "$(GREEN)✓ Dependencies installed!$(NC)"

build: ## Build the static site
	@echo "$(BLUE)🚀 Building Reideen's Blog...$(NC)"
	@echo ""
	@cd $(BACKEND_DIR) && $(PYTHON) -m builder
	@echo ""
	@echo "$(GREEN)✨ Build complete!$(NC)"
	@echo ""

serve: build ## Build and serve the site locally
	@echo "$(BLUE)🌐 Starting local server...$(NC)"
	@echo ""
	@echo "$(GREEN)Visit: http://localhost:$(PORT)$(NC)"
	@echo "$(YELLOW)Press Ctrl+C to stop$(NC)"
	@echo ""
	@$(PYTHON_VENV) -m http.server $(PORT) --directory $(DIST_DIR)

clean: ## Clean the build output
	@echo "$(YELLOW)🧹 Cleaning build output...$(NC)"
	@rm -rf $(DIST_DIR)/*
	@echo "$(GREEN)✓ Clean complete!$(NC)"

rebuild: clean build ## Clean and rebuild

all: clean install build serve
