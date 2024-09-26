
=================
 Span Term Query 
=================




—-
layout: guide
title: Span Term Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches spans containing a term. The span term query maps to Lucene
``SpanTermQuery``. Here is an example:

::

    {
        “span_term” : { “user” : “kimchy” }
    }    

A boost can also be associated with the query:

::

    {
        “span_term” : { “user” : { “value” : “kimchy”, “boost” : 2.0 } }
    }    

Or :

::

    {
        “span_term” : { “user” : { “term” : “kimchy”, “boost” : 2.0 } }
    }    




