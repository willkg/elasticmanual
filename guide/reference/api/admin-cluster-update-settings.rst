
=============================
 Cluster Update Settings API 
=============================




—-
layout: guide
title: Cluster Update Settings API
cat: guide
sidebar: reference\_api
—-

Allow to update cluster wide specific settings. Settings updated can
either be persistent (applied cross restarts) or transient (will not
survive a full cluster restart). Here is an example:

::

    curl -XPUT localhost:9200/_cluster/settings -d '{
        “persistent” : {
            “discovery.zen.minimum_master_nodes” : 2
        }
    }’

Or:

::

    curl -XPUT localhost:9200/_cluster/settings -d '{
        “transient” : {
            “discovery.zen.minimum_master_nodes” : 2
        }
    }’

There is a specific list of settings that can be updated, those include:

-  ``discovery.zen.minimum_master_nodes``
-  ``index.shard.recovery.concurrent_streams``
-  ``cluster.routing.allocation.node_initial_primaries_recoveries``,
   ``cluster.routing.allocation.node_concurrent_recoveries``
-  ``cluster.routing.allocation.cluster_concurrent_rebalance``
-  ``cluster.routing.allocation.awareness.attributes``
-  ``cluster.routing.allocation.awareness.force.*``
-  ``cluster.routing.allocation.disable_allocation``
-  ``cluster.routing.allocation.disable_replica_allocation``
-  ``cluster.routing.allocation.include.*``
-  ``cluster.routing.allocation.exclude.*``
-  ``indices.cache.filter.size``
-  ``indices.ttl.interval``
-  ``indices.recovery.file_chunk_size``,
   ``indices.recovery.translog_ops``,
   ``indices.recovery.translog_size``, ``indices.recovery.compress``,
   ``indices.recovery.concurrent_streams``,
   ``indices.recovery.max_size_per_sec``.
-  ````

Logger values can also be updated by setting ``logger.`` prefix. More
settings will be allowed to be updated.

Cluster wide settings can be returned using
``curl -XGET localhost:9200/_cluster/settings``.



