
==============
 Validate API 
==============




—-
layout: guide
title: Validate API
cat: guide
sidebar: reference\_api
—-

The validate API allows a user to validate a potentially expensive query
without executing it. The following example shows how it can be used:

::

    curl -XPUT 'http://localhost:9200/twitter/tweet/1’ -d '{
        “user” : “kimchy”,
        “post_date” : “2009-11-15T14:12:12”,
        “message” : “trying out Elastic Search”}’

        

When the query is valid, the response contains ``valid:true``:

::

    curl -XGET 'http://localhost:9200/twitter/_validate/query?q=user:foo’
    {“valid”:true,”_shards”:{“total”:1,“successful”:1,failed}}

Or, with a request body:

::

    curl -XGET 'http://localhost:9200/twitter/tweet/_validate/query’ -d '{
      “filtered” : {
        “query” : {
          “query_string” : {
            “query” : “:“
          }
        },
        “filter” : {
          “term” : { “user” : “kimchy” }
        }
      }
    }’
    {“valid”:true,”_shards”:{“total”:1,“successful”:1,failed}}

If the query is invalid, ``valid`` will be ``false``. Here the query is
invalid because ElasticSearch knows the post\_date field should be a
date due to dynamic mapping, and 'foo’ does not correctly parse into a
date:

::

    curl -XGET 'http://localhost:9200/twitter/tweet/_validate/query?q=post_date:foo’
    {“valid”:false,”_shards”:{“total”:1,“successful”:1,failed}}

An ``explain`` parameter can be specified to get more detailed
information about why a query failed:

::

    curl -XGET 'http://localhost:9200/twitter/tweet/_validate/query?q=post_date:foo&pretty=true&explain=true’
    {
      “valid” : false,
      “_shards” : {
        “total” : 1,
        “successful” : 1,
        “failed” : 0
      },
      “explanations” : [ {
        “index” : “twitter”,
        “valid” : false,
        “error” : “org.elasticsearch.index.query.QueryParsingException: [twitter] Failed to parse; org.elasticsearch.ElasticSearchParseException: failed to parse date field [foo], tried both date format [dateOptionalTime], and timestamp number; java.lang.IllegalArgumentException: Invalid format: \“foo\”“
      } ]
    }




