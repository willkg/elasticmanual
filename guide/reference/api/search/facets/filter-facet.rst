
==============================
 Search API – Filter Facets 
==============================




—-
layout: guide
title: Search API – Filter Facets
cat: guide
sidebar: reference\_api\_search\_facets
—-

A filter facet (not to be confused with a `facet
filter </guide/reference/api/search/facets/index.html>`_) allows you to
return a count of the hits matching the filter. The filter itself can be
expressed using the `Query DSL <../../../query-dsl/>`_. For example:

::

    {
        “facets” : {
            “wow_facet” : {
                “filter” : {
                    “term” : { “tag” : “wow” }
                }
            }
        }
    }    

Note, filter facet filters are faster than query facet when using native
filters (non query wrapper ones).



