
================
 Filtered Query 
================




—-
layout: guide
title: Filtered Query
cat: guide
sidebar: reference\_query\_dsl
—-

A query that applies a filter to the results of another query. This
query maps to Lucene ``FilteredQuery``.

::

    {
        “filtered” : {
            “query” : {
                “term” : { “tag” : “wow” }
            },
            “filter” : {
                “range” : {
                    “age” : { “from” : 10, “to” : 20 }
                }
            }
        }
    }

The filter object can hold only filter elements, not queries. Filters
can be much faster compared to queries since they don’t perform any
scoring, especially when they are cached.



