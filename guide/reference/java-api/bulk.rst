
===============
 Bulk Java API 
===============




—-
layout: guide
title: Bulk Java API
cat: guide
sidebar: reference\_java\_api
—-

The bulk API allows one to index and delete several documents in a
single request. Here is a sample usage:

::

    import static org.elasticsearch.common.xcontent.XContentFactory.*;

        BulkRequestBuilder bulkRequest = client.prepareBulk();

        // either use client#prepare, or use Requests# to directly build index/delete requestsbulkRequest.add(client.prepareIndex(“twitter”, “tweet”, “1”)
            .setSource(jsonBuilder()
                        .startObject()
                            .field(“user”, “kimchy”)
                            .field(“postDate”, new Date())
                            .field(“message”, “trying out Elastic Search”)
                        .endObject()
                      )
            );

        bulkRequest.add(client.prepareIndex(“twitter”, “tweet”, “2”)
            .setSource(jsonBuilder()
                        .startObject()
                            .field(“user”, “kimchy”)
                            .field(“postDate”, new Date())
                            .field(“message”, “another post”)
                        .endObject()
                      )
            );

        BulkResponse bulkResponse = bulkRequest.execute().actionGet();if (bulkResponse.hasFailures()) {
        // process failures by iterating through each bulk response item}




