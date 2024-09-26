
==================
 Has Parent Query 
==================




—-
layout: guide
title: Has Parent Query
cat: guide
sidebar: reference\_query\_dsl
—-

The ``has_parent`` query works the same as the
`has\_parent <has-parent-filter.html>`_ filter, by automatically
wrapping the filter with a constant\_score (when using the default score
type). It has the same syntax as the
`has\_parent <has-parent-filter.html>`_ filter. This query is
experimental and is available from version ``0.19.10``.

::

    {
        “has_parent” : {
            “parent_type” : “blog”,
            “query” : {
                “term” : {
                    “tag” : “something”
                }
            }
        }
    }    

Scoring capabilities
--------------------

The ``has_parent`` also has scoring support from version ``0.20.2``. The
supported score types are ``score`` or ``none``. The default is ``none``
and yields the same behaviour as in previous versions. If the score type
is set to another value than ``none``, the scores of all the matching
parent documents are aggregated into the associated child documents. The
score type can be specified with the ``score_type`` field inside the
``has_parent`` query:

::

    {
        “has_parent” : {
            “parent_type” : “blog”,
            “score_type” : “score”,
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
same scope name that will work against the parent documents. For
example:

::

    {
        “has_parent” : {
            “_scope” : “my_scope”,
            “parent_type” : “blog”,
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
memory for it.



