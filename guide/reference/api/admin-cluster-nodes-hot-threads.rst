
================================
 Cluster Nodes hot\_threads API 
================================




—-
layout: guide
title: Cluster Nodes hot\_threads API
cat: guide
sidebar: reference\_api
—-

An API allowing to get the current hot threads on each node in the
cluster. Endpoints are ``/_nodes/hot_threads``, and
``/_nodes/{nodesIds}/hot_threads``. This API is experimental.

The output is plain text with a breakdown of each node’s top hot
threads. Parameters allows are:

-  ``threads``: number of hot threads to provide, defaults to 3.
-  ``interval``: the interval to do the second sampling of threads.
   Defaults to 500ms.
-  ``type``: The type to sample, defaults to cpu, but supports wait and
   block to see hot threads that are in wait or block state.




