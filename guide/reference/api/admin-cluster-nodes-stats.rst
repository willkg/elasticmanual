
=================
 Nodes Stats API 
=================




—-
layout: guide
title: Nodes Stats API
cat: guide
sidebar: reference\_api
—-

The cluster nodes stats API allows to retrieve one or more (or all) of
the cluster nodes statistics.

::

    $ curl -XGET 'http://localhost:9200/_cluster/nodes/stats’

        $ curl -XGET 'http://localhost:9200/_cluster/nodes/nodeId1,nodeId2/stats’

The first command retrieves stats of all the nodes in the cluster. The
second command selectively retrieves nodes stats of only ``nodeId1`` and
``nodeId2``. All the nodes selective options are explained
`here <index.html>`_.



