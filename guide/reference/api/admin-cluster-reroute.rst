
=====================
 Cluster Reroute API 
=====================




—-
layout: guide
title: Cluster Reroute API
cat: guide
sidebar: reference\_api
—-

The reroute command allows to explicitly execute a cluster reroute
allocation command including specific commands. For example, a shard can
be moved from one node to another explicitly, an allocation can be
canceled, or an unassigned shard can be explicitly allocated on a
specific node.

Here is a short example of how a simple reroute API call:

::

        
    curl -XPOST 'localhost:9200/_cluster/reroute’ -d '{
        “commands” : [ {
            “move” : 
                {
                  “index” : “test”, “shard” : 0, 
                  “from_node” : “node1”, “to_node” : “node2”
                }
            },
            {
              “allocate” : {
                  “index” : “test”, “shard” : 1, “node” : “node3”
              }
            }
        ]
    }’

An important aspect to remember is the fact that once when an allocation
occurs, the cluster will aim at re-balancing its state back to an even
state. For example, if the allocation includes moving a shard from
``node1`` to ``node2``, in an ``even`` state, then another shard will be
moved from ``node2`` to ``node1`` to even things out.

The cluster can be set to disable allocations, which means that only the
explicitly allocations will be performed. Obviously, only once all
commands has been applied, the cluster will aim to be re-balance its
state.

Another option is to run the commands in ``dry_run`` (as a URI flag, or
in the request body). This will cause the commands to apply to the
current cluster state, and return the resulting cluster after the
commands (and re-balancing) has been applied.

The commands supported are:

-  ``move``: Move a started shard from one node to another node. Accepts
   ``index`` and ``shard`` for index name and shard number,
   ``from_node`` for the node to move the shard ``from``, and
   ``to_node`` for the node to move the shard to.
-  ``cancel``: Cancel allocation of a shard (or recovery). Accepts
   ``index`` and ``shard`` for index name and shard number, and ``node``
   for the node to cancel the shard allocation on. It also accepts
   ``allow_primary`` flag to explicitly specify that it is allowed to
   cancel allocation for a primary shard.
-  ``allocate``: Allocate an unassigned shard to a node. Accepts the
   ``index`` and ``shard`` for index name and shard number, and ``node``
   to allocate the shard to. It also accepts ``allow_primary`` flag to
   explicitly specify that it is allowed to explicitly allocate a
   primary shard (might result in data loss).




