
========================
 Open / Close Index API 
========================




—-
layout: guide
title: Open / Close Index API
cat: guide
sidebar: reference\_api
—-

The open and close index APIs allow to close an index, and later on
opening it. A closed index has almost no overhead on the cluster (except
for maintaining its metadata), and is blocked for read/write operations.
A closed index can be opened which will then go through the normal
recovery process.

The REST endpoint is ``/{index}/_close`` and ``/{index}/_open``. For
example:

::

    curl -XPOST 'localhost:9200/my_index/_close’

        curl -XPOST 'localhost:9200/my_index/_open’




