
==================================
 Search API – Indices And Types 
==================================




—-
layout: guide
title: Search API – Indices And Types
cat: guide
sidebar: reference\_api\_search
—-

The search API can be applied to multiple types within an index, and
across multiple indices. For example, we can search on all documents
across all types within the twitter index:

::

    $ curl -XGET 'http://localhost:9200/twitter/_search?q=user:kimchy’

We can also search within specific types:

::

    $ curl -XGET 'http://localhost:9200/twitter/tweet,user/_search?q=user:kimchy’

We can also search all tweets with a certain tag across several indices
(for example, when each user has his own index):

::

    $ curl -XGET 'http://localhost:9200/kimchy,elasticsearch/tweet/_search?q=tag:wow’

Or we can search all tweets across all available indices using ``_all``
placeholder:

::

    $ curl – XGET 'http://localhost:9200/_all/tweet/_search?q=tag:wow’

Or even search across all indices and all types:

::

    $ curl -XGET 'http://localhost:9200/_search?q=tag:wow’




