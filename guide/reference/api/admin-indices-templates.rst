
=====================
 Index Templates API 
=====================




—-
layout: guide
title: Index Templates API
cat: guide
sidebar: reference\_api
—-

Index templates allow to define templates that will automatically be
applied to new indices created. The templates include both settings and
mappings, and a simple pattern template that controls if the template
will be applied to the index created. For example:

::

    curl -XPUT localhost:9200/_template/template_1 -d '
    {
        “template” : “te*”,
        “settings” : {
            “number_of_shards” : 1
        },
        “mappings” : {
            “type1” : {
                “_source” : { “enabled” : false }
            }
        }
    }
    '

Defines a template named template\_1, with a template pattern of
``te*``. The settings and mappings will be applied to any index name
that matches the ``te*`` template.

Deleting a Template
===================

Index templates are identified by a name (in the above case
``template_1``) and can be delete as well:

::

    curl -XDELETE localhost:9200/_template/template_1

GETting a Template
==================

Index templates are identified by a name (in the above case
``template_1``) and can be retrieved using the following:

::

    curl -XGET localhost:9200/_template/template_1

To get list of all index templates you can use `Cluster
State <admin-cluster-state.html>`_ API and check for the
metadata/templates section of the response.

Multiple Template Matching
==========================

Multiple index templates can potentially match an index, in this case,
both the settings and mappings are merged into the final configuration
of the index. The order of the merging can be controlled using the
``order`` parameter, with lower order being applied first, and higher
orders overriding them. For example:

::

    curl -XPUT localhost:9200/_template/template_1 -d '{
        “template” : “*”,
        “order” : 0,
        “settings” : {
            “number_of_shards” : 1
        },
        “mappings” : {
            “type1” : {
                “_source” : { “enabled” : false }
            }
        }}'

        curl -XPUT localhost:9200/_template/template_2 -d '{
        “template” : “te*”,
        “order” : 1,
        “settings” : {
            “number_of_shards” : 1
        },
        “mappings” : {
            “type1” : {
                “_source” : { “enabled” : true }
            }
        }}'

The above will disable storing the ``_source`` on all ``type1`` types,
but for indices of that start with ``te*``, source will still be
enabled. Note, for mappings, the merging is “deep”, meaning that
specific object/property based mappings can easily be added/overridden
on higher order templates, with lower order templates providing the
basis.



