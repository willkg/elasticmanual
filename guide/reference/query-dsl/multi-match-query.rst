
===================
 Multi Match Query 
===================




—-
layout: guide
title: Multi Match Query
cat: guide
sidebar: reference\_query\_dsl
—-

The ``multi_match`` query builds further on top of the ``match`` query
by allowing multiple fields to be specified. The idea here is to allow
to more easily build a concise match type query over multiple fields
instead of using a relatively more expressive query by using multiple
match queries within a ``bool`` query.

The structure of the query is a bit different. Instead of a nested json
object defining the query field, there is a top json level field for
defining the query fields. Example:

::

    {
      “multi_match” : {
        “query” : “this is a test”,
        “fields” : [ “subject”, “message” ]
      }
    }

The ``multi_match`` query creates either a ``bool`` or a ``dis_max`` top
level query. Each field is a query clause in this top level query. The
query clause contains the actual query (the specified 'type’ defines
what query this will be). Each query clause is basically a ``should``
clause.

Options
-------

All options that apply on the ``match`` query also apply on the
``multi_match`` query. The ``match`` query options apply only on the
individual clauses inside the top level query.

-  ``fields`` – Fields to be used in the query.
-  ``use_dis_max`` – Boolean indicating to either create a ``dis_max``
   query or a ``bool`` query. Defaults to ``true``.
-  ``tie_breaker`` – Multiplier value to balance the scores between
   lower and higher scoring fields. Only applicable when ``use_dis_max``
   is set to true. Defaults to ``0.0``.

The query accepts all the options that a regular ``match`` query
accepts.

Boosting
--------

The ``multi_match`` query supports field boosting via ``^`` notation in
the fields json field.

::

    {
      “multi_match” : {
        “query” : “this is a test”,
        “fields” : [ “subject^2”, “message” ]
      }
    }

In the above example hits in the ``subject`` field are 2 times more
important than in the ``message`` field.



