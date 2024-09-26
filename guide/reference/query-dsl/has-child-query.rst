
=================
 Has Child Query 
=================




—-
layout: guide
title: Has Child Query
cat: guide
sidebar: reference\_query\_dsl
—-

The ``has_child`` query works the same as the
`has\_child <has-child-filter.html>`_ filter, by automatically wrapping
the filter with a `constant\_score <constant-score-query.html>`_. It has
the same syntax as the `has\_child <has-child-filter.html>`_ filter:

::

    {
        “has_child” : {
            “type” : “blog_tag”
            “query” : {
                “term” : {
                    “tag” : “something”
                }
            }
        }
    }    

Scope
-----

A ``_scope`` can be defined on the filter allowing to run facets on the
same scope name that will work against the child documents. For example:

::

    {
        “has_child” : {
            “_scope” : “my_scope”,
            “type” : “blog_tag”
            “query” : {
                “term” : {
                    “tag” : “something”
                }
            }
        }
    }    

Memory Considerations
=====================

With the current implementation, all ``_id`` values are loaded to memory
(heap) in order to support fast lookups, so make sure there is enough
mem for it.



