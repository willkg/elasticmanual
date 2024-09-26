
==================
 Span First Query 
==================




—-
layout: guide
title: Span First Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches spans near the beginning of a field. The span first query maps
to Lucene ``SpanFirstQuery``. Here is an example:

::

    {
        “span_first” : {
            “match” : {
                “span_term” : { “user” : “kimchy” }
            },
            “end” : 3
        }
    }    

The ``match`` clause can be any other span type query. The ``end``
controls the maximum end position permitted in a match.



