
================
 Span Not Query 
================




—-
layout: guide
title: Span Not Query
cat: guide
sidebar: reference\_query\_dsl
—-

Removes matches which overlap with another span query. The span not
query maps to Lucene ``SpanNotQuery``. Here is an example:

::

    {
        “span_not” : {
            ©“include” : {
                “span_term” : { “field1” : “value1” }
            },
            “exclude” : {
                “span_term” : { “field2” : “value2” }
            }
        }
    }

The ``include`` and ``exclude`` clauses can be any span type query. The
``include`` clause is the span query whose matches are filtered, and the
``exclude`` clause is the span query whose matches must not overlap
those returned.



