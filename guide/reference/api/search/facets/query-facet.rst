
=============================
 Search API – Query Facets 
=============================




—-
layout: guide
title: Search API – Query Facets
cat: guide
sidebar: reference\_api\_search\_facets
—-

A facet query allows to return a count of the hits matching the facet
query. The query itself can be expressed using the Query DSL. For
example:

::

    {
        “facets” : {
            “wow_facet” : {
                “query” : {
                    “term” : { “tag” : “wow” }
                }
            }
        }
    }    




