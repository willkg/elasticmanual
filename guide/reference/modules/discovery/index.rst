
===========
 Discovery 
===========




—-
layout: guide
title: Discovery
cat: guide
sidebar: reference\_modules\_discovery
—-

The discovery module is responsible for discovering nodes within a
cluster, as well as electing a master node.

Note, ElasticSearch is a peer to peer based system, nodes communicate
with one another directly if operations are delegated / broadcast. All
the main APIs (index, delete, search) do not communicate with the master
node. The responsibility of the master node is to maintain the global
cluster state, and act if nodes join or leave the cluster by reassigning
shards. Each time a cluster state is changed, the state is made known to
the other nodes in the cluster (the manner depends on the actual
discovery implementation).

Settings
--------

The ``cluster.name`` allows to create separated clusters from one
another. The default value for the cluster name is ``elasticsearch``,
though it is recommended to change this to reflect the logical group
name of the cluster running.



