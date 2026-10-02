Vector Rescue
=============

The British APL Association (BAA) was founded at Imperial College, London, in 1980 but is now largely inactive.

https://britishaplassociation.org

Its domain vector.org.uk holds its journal *Vector* as a WordPress site. 

The previous version of its website, handbuilt in PHP, XML and XHTML, should be available at archive.vector.org.uk, but the URL now seems to point to the WordPress site, breaking inbound links such as (from nsl.com)

http://vector.johnbutlerassociates.co.uk/art10500650


and its original URL

http://vector.org.uk/art10500650

and 

http://archive.vector.org.uk/art10500650

The BAA does not appear to have capacity to maintain the valuable archive. The latest issue of *Vector* is dated 2022.

This project aims to recover and publish the entire Vector archive and publish it. 


Target environment
------------------

Candidates:

-   Dyalog has offered to host the site; the project could live on its Gitea server.
-   As a public resource this could live on GitHub, published via GitHub Pages


Resources
---------

1.  The filetree that the PHP site served. From memory: the article bodies were stored as XHTML fragments that the PHP wrapped in chrome using an XML index to the archive. The XHTML was encoded as UTF-8.
2.  An export of the WordPress database. This will contain articles published since the WP site went live, completing the archive as publication has ended.
3.  Control of the archive.vector.org.uk DNS -- presumed with Jake.

### Old Microsoft Word documents

*Vector* was for 20 years published as a printed journal, assembled from Microsoft Word documents. Before Unicode, a variety of mappings and fonts were used to represent the APL code. 

Ian Clark worked for years to convert the DOCs to Unicode. If the filetree holds them, they are a potential source of articles never republished online.


### Potential sources

-   John “Jake” Jacob, current editor of *Vector*
-   Paul Grosvenor, chair of the BAA 
-   Stephen Taylor, previous editor of *Vector*, who converted it to online publication and designed and built the PHP site.


Decisions and status
--------------------

1.  **Sources.** Retrieving them is the first step. Paul Grosvenor has been emailed to ask what he can supply.
2.  **First deliverable.** A survey of what has been retrieved.
3.  **Hosting.** Open. The `art` URLs are essential. If neither Gitea nor GitHub Pages can handle them cleanly, a less generic solution is acceptable, for example hosting behind HTTPD on dyalog.com.
4.  **URLs.** Restoring the old `art` URLs exactly is the top priority.
5.  **WordPress overlap.** WP articles duplicate some old-site articles. Diffs will be examined before ruling, and the choice may be made article by article.
6.  **Pre-Unicode APL.** Mapping pre-Unicode Word sources to Unicode is in scope.


Project structure
-----------------

	plans/          plans for the project
	progress/       daily record of work done
	reviews/        reviews of tests and implementations, 
	                and responses to them
    sources/        recovered files from which to work (read-only)




Pipeline
--------

The conversion is a rerunnable pipeline (Python, managed with `uv`). It reads `sources/sjt/Vector` and never writes there; everything it produces goes in `build/`, which is not committed.

    make test        # run the tests
    make all         # inventory → convert → site → report
    make inventory   # build/inventory.json from index.xml
    make convert     # build/docs/art<ID>.md
    make site        # build/site with Zensical
    make report      # build/report.md: checks every page against its source
    make publish     # push build/site to the gh-pages branch (development review)
    make fetch-wayback  # recover captures from the Wayback Machine into sources/wayback/

The run report compares the visible text and every code block of each built page with its source, and summarises what passed through as raw HTML and why. Each run keeps the previous report (`build/report.prev.json`) and shows the change, so a revised rule can be measured against the last run.

Conversion rules are provisional and tracked as GitHub issues. Each rule is written test-first; an element without a rule passes through as raw HTML so nothing is lost.
