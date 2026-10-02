.PHONY: all inventory convert site report test clean

RUN = uv run vecrescue

all:
	$(RUN) all

inventory convert site report:
	$(RUN) $@

test:
	uv run pytest -q

clean:
	rm -rf build
