.PHONY: all build inventory convert site report review test clean publish fetch-wayback fetch-php

RUN = uv run vecrescue
MATHJAX = vendor/mathjax-3.2.2
MATHJAX_SHA1 = c754d7b46a679d7f3fa03543d6b8bf124ddf9f6b

all build: $(MATHJAX)
	$(RUN) all

# MathJax, served from the site (#285): fetched once, checked against the npm
# registry's SHA-1, and only the parts the SVG output loads are kept.
$(MATHJAX):
	mkdir -p vendor && curl -sSL -o vendor/mathjax.tgz https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz
	echo "$(MATHJAX_SHA1)  vendor/mathjax.tgz" | shasum -c -
	rm -rf vendor/package && tar xzf vendor/mathjax.tgz -C vendor
	mkdir -p $@/input/tex
	cp vendor/package/es5/tex-svg.js $@/
	cp -R vendor/package/es5/input/tex/extensions $@/input/tex/
	cp -R vendor/package/es5/a11y vendor/package/es5/ui vendor/package/es5/sre $@/
	cp vendor/package/LICENSE $@/
	rm -rf vendor/package vendor/mathjax.tgz

inventory convert site report:
	$(RUN) $@

# Record the reviews ticked and signed in plans/pdf-review-checklist.md in the
# transcriptions' front matter; the next build shows "Reviewed by … on …".
review:
	$(RUN) review

test:
	uv run pytest -q

clean:
	rm -rf build

# Sources the restored PHP site holds and our tree lacks, and its article
# pages for comparison, into sources/php-site/ (#104). Polite and resumable.
fetch-php:
	$(RUN) fetch-php --renderings

# Recover captures from the Wayback Machine into sources/wayback/ (slow, polite,
# resumable; see surveys/wayback-survey.md). Needs build/inventory.json.
fetch-wayback:
	$(RUN) inventory
	$(RUN) fetch-wayback

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
