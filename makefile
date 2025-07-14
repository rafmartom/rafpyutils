.PHONY: help all clean test setup-repo 

.DEFAULT_GOAL := all

help:
	@echo "Project Build Targets:"
	@echo "  all         - Compile the project"
	@echo "  clean       - Remove build artifacts"
	@echo ""
	@echo "Repository Operations:"
	@echo "  test        - Run tests"
	@echo "  setup-repo  - Configure repository Localy"
	@echo ""
	@echo "Miscellaneous:"
	@echo "  help        - Show this help"
	@echo ""


## ----------------------------------------------------------------------------
# @section PROJECT_TARGETS

all:
	@echo "[all] No build steps defined yet."
clean:
	@echo "[clean] No cleanup needed (no build artifacts)."

## EOF EOF EOF PROJECT_TARGETS
## ----------------------------------------------------------------------------


## ----------------------------------------------------------------------------
# @section REPOSITORY_MANAGEMENT

test: all
	@python3 -m unittest discover tests

setup-repo:
	@echo "#!/bin/sh\nmake test" > .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit

## EOF EOF EOF REPOSITORY_MANAGEMENT
## ----------------------------------------------------------------------------
