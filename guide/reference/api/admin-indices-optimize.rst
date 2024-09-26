
==============
 Optimize API 
==============




—-
layout: guide
title: Optimize API
cat: guide
sidebar: reference\_api
—-

The optimize API allows to optimize one or more indices through an API.
The optimize process basically optimizes the index for faster search
operations (and relates to the number of segments a lucene index within
each shard). The optimize operation allows to optimize the number of
segments to optimize to.

::

    $ curl -XPOST 'http://localhost:9200/twitter/_optimize’

Request Parameters
==================

The optimize API accepts the following request parameters:

Name
Description
max\_num\_segments
The number of segments to optimize to. To fully optimize the index, set
it to ``1``. Defaults to simply checking if a merge needs to execute,
and if so, executes it.
only\_expunge\_deletes
Should the optimize process only expunge segments with deletes in it. In
Lucene, a document is not deleted from a segment, just marked as
deleted. During a merge process of segments, a new segment is created
that does have those deletes. This flag allow to only merge segments
that have deletes. Defaults to ``false``.
refresh
Should a refresh be performed after the optimize. Defaults to ``true``.
flush
Should a flush be performed after the optimize. Defaults to ``true``.
wait\_for\_merge
Should the request wait for the merge to end. Defaults to ``true``.
Note, a merge can potentially be a very heavy operation, so it might
make sense to run it set to ``false``.
Multi Index
===========

The optimize API can be applied to more than one index with a single
call, or even on ``_all`` the indices.

::

    $ curl -XPOST 'http://localhost:9200/kimchy,elasticsearch/_optimize’

        $ curl -XPOST 'http://localhost:9200/_optimize’




