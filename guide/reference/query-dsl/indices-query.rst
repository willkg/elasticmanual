
===============
 Indices Query 
===============




—-
layout: guide
title: Indices Query
cat: guide
sidebar: reference\_query\_dsl
—-

The ``indices`` query can be used when executed across multiple indices,
allowing to have a query that executes only when executed on an index
that matches a specific list of indices, and another query that executes
when it is executed on an index that does not match the listed indices.

::

    {
        “indices” : {
            “indices” : [“index1”, “index2”],
            “query” : {
                “term” : { “tag” : “wow” }
            },
            “no_match_query” : {
                “term” : { “tag” : “kow” }
            }
        }
    }

``no_match_query`` can also have “string” value of ``none`` (to match no
documents), and ``all`` (to match all).



