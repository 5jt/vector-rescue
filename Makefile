.PHONY: all inventory convert site test clean

RUN = uv run vecrescue

all:
	$(RUN) all

inventory convert site:
	$(RUN) $@

test:
	uv run pytest -q

clean:
	rm -rf build
