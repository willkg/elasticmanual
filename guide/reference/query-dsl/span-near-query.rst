
=================
 Span Near Query 
=================




—-
layout: guide
title: Span Near Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches spans which are near one another. One can specify *slop*, the
maximum number of intervening unmatched positions, as well as whether
matches are required to be in-order. The span near query maps to Lucene
``SpanNearQuery``. Here is an example:

::

    {
        “span_near” : {
            “clauses” : [
                { “span_term” : { “field” : “value1” } },
                { “span_term” : { “field” : “value2” } },
                { “span_term” : { “field” : “value3” } }
            ],
            “slop” : 12,
            “in_order” : false,
            “collect_payloads” : false
        }
    }

The ``clauses`` element is a list of one or more other span type queries
and the ``slop`` controls the maximum number of intervening unmatched
positions permitted.



