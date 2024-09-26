
=================
 Wikipedia River 
=================




—-
layout: guide
title: Wikipedia River
cat: guide
sidebar: reference\_river
—-

A simple river to index wikipedia. Create it using:

::

    curl -XPUT localhost:9200/_river/my_river/_meta -d '
    {
        “type” : “wikipedia”
    }
    '

The default download is the latest wikipedia dump
(\`http://download.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2\`).
It can be changed using:

::

    {
        “type” : “wikipedia”,
        “wikipedia” : {
            “url” : “url to link to wikipedia dump”
        }
    }

The index name defaults to the river name, and the type defaults to
page. Both can be changed in the index section:

::

    {
        “type” : “wikipedia”,
        “index” : {
            “name” : “my_index”,
            “type” : “my_type”,
            “bulk_size” : 100
        }
    }




