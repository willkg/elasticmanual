
========================
 Search API – Explain 
========================




—-
layout: guide
title: Search API – Explain
cat: guide
sidebar: reference\_api\_search
—-

Enables explanation for each hit on how its score was computed.

::

    {
        “explain”: true,
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }




