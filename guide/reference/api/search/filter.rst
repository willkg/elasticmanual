
=======================
 Search API – Filter 
=======================




—-
layout: guide
title: Search API – Filter
cat: guide
sidebar: reference\_api\_search
—-

When doing things like facet navigation, sometimes only the hits are
needed to be filtered by the chosen facet, and all the facets should
continue to be calculated based on the original query. The ``filter``
element within the search request can be used to accomplish it.

Note, this is different compared to creating a ``filtered`` query with
the filter, since this will cause the facets to only process the
filtered results.

For example, lets create two tweets, with two different tags:

::

    curl -XPUT 'localhost:9200/twitter/tweet/1’ -d '{
        “message” : “something blue”,
        “tag” : “blue”}'

        curl -XPUT 'localhost:9200/twitter/tweet/2’ -d '{
        “message” : “something green”,
        “tag” : “green”}'

        curl -XPOST 'localhost:9200/_refresh’

We can now search for something, and have a terms facet.

::

    curl -XPOST 'localhost:9200/twitter/_search?pretty=true’ -d '
    {
        “query” : {
            “term” : { “message” : “something” }
        },
        “facets” : {
            “tag” : {
                “terms” : { “field” : “tag” }
            }
        }
    }
    '

We get two hits, and the relevant facets with a count of 1 for both
``green`` and ``blue``. Now, lets say the ``green`` facet is chosen, we
can simply add a filter for it:

::

    curl -XPOST 'localhost:9200/twitter/_search?pretty=true’ -d '
    {
        “query” : {
            “term” : { “message” : “something” }
        },
        “filter” : {
            “term” : { “tag” : “green” }
        },
        “facets” : {
            “tag” : {
                “terms” : { “field” : “tag” }
            }
        }
    }
    '

And now, we get only 1 hit back, but the facets remain the same.

Note, if additional filters is required on specific facets, they can be
added as a ``facet_filter`` to the relevant facets.



