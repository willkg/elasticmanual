
=============
 Fuzzy Query 
=============




—-
layout: guide
title: Fuzzy Query
cat: guide
sidebar: reference\_query\_dsl
—-

A fuzzy based query that uses similarity based on Levenshtein (edit
distance) algorithm.

Warning: this query is not very scalable with its default prefix length
of 0 – in this case, **every** term will be enumerated and cause an edit
score calculation or ``max_expansions`` is not set.

Here is a simple example:

::

    {
        “fuzzy” : { “user” : “ki” }
    }

More complex settings can be set (the values here are the default
values):

::

        {
            “fuzzy” : { 
                “user” : {
                    “value” : “ki”,
                    “boost” : 1.0,
                    “min_similarity” : 0.5,
                    “prefix_length” : 0
                }
            }
        }

The ``max_expansions`` parameter (unbounded by default) controls the
number of terms the fuzzy query will expand to.

Numeric / Date Fuzzy
--------------------

``fuzzy`` query on a numeric field will result in a range query “around”
the value using the ``min_similarity`` value. For example:

::

    {
        “fuzzy” : {
            “price” : {
                “value” : 12,
                “min_similarity” : 2
            }
        }
    }

Will result in a range query between 10 and 14. Same applies to dates,
with support for time format for the ``min_similarity`` field:

::

    {
        “fuzzy” : {
            “created” : {
                “value” : “2010-02-05T12:05:07”,
                “min_similarity” : “1d”
            }
        }
    }

In the mapping, numeric and date types now allow to configure a
``fuzzy_factor`` mapping value (defaults to 1), which will be used to
multiply the fuzzy value by it when used in a ``query_string`` type
query. For example, for dates, a fuzzy factor of “1d” will result in
multiplying whatever fuzzy value provided in the min\_similarity by it.
Note, this is explicitly supported since query\_string query only
allowed for similarity valued between 0.0 and 1.0.



