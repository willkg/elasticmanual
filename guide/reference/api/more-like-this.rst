
====================
 More Like This API 
====================




—-
layout: guide
title: More Like This API
cat: guide
sidebar: reference\_api
—-

The more like this (mlt) API allows to get documents that are “like” a
specified document. Here is an example:

::

    $ curl -XGET 'http://localhost:9200/twitter/tweet/1/_mlt?mlt_fields=tag,content&min_doc_freq=1’

The API simply results in executing a search request with
`moreLikeThis </guide/reference/query-dsl/mlt-query.html>`_ query (http
parameters match the parameters to the ``more_like_this`` query). This
means that the body of the request can optionally include all the
request body options in the `search API </guide/reference/api/search/>`_
(facets, from/to and so on).

Rest parameters relating to search are also allowed, including
``search_type``, ``search_indices``, ``search_types``,
``search_scroll``, ``search_size`` and ``search_from``.

When no ``mlt_fields`` are specified, all the fields of the document
will be used in the ``more_like_this`` query generated.



