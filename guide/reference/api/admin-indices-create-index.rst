
==================
 Create Index API 
==================




—-
layout: guide
title: Create Index API
cat: guide
sidebar: reference\_api
—-

The create index API allows to instantiate an index. ElasticSearch
provides support for multiple indices, including executing operations
across several indices. Each index created can have specific settings
associated with it.

::

    $ curl -XPUT 'http://localhost:9200/twitter/’

        $ curl -XPUT 'http://localhost:9200/twitter/’ -d 'index :
        number_of_shards : 3
        number_of_replicas : 2'

The above second example curl shows how an index called ``twitter`` can
be created with specific settings for it using
`YAML <http://www.yaml.org>`_. In this case, creating an index with 3
shards, each with 2 replicas. The index settings can also defined with
`JSON <http://www.json.org>`_:

::

    $ curl -XPUT 'http://localhost:9200/twitter/’ -d '{
        “settings” : {
            “index” : {
                “number_of_shards” : 3,
                “number_of_replicas” : 2
            }
        }
    }’

or more simplified

::

    $ curl -XPUT 'http://localhost:9200/twitter/’ -d '{
        “settings” : {
            “number_of_shards” : 3,
            “number_of_replicas” : 2
        }
    }’

*Note you do not have to explicitly specify ``index`` section inside
``settings`` section.*

Mappings
========

The create index API allows to provide a set of one or more mappings:

::

    curl -XPOST localhost:9200/test -d '{
        “settings” : {
            “number_of_shards” : 1
        },
        “mappings” : {
            “type1” : {
                “_source” : { “enabled” : false },
                “properties” : {
                    “field1” : { “type” : “string”, “index” : “not_analyzed” }
                }
            }
        }
    }’

Index Settings
==============

For more information regarding all the different index level settings
that can be set when creating an index, please check the `index
modules </guide/reference/index-modules>`_ section.



