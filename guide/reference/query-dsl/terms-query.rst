
=============
 Terms Query 
=============




—-
layout: guide
title: Terms Query
cat: guide
sidebar: reference\_query\_dsl
—-

A query that match on any (configurable) of the provided terms. This is
a simpler syntax query for using a ``bool`` query with several ``term``
queries in the ``should`` clauses. For example:

::

    {
        “terms” : {
            “tags” : [ “blue”, “pill” ],
            “minimum_match” : 1
        }
    }

The ``terms`` query is also aliased with ``in`` as the query name for
simpler usage.



