
=============
 Range Query 
=============




—-
layout: guide
title: Range Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches documents with fields that have terms within a certain range.
The type of the Lucene query depends on the field type, for ``string``
fields, the ``TermRangeQuery``, while for number/date fields, the query
is a ``NumericRangeQuery``. The following example returns all documents
where ``age`` is between ``10`` and ``20``:

::

    {
        “range” : {
            “age” : { 
                “from” : 10, 
                “to” : 20, 
                “include_lower” : true, 
                “include_upper”: false, 
                “boost” : 2.0
            }
        }
    }

The ``range`` query top level parameters include:

Name
Description
``from``
The lower bound. Defaults to start from the first.
``to``
The upper bound. Defaults to unbounded.
``include_lower``
Should the first from (if set) be inclusive or not. Defaults to ``true``
``include_upper``
Should the last to (if set) be inclusive or not. Defaults to ``true``.
``gt``
Same as setting ``from`` to the value, and ``include_lower`` to
``false``.
``gte``
Same as setting ``from`` to the value,and ``include_lower`` to ``true``.
``lt``
Same as setting ``to`` to the value, and ``include_upper`` to ``false``.
``lte``
Same as setting ``to`` to the value, and ``include_upper`` to ``true``.
``boost``
Sets the boost value of the query. Defaults to ``1.0``.



