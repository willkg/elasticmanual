
==================
 Delete Index API 
==================




—-
layout: guide
title: Delete Index API
cat: guide
sidebar: reference\_api
—-

The delete index API allows to delete an existing index.

::

    $ curl -XDELETE 'http://localhost:9200/twitter/’

The above example deletes an index called ``twitter``.

The delete index API can also be applied to more than one index, or on
``_all`` indices (be careful!). All indices will also be deleted when no
specific index is provided. In order to disable allowing to delete all
indices, set ``action.disable_delete_all_indices`` setting in the config
to ``true``.



