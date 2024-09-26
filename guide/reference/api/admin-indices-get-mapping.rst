
=================
 Get Mapping API 
=================




—-
layout: guide
title: Get Mapping API
cat: guide
sidebar: reference\_api
—-

The get mapping API allows to retrieve mapping definition of index or
index/type.

::

    $ curl -XGET 'http://localhost:9200/twitter/tweet/_mapping’

Multiple Indices and Types
==========================

The get mapping API can be used to get more than one index or type
mapping with a single call. General usage of the API follows the
following syntax: ``host:port/{index}/{type}/_mapping`` where both
``{index}`` and ``{type}`` can stand for comma-separated list of names.
To get mappings for all indices you can use ``_all`` for ``{index}``.
The following are some examples:

::

    $ curl -XGET 'http://localhost:9200/twitter,kimchy/_mapping’

        $ curl -XGET 'http://localhost:9200/_all/tweet,book/_mapping’

If you want to get mappings of all indices and types then the following
two examples are equivalent:

::

    $ curl -XGET 'http://localhost:9200/_all/_mapping’

        $ curl -XGET 'http://localhost:9200/_mapping’




