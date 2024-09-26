
==========================
 Delete By Query Java API 
==========================




—-
layout: guide
title: Delete By Query Java API
cat: guide
sidebar: reference\_java\_api
—-

The delete by query API allows to delete documents from one or more
indices and one or more types based on a query. The query can either be
provided the `Query DSL <../query_dsl>`_. Here is an example:

::

    import static org.elasticsearch.index.query.xcontent.FilterBuilders.*;import static org.elasticsearch.index.query.xcontent.QueryBuilders.*;

        DeleteByQueryResponse response = client.prepareDeleteByQuery(“test”)
            .setQuery(termQuery(”_type”, “type1”))
            .execute()
            .actionGet();

For more information on the delete by query operation, check out the
`delete\_by\_query API </guide/reference/api/delete-by-query.html>`_
docs.



