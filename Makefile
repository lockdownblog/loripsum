POETRY=poetry
POETRY_RUN=$(POETRY) run

SOURCE_FILES=$(shell find . -path "./loripsum/*.py")
SOURCES_FOLDER=loripsum

BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

check_on_main:
ifeq ($(BRANCH),main)
	echo "You are good to go!"
else
	$(error You are not in the main branch)
endif

patch: check_on_main
	$(POETRY_RUN) bumpversion patch --verbose
	git push --follow-tags

minor: check_on_main
	$(POETRY_RUN) bumpversion minor --verbose
	git push --follow-tags

major: check_on_main
	$(POETRY_RUN) bumpversion major --verbose
	git push --follow-tags

style:
	$(POETRY_RUN) isort $(SOURCES_FOLDER)
	$(POETRY_RUN) black $(SOURCE_FILES)

lint:
	$(POETRY_RUN) isort $(SOURCES_FOLDER) --check-only
	$(POETRY_RUN) black $(SOURCE_FILES) --check

test-unit:
	PYTHONPATH=. $(POETRY_RUN) pytest -vv test/unit

test-end-to-end:
	PYTHONPATH=. $(POETRY_RUN) pytest -vv test/end_to_end

.PHONY: test
