
=================
 Search Java API 
=================




—-
layout: guide
title: Search Java API
cat: guide
sidebar: reference\_java\_api
—-

The search API allows to execute a search query and get back search hits
that match the query. It can be executed across one or more indices and
across one or more types. The query can either be provided using the
`Query DSL <query-dsl.html>`_. The body of the search request is built
using the ``SearchSourceBuilder``. Here is an example:

::

    import static org.elasticsearch.index.query.FilterBuilders.*;import static org.elasticsearch.index.query.QueryBuilders.*;

        SearchResponse response = client.prepareSearch(“test”)
            .setSearchType(SearchType.DFS_QUERY_THEN_FETCH)
            .setQuery(termQuery(“multi”, “test”))
            .setFrom(0).setSize(60).setExplain(true)
            .execute()
            .actionGet();

For more information on the search operation, check out the REST
`search </guide/reference/api/search/>`_ docs.

Using scrolls in Java
=====================

Read the `scroll
documentation </guide/reference/api/search/scroll.html>`_ first!

::

    import static org.elasticsearch.index.query.FilterBuilders.*;import static org.elasticsearch.index.query.QueryBuilders.*;

        QueryBuilder qb = termQuery(“multi”, “test”);

        SearchResponse scrollResp = client.prepareSearch(test)
            .setSearchType(SearchType.SCAN)
            .setScroll(new TimeValue(60000))
            .setQuery(qb.buildAsBytes())
            .setSize(100).execute().actionGet(); //100 hits per shard will be returned for each scroll//Scroll until no hits are returnedwhile (true) {
        scrollResp = client.prepareSearchScroll(scrollResp.getScrollId()).setScroll(new TimeValue(600000)).execute().actionGet();
        boolean hitsRead = false;
        for (SearchHit hit : scrollResp.getHits()) {
            hitsRead = true;
            //Handle the hit…
        }
        //Break condition: No hits are returned
        if (!hitsRead) {
            break;
        }}

Operation Threading
===================

The search API allows to set the threading model the operation will be
performed when the actual execution of the API is performed on the same
node (the API is executed on a shard that is allocated on the same
server).

There are three threading modes.The ``NO_THREADS`` mode means that the
search operation will be executed on the calling thread. The
``SINGLE_THREAD`` mode means that the search operation will be executed
on a single different thread for all local shards. The
``THREAD_PER_SHARD`` mode means that the search operation will be
executed on a different thread for each local shard.

The default mode is ``SINGLE_THREAD``.



