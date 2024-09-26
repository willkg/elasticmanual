
===================
 Has Parent Filter 
===================




—-
layout: guide
title: Has Parent Filter
cat: guide
sidebar: reference\_query\_dsl
—-

The ``has_parent`` filter accepts a query and a parent type. The query
is executed in the parent document space, which is specified by the
parent type. This filter return child documents which associated parents
have matched. For the rest ``has_parent`` filter has the same options
and works in the same manner as the ``has_child`` filter.

The ``has_parent`` filter is available from version ``0.19.10``. This is
an experimental filter.

Filter example
==============

::

    {
        “has_parent” : {
            “parent_type” : “blog”,
            “query” : {
                “term” : {
                    “tag” : “something”
                }
            }
        }}  

The ``parent_type`` field name can also be abbreviated to ``type``.

The way that the filter is implemented is by first running the parent
query, doing the matching up to the child doc for each document matched.

Scope
=====

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

Memory considerations
=====================

With the current implementation, all ``_id`` values are loaded to memory
(heap) in order to support fast lookups, so make sure there is enough
memory for it.



