
======================
 Constant Score Query 
======================




—-
layout: guide
title: Constant Score Query
cat: guide
sidebar: reference\_query\_dsl
—-

A query that wraps a filter or another query and simply returns a
constant score equal to the query boost for every document in the
filter. Maps to Lucene ``ConstantScoreQuery``.

::

    {
        “constant_score” : {
            “filter” : {
                “term” : { “user” : “kimchy”}
            },
            “boost” : 1.2
        }
    }

The filter object can hold only filter elements, not queries. Filters
can be much faster compared to queries since they don’t perform any
scoring, especially when they are cached.

A query can also be wrapped in a ``constant_score`` query:

::

    {
        “constant_score” : {
            “query” : {
                “term” : { “user” : “kimchy”}
            },
            “boost” : 1.2
        }
    }




