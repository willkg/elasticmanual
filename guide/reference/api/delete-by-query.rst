
=====================
 Delete By Query API 
=====================




—-
layout: guide
title: Delete By Query API
cat: guide
sidebar: reference\_api
—-

The delete by query API allows to delete documents from one or more
indices and one or more types based on a query. The query can either be
provided using a simple query string as a parameter, or using the `Query
DSL </guide/reference/query-dsl>`_ defined within the request body. Here
is an example:

::

    $ curl -XDELETE 'http://localhost:9200/twitter/tweet/_query?q=user:kimchy’

        $ curl -XDELETE 'http://localhost:9200/twitter/tweet/_query’ -d '{
        “term” : { “user” : “kimchy” }}'

Both above examples end up doing the same thing, which is delete all
tweets from the twitter index for a certain user. The result of the
commands is:

::

    {
        “ok” : true,
        “_indices” : {
            “twitter” : { 
                “_shards” : {
                    “total” : 5,
                    “successful” : 5,
                    “failed” : 0
                }
            }
        }
    }

Note, delete by query bypasses versioning support. Also, it is not
recommended to delete “large chunks of the data in an index”, many
times, its better to simply reindex into a new index.

Multiple Indices and Types
==========================

The delete by query API can be applies to multiple types within an
index, and across multiple indices. For example, we can delete all
documents across all types within the twitter index:

::

    $ curl -XDELETE 'http://localhost:9200/twitter/_query?q=user:kimchy’

We can also delete within specific types:

::

    $ curl -XDELETE 'http://localhost:9200/twitter/tweet,user/_query?q=user:kimchy’

We can also delete all tweets with a certain tag across several indices
(for example, when each user has his own index):

::

    $ curl -XDELETE 'http://localhost:9200/kimchy,elasticsearch/_query?q=tag:wow’

Or even delete across all indices:

::

    $ curl -XDELETE 'http://localhost:9200/_all/_query?q=tag:wow’

Request Parameters
==================

When executing a delete by query using the query parameter ``q``, the
query passed is a query string using Lucene query parser. There are
additional parameters that can be passed:

Name
Description
df
The default field to use when no field prefix is defined within the
query.
analyzer
The analyzer name to be used when analyzing the query string.
default\_operator
The default operator to be used, can be ``AND`` or ``OR``. Defaults to
``OR``.
Request Body
============

The delete by query can use the `Query
DSL </guide/reference/query-dsl>`_ within its body in order to express
the query that should be executed and delete all documents. The body
content can also be passed as a REST parameter named ``source``.

Distributed
===========

The delete by query API is broadcast across all primary shards, and from
there, replicated across all shards replicas.

Routing
=======

The routing value (a comma separated list of the routing values) can be
specified to control which shards the delete by query request will be
executed on.

Replication Type
================

The replication of the operation can be done in an asynchronous manner
to the replicas (the operation will return once it has be executed on
the primary shard). The ``replication`` parameter can be set to
``async`` (defaults to ``sync``) in order to enable it.

Write Consistency
=================

Control if the operation will be allowed to execute based on the number
of active shards within that partition (replication group). The values
allowed are ``one``, ``quorum``, and ``all``. The parameter to set it is
``consistency``, and it defaults to the node level setting of
``action.write_consistency`` which in turn defaults to ``quorum``.

For example, in a N shards with 2 replicas index, there will have to be
at least 2 active shards within the relevant partition (``quorum``) for
the operation to succeed. In a N shards with 1 replica scenario, there
will need to be a single shard active (in this case, ``one`` and
``quorum`` is the same).



