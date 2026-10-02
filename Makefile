.PHONY: all inventory convert site report test clean publish

RUN = uv run vecrescue

all:
	$(RUN) all

inventory convert site report:
	$(RUN) $@

test:
	uv run pytest -q

clean:
	rm -rf build

# Push build/site to the gh-pages branch of origin, for development review.
# One commit, force-pushed: the branch holds nothing but the latest build.
# x-extensionless is a copy of an article page with no extension, to test
# whether GitHub Pages serves such a file as HTML (exact /art<ID> URLs).
REMOTE = $(shell git remote get-url origin)
publish:
	rm -rf build/publish && cp -R build/site build/publish
	touch build/publish/.nojekyll
	cp build/publish/art10500650/index.html build/publish/x-extensionless
	cd build/publish && git init -q -b gh-pages && git add -A \
	  && git commit -q -m "Development build" && git push -q -f $(REMOTE) gh-pages
	rm -rf build/publish
