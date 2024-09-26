
============
 Not Filter 
============




—-
layout: guide
title: Not Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A filter that filters out matched documents using a query. This filter
is more performant then `bool <bool-filter.html>`_ filter. Can be placed
within queries that accept a filter.

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “not” : {
                    “range” : {
                        “postDate” : {
                            “from” : “2010-03-01”,
                            “to” : “2010-04-01”
                        }
                    }
                }
            }
        }
    }

Or, in a longer form with a ``filter`` element:

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “not” : {
                    “filter” :  {
                        “range” : {
                            “postDate” : {
                                “from” : “2010-03-01”,
                                “to” : “2010-04-01”
                            }
                        }
                    }
                }
            }
        }
    }

Caching
=======

The result of the filter is not cached by default. The \`\_cache\` can
be set to \`true\` in order to cache it (tough usually not needed). Here
is an example:

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “not” : {
                    “filter” :  {
                        “range” : {
                            “postDate” : {
                                “from” : “2010-03-01”,
                                “to” : “2010-04-01”
                            }
                        }
                    },
                    “_cache” : true
                }
            }
        }
    }




