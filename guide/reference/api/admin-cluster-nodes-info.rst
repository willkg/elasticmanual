
================
 Nodes Info API 
================




—-
layout: guide
title: Nodes Info API
cat: guide
sidebar: reference\_api
—-

The cluster nodes info API allows to retrieve one or more (or all) of
the cluster nodes information.

::

    $ curl -XGET 'http://localhost:9200/_cluster/nodes’

        $ curl -XGET 'http://localhost:9200/_cluster/nodes/nodeId1,nodeId2’

The first command retrieves information of all the nodes in the cluster.
The second command selectively retrieves nodes information of only
``nodeId1`` and ``nodeId2``. All the nodes selective options are
explained `here <index.html>`_.



