
================
 GeoShape Query 
================




—-
layout: guide
title: GeoShape Query
cat: guide
sidebar: reference\_query\_dsl
—-

Query version of the `geo\_shape
Filter </guide/reference/query-dsl/geo-shape-filter.html>`_.

The following is an example of the ``geo_shape`` Query:

::

    {
        “query” : {
            “geo_shape” : {
                “location” : {
                    “shape” : {
                        “type” : “envelope”,
                        “coordinates” : [[-45.0, 45.0], [45.0, -45.0]]
                    }
                    “relation” : “contains”
                }
            }
        }
    }

See the Filter’s documentation for more information.

Relevancy and Score
===================

Currently ElasticSearch does not have any notion of geo shape relevancy,
consequently the Query internally uses a ``constant_score`` Query.

Query vs. Filter
================

The ``geo_shape`` Query and Filter use slightly different search
algorithms internally. The Query makes use of a ``bool`` Query
internally while the Filter uses a ``terms`` Filter. As such, due to
internal logic of the ``bool`` Query, there **may** be a slight
performance improvement using the ``geo_shape`` Query when querying
areas with a high density of shapes. However it is recommended that you
experiment with your dataset to identify which approach performs better.



