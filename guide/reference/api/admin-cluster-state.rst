
===================
 Cluster State API 
===================




—-
layout: guide
title: Cluster State API
cat: guide
sidebar: reference\_api
—-

The cluster state API allows to get a comprehensive state information of
the whole cluster.

::

    $ curl -XGET 'http://localhost:9200/_cluster/state’

Response Filters
================

It is possible to filter the cluster state response using the following
REST parameters:

Parameter
Description
filter\_nodes
Set to ``true`` to filter out the ``nodes`` part of the response.
filter\_routing\_table
Set to ``true`` to filter out the ``routing_table`` part of the
response.
filter\_metadata
Set to ``true`` to filter out the ``metadata`` part of the response.
filter\_blocks
Set to ``true`` to filter out the ``blocks`` part of the response.
filter\_indices
When not filtering metadata, a comma separated list of indices to
include in the response.
Example follows:

::

    $ curl -XGET 'http://localhost:9200/_cluster/state?filter_nodes=true’




