
======================
 Search API – Query 
======================




—-
layout: guide
title: Search API – Query
cat: guide
sidebar: reference\_api\_search
—-

The query element within the search request body allows to define a
query using the `Query DSL </guide/reference/query-dsl>`_.

::

    {
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }




