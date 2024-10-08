
====================
 Nodes Shutdown API 
====================




—-
layout: guide
title: Nodes Shutdown API
cat: guide
sidebar: reference\_api
—-

The nodes shutdown API allows to shutdown one or more (or all) nodes in
the cluster. Here is an example of shutting the ``_local`` node the
request is directed to:

::

    $ curl -XPOST 'http://localhost:9200/_cluster/nodes/_local/_shutdown’

Specific node(s) can be shutdown as well using their respective node ids
(or other selective options as explained `here <index.html.>`_):

::

    $ curl -XPOST 'http://localhost:9200/_cluster/nodes/nodeId1,nodeId2/_shutdown’

The master (of the cluster) can also be shutdown using:

::

    $ curl -XPOST 'http://localhost:9200/_cluster/nodes/_master/_shutdown’

Finally, all nodes can be shutdown using one of the options below:

::

    $ curl -XPOST 'http://localhost:9200/_shutdown’

        $ curl -XPOST 'http://localhost:9200/_cluster/nodes/_shutdown’

        $ curl -XPOST 'http://localhost:9200/_cluster/nodes/_all/_shutdown’

Delay
=====

By default, the shutdown will be executed after a 1 seconds delay
(``1s``). The delay can be customized by setting the ``delay`` parameter
in a time value format. For example:

::

    $ curl -XPOST 'http://localhost:9200/_cluster/nodes/_local/_shutdown?delay=10s’




