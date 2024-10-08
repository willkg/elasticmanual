
=============
 Warmers API 
=============




—-
layout: guide
title: Warmers API
cat: guide
sidebar: reference\_api
—-

Index warming allows to run registered search requests to warm up the
index before it is available for search. With the near real time aspect
of search, cold data (segments) will be warmed up before they become
available for search. This feature is available from version 0.20
onwards.

Warmup searches typically include requests that require heavy loading of
data, such as faceting or sorting on specific fields. The warmup APIs
allows to register warmup (search) under specific names, remove them,
and get them.

Index warmup can be disabled by setting ``index.warmer.enabled`` to
``false``. It is supported as a realtime setting using update settings
API. This can be handy when doing initial bulk indexing, disabling pre
registered warmers to make indexing faster and less expensive and then
enable it.

Index Creation / Templates
==========================

Warmers can be registered when an index gets created, for example:

::

    curl -XPUT localhost:9200/test -d '{
        “warmers” : {
            “warmer_1” : {
                “types” : [],
                “source” : {
                    “query” : {
                        ...
                    },
                    “facets” : {
                        ...
                    }
                }
            }
        }
    }’

Or, in an index template:

::

    curl -XPUT localhost:9200/_template/template_1 -d '
    {
        “template” : “te*”,
        “warmers” : {
            “warmer_1” : {
                “types” : [],
                “source” : {
                    “query” : {
                        ...
                    },
                    “facets” : {
                        ...
                    }
                }
            }
        }
    }’

Put Warmer
==========

Allows to put a warmup search request on a specific index (or indices),
with the body composing of a regular search request. Types can be
provided as part of the URI if the search request is designed to be run
only against the specific types.

Here is an example that registers a warmup called ``warmer_1`` against
index ``test`` (can be alias or several indices), for a search request
that runs against all types:

::

    curl -XPUT localhost:9200/test/_warmer/warmer_1 -d '{
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “facet_1” : {
                “terms” : {
                    “field” : “field”
                }
            } 
        }
    }’

And an example that registers a warmup against specific types:

::

    curl -XPUT localhost:9200/test/type1/_warmer/warmer_1 -d '{
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “facet_1” : {
                “terms” : {
                    “field” : “field”
                }
            } 
        }
    }’

Delete Warmer
=============

Removing a warmer can be done against an index (or alias / indices)
based on its name. The provided name can be a simple wildcard expression
or omitted to remove all warmers. Some samples:

::

        
            delete warmer named warmer_1 on test index
        curl -XDELETE localhost:9200/test/_warmer/warmer_1 

         
            delete all warmers that start with warm on test index
        curl -XDELETE localhost:9200/test/_warmer/warm* 

         
            delete all warmers for test index
        curl -XDELETE localhost:9200/test/_warmer/

GETting Warmer
==============

Getting a warmer for specific index (or alias, or several indices) based
on its name. The provided name can be a simple wildcard expression or
omitted to get all warmers. Some examples:

::

        
            get warmer named warmer_1 on test index
        curl -XGET localhost:9200/test/_warmer/warmer_1 

         
            get all warmers that start with warm on test index
        curl -XGET localhost:9200/test/_warmer/warm* 

         
            get all warmers for test index
        curl -XGET localhost:9200/test/_warmer/




