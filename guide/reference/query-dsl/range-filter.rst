
==============
 Range Filter 
==============




—-
layout: guide
title: Range Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents with fields that have terms within a certain range.
Similar to range query, except that it acts as a filter. Can be placed
within queries that accept a filter.

::

    {
        “constant_score” : {
            “filter” : {
                “range” : {
                    “age” : { 
                        “from” : “10”, 
                        “to” : “20”, 
                        “include_lower” : true, 
                        “include_upper” : false
                    }
                }
            }
        }
    }

The ``range`` filter top level parameters include:

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
Same as setting ``from`` to the value, and ``include_lower`` to
``true``.
``lt``
Same as setting ``to`` to the value, and ``include_upper`` to ``false``.
``lte``
Same as setting ``to`` to the value, and ``include_upper`` to ``true``.
Caching
=======

The result of the filter is automatically cached by default. The
``_cache`` can be set to ``false`` to turn it off.



