
================
 Count Java API 
================




—-
layout: guide
title: Count Java API
cat: guide
sidebar: reference\_java\_api
—-

The count API allows to easily execute a query and get the number of
matches for that query. It can be executed across one or more indices
and across one or more types. The query can be provided using the `Query
DSL <query-dsl.html>`_.

::

    import static org.elasticsearch.index.query.xcontent.FilterBuilders.*;import static org.elasticsearch.index.query.xcontent.QueryBuilders.*;

        CountResponse response = client.prepareCount(“test”)
            .setQuery(termQuery(”_type”, “type1”))
            .execute()
            .actionGet();

For more information on the count operation, check out the REST
`count </guide/reference/api/count.html>`_ docs.

Operation Threading
===================

The count API allows to set the threading model the operation will be
performed when the actual execution of the API is performed on the same
node (the API is executed on a shard that is allocated on the same
server).

There are three threading modes.The ``NO_THREADS`` mode means that the
count operation will be executed on the calling thread. The
``SINGLE_THREAD`` mode means that the count operation will be executed
on a single different thread for all local shards. The
``THREAD_PER_SHARD`` mode means that the count operation will be
executed on a different thread for each local shard.

The default mode is ``SINGLE_THREAD``.



