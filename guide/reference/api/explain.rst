
=============
 Explain API 
=============




—-
layout: guide
title: Explain API
cat: guide
sidebar: reference\_api
—-

The explain api computes a score explanation for a query and a specific
document. This can give useful feedback whether a document matches or
didn’t match a specific query. This feature is available from version
``0.19.9`` and up.

Usage
=====

Full query example:

::

    curl -XGET 'localhost:9200/twitter/tweet/1/_explain’ -d '{
          “query” : {
            “term” : { “message” : “search” }
          }
    }’

This will yield the following result:

::

    {
      “ok” : true,
      “matches” : true,
      “explanation” : {
        “value” : 0.15342641,
        “description” : “fieldWeight(message:search in 0), product of:”,
        “details” : [ {
          “value” : 1.0,
          “description” : “tf(termFreq(message:search)=1)”
        }, {
          “value” : 0.30685282,
          “description” : “idf(docFreq=1, maxDocs=1)”
        }, {
          “value” : 0.5,
          “description” : “fieldNorm(field=message, doc=0)”
        } ]
      }
    }

There is also a simpler way of specifying the query via the ``q``
parameter. The specified ``q`` parameter value is then parsed as if the
``query_string`` query was used. Example usage of the ``q`` parameter in
the explain api:

::

        curl -XGET 'localhost:9200/twitter/tweet/1/_explain?q=message:search’

This will yield the same result as the previous request.

All parameters
==============

-  ``fields``: Allows to control which fields to return as part of the
   document explained (support ``_source`` for the full document). Note,
   this feature is available since 0.20.
-  ``routing``: Controls the routing in the case the routing was used
   during indexing.
-  ``parent``: Same effect as setting the routing parameter.
-  ``preference``: Controls on which shard the explain is executed.
-  ``source``: Allows the data of the request to be put in the query
   string of the url.
-  ``q``: The query string (maps to the query\_string query).
-  ``df``: The default field to use when no field prefix is defined
   within the query. Defaults to \_all field.
-  ``analyzer``: The analyzer name to be used when analyzing the query
   string. Defaults to the analyzer of the \_all field.
-  ``analyze_wildcard`` Should wildcard and prefix queries be analyzed
   or not. Defaults to false.
-  ``lowercase_expanded_terms``: Should terms be automatically
   lowercased or not. Defaults to true.
-  ``lenient``: If set to true will cause format based failures (like
   providing text to a numeric field) to be ignored. Defaults to false.
-  ``default_operator``: The default operator to be used, can be AND or
   OR. Defaults to OR.




