
============================
 Custom Filters Score Query 
============================




—-
layout: guide
title: Custom Filters Score Query
cat: guide
sidebar: reference\_query\_dsl
—-

A ``custom_filters_score`` query allows to execute a query, and if the
hit matches a provided filter (ordered), use either a boost or a script
associated with it to compute the score. Here is an example:

::

    {
        “custom_filters_score” : {
            “query” : {
                “match_all” : {}
            },
            “filters” : [
                {
                    “filter” : { “range” : { “age” : {“from” : 0, “to” : 10} } },
                    “boost” : “3”
                },
                {
                    “filter” : { “range” : { “age” : {“from” : 10, “to” : 20} } },
                    “boost” : “2”
                }
            ]
        }
    }

This can considerably simplify and increase performance for
parameterized based scoring since filters are easily cached for faster
performance, and boosting / script is considerably simpler.

Score Mode
----------

A ``score_mode`` can be defined to control how multiple matching filters
control the score. By default, it is set to ``first`` which means the
first matching filter will control the score of the result. It can also
be set to ``max``/@total@/@avg@ which will aggregate the result from all
matching filters based on the aggregation type.

Script
------

A ``script`` can be used instead of ``boost`` for more complex score
calculations. With optional ``params`` and ``lang`` (on the same level
as ``query`` and ``filters``).



