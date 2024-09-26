
===============
 Span Or Query 
===============




—-
layout: guide
title: Span Or Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches the union of its span clauses. The span or query maps to Lucene
``SpanOrQuery``. Here is an example:

::

    {
        “span_or” : {
            “clauses” : [
                { “span_term” : { “field” : “value1” } },
                { “span_term” : { “field” : “value2” } },
                { “span_term” : { “field” : “value3” } }
            ]
        }
    }

The ``clauses`` element is a list of one or more other span type
queries.



