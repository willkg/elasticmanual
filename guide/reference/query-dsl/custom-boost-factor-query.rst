
===========================
 Custom Boost Factor Query 
===========================




—-
layout: guide
title: Custom Boost Factor Query
cat: guide
sidebar: reference\_query\_dsl
—-

``custom_boost_factor`` query allows to wrap another query and multiply
its score by the provided ``boost_factor``. This can sometimes be
desired since ``boost`` value set on specific queries gets normalized,
while this query boost factor does not.

::

    “custom_boost_factor” : {
        “query” : {
            ....
        },
        “boost_factor” : 5.2
    }




