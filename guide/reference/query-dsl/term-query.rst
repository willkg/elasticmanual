
============
 Term Query 
============




—-
layout: guide
title: Term Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches documents that have fields that contain a term (**not
analyzed**). The term query maps to Lucene ``TermQuery``. The following
matches documents where the user field contains the term ``kimchy``:

::

    {
        “term” : { “user” : “kimchy” }
    }    

A boost can also be associated with the query:

::

    {
        “term” : { “user” : { “value” : “kimchy”, “boost” : 2.0 } }
    }    

Or :

::

    {
        “term” : { “user” : { “term” : “kimchy”, “boost” : 2.0 } }
    }    




