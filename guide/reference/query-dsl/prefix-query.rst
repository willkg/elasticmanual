
==============
 Prefix Query 
==============




—-
layout: guide
title: Prefix Query
cat: guide
sidebar: reference\_query\_dsl
—-

Matches documents that have fields containing terms with a specified
prefix (**not analyzed**). The prefix query maps to Lucene
``PrefixQuery``. The following matches documents where the user field
contains a term that starts with ``ki``:

::

    {
        “prefix” : { “user” : “ki” }
    }

A boost can also be associated with the query:

::

    {
        “prefix” : { “user” :  { “value” : “ki”, “boost” : 2.0 } }
    }

Or :

::

    {
        “prefix” : { “user” :  { “prefix” : “ki”, “boost” : 2.0 } }
    }

This multi term query allows to control how it gets rewritten using the
`rewrite <multi-term-rewrite.html>`_ parameter.



