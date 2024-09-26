
=======================
 Search API – Facets 
=======================




—-
layout: guide
title: Search API – Facets
cat: guide
sidebar: reference\_api\_search\_facets
—-

The usual purpose of a full-text search engine is to return a small
number of documents matching your query.

*Facets* provide aggregated data based on a search query. In the
simplest case, a `terms
facet </guide/reference/api/search/facets/terms-facet.html>`_ can return
*facet counts* for various *facet values* for a specific *field*.
ElasticSearch supports more more facet implementations, such as
`statistical </guide/reference/api/search/facets/statistical-facet.html>`_
or `date
histogram </guide/reference/api/search/facets/date-histogram-facet.html>`_
facets.

The field used for facet calculations *must* be of type numeric,
date/time or be analyzed as a single token — see the
`*Mapping* </guide/reference/mapping/index.html>`_ guide for details on
the analysis process.

You can give the facet a custom *name* and return multiple facets in one
request.

Let’s try it out with a simple example. Suppose we have a number of
articles with a field called ``tags``, preferably analyzed with the
`keyword </guide/reference/index-modules/analysis/keyword-analyzer.html>`_
analyzer. The facet aggregation will return counts for the most popular
tags across the documents matching your query — or across all documents
in the index.

We will store some example data first:

::

    curl -X DELETE “http://localhost:9200/articles”
    curl -X POST “http://localhost:9200/articles/article” -d '{“title” : “One”,   “tags” : [“foo”]}’
    curl -X POST “http://localhost:9200/articles/article” -d '{“title” : “Two”,   “tags” : [“foo”, “bar”]}’
    curl -X POST “http://localhost:9200/articles/article” -d '{“title” : “Three”, “tags” : [“foo”, “bar”, “baz”]}’

Now, let’s query the index for articles beginning with letter “T” and
retrieve a `*terms
facet* </guide/reference/api/search/facets/terms-facet.html>`_ for the
``tags`` field. We will name the facet simply: *tags*.

::

    curl -X POST “http://localhost:9200/articles/_search?pretty=true” -d '
      {
        “query” : { “query_string” : {“query” : “T*”} },
        “facets” : {
          “tags” : { “terms” : {“field” : “tags”} }
        }
      }
    '

This request will return articles “Two” and “Three” (because they match
our query), as well as the ``tags`` facet:

::

    “facets” : {
      “tags” : {
        “_type” : “terms”,
        “missing” : 0,
        “total”: 5,
        “other”: 0,
        “terms” : [ {
          “term” : “foo”,
          “count” : 2
        }, {
          “term” : “bar”,
          “count” : 2
        }, {
          “term” : “baz”,
          “count” : 1
        } ]
      }
    }

In the ``terms`` array, relevant *terms* and *counts* are returned.
You’ll probably want to display these to your users. The facet also
returns the number of documents which have no value for the field
(``missing``), the number of facet values not included in the returned
facets (``other``), and the total number of tokens in the facet
(``total``).

Notice, that the counts are scoped to the current query: *foo* is
counted only twice (not three times), *bar* is counted twice and *baz*
once.

That’s because the primary purpose of facets is to enable `*faceted
navigation* <http://en.wikipedia.org/wiki/Faceted_search>`_, allowing
the user to refine her query based on the insight from the facet, ie.
restrict the search to a specific category, price or date range. See the
example of faceted navigation at *LinkedIn* below:

.. figure:: /guide/images/linkedin-faceted-search.png
   :align: center
   :alt: Faceted Search at LinkedIn

   Faceted Search at LinkedIn
Facets can be used, however, for other purposes: computing histograms,
statistical aggregations, and more. See the article about `data
visualization </blog/2011/05/13/data-visualization-with-elasticsearch-and-protovis.html>`_
on the ElasticSearch’s blog for inspiration.

Scope
-----

As we have already mentioned, facet computation is restricted to the
scope of the current query, called ``main``, by default. Facets can be
computed within the ``global`` scope as well, in which case it will
return values computed acrosss all documents in the index:

::

    {
        “facets” : {
            ““ : {
                ““ : { ... },
                “global” : true
            }
        }
    }    

There’s one **important distinction** to keep in mind. While search
*queries* restrict both the returned documents and facet counts, search
*filters* restrict only returned documents — but *not* facet counts.

If you need to restrict both the documents and facets, and you’re not
willing or able to use a query, you may use a *facet filter*.

Facet Filter
------------

All facets can be configured with an additional filter (explained in the
`Query DSL </guide/reference/query-dsl>`_ section), which *will* reduce
the documents they use for computing results. An example with a *term*
filter:

::

    {
        “facets” : {
            ““ : {
                ““ : {
                    ...
                },
                “facet_filter” : {
                    “term” : { “user” : “kimchy”}
                }
            }
        }
    }    

Note that this is different from a facet of the
`filter </guide/reference/api/search/facets/filter-facet.html>`_ type.

Facets with the *nested* types
------------------------------

`Nested </guide/reference/mapping/nested-type.html>`_ mapping allows for
better support for “inner” documents faceting, especially when it comes
to multi valued key and value facets (like histograms, or term stats).

Why is it good for? First of all, this is the only way to use facets on
nested documents once they are used (possibly for other reasons). But,
there is also facet specific reason why nested documents can be used,
and that’s the fact that facets working on different key and value field
(like term\_stats, or histogram) can now support cases where both are
multi valued properly.

For example, lets use the following mapping:

::

    {
        “type1” : {
            “properties” : {
                “obj1” : {
                    “type” : “nested”
                }
            }
        }
    }

And, here is a sample data:

::

    {
        “obj1” : [
            {
                “name” : “blue”,
                “count” : 4
            },
            {
                “name” : “green”,
                “count” : 6
            }
        ]
    }

Nested Query Facets
~~~~~~~~~~~~~~~~~~~

Any ``nested`` query allows to specify a ``_scope`` associated with it.
Any ``facet`` allows for a scope to be defined on it controlling the
scope it will execute against. For example, the following ``facet1``
terms stats facet will only run on documents matching the nested query
associated with ``my_scope``:

::

    {
        “query”: {
            “nested”: {
                “_scope”: “my_scope”,
                “path”: “obj1”,
                “score_mode”: “avg”,
                “query”: {
                    “bool”: {
                        “must”: [
                            {“text”: {“obj1.name”: “blue”}},
                            {“range”: {“obj1.count”: {“gt”: 3}}}
                        ]
                    }
                }
            }
        },
        “facets”: {
            “facet1”: {
                “terms_stats”: {
                    “key_field”: “obj1.name”,
                    “value_field”: “obj1.count”
                },
                “scope”: “my_scope”
            }
        }
    }

All Nested Matching Root Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another option is to run the facet on all the nested documents matching
the root objects that the main query will end up producing. For example:

::

    {
        “query”: {
            “match_all”: {}
        },
        “facets”: {
            “facet1”: {
                “terms_stats”: {
                    “key_field” : “name”,
                    “value_field”: “count”
                },
                “nested”: “obj1”
            }
        }
    }

The ``nested`` element provides the path to the nested document (can be
a multi level nested docs) that will be used.



