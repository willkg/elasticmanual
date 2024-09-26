
=============
 Field Query 
=============




—-
layout: guide
title: Field Query
cat: guide
sidebar: reference\_query\_dsl
—-

A query that executes a query string against a specific field. It is a
simplified version of `query\_string <query-string-query.html>`_ query
(by setting the ``default_field`` to the field this query executed
against). In its simplest form:

::

    {
        “field” : { 
            “name.first” : “+something -else”
        }
    }

Most of the ``query_string`` parameters are allowed with the ``field``
query as well, in such a case, the query should be formatted as follows:

::

    {
        “field” : { 
            “name.first” : {
                “query” : “+something -else”,
                “boost” : 2.0,
                “enable_position_increments”: false
            }
        }
    }




