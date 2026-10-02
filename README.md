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

### Old Microsoft Word documents

*Vector* was for 20 years published as a printed journal, assembled from Microsoft Word documents. Before Unicode, a variety of mappings and fonts were used to represent the APL code. 

Ian Clark worked for years to convert the DOCs to Unicode. If the filetree holds them, they are a potential source of articles never republished online.


### Potential sources

-   John “Jake” Jacob, current editor of *Vector*
-   Paul Grosvenor, chair of the BAA 
-   Stephen Taylor, previous editor of *Vector*, who converted it to online publication and designed and built the PHP site.
-   