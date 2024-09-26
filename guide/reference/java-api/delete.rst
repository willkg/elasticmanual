
=================
 Delete Java API 
=================




—-
layout: guide
title: Delete Java API
cat: guide
sidebar: reference\_java\_api
—-

The delete API allows to delete a typed JSON document from a specific
index based on its id. The following example deletes the JSON document
from an index called twitter, under a type called tweet, with id valued
1:

::

    DeleteResponse response = client.prepareDelete(“twitter”, “tweet”, “1”)
            .execute()
            .actionGet();

For more information on the delete operation, check out the `delete
API </guide/reference/api/delete.html>`_ docs.

Operation Threading
===================

The delete API allows to set the threading model the operation will be
performed when the actual execution of the API is performed on the same
node (the API is executed on a shard that is allocated on the same
server).

The options are to execute the operation on a different thread, or to
execute it on the calling thread (note that the API is still async). By
default, ``operationThreaded`` is set to ``true`` which means the
operation is executed on a different thread. Here is an example that
sets it to ``false``:

::

    DeleteResponse response = client.prepareDelete(“twitter”, “tweet”, “1”)
            .setOperationThreaded(false)
            .execute()
            .actionGet();




