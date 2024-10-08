
======
 Node 
======




—-
layout: guide
title: Node
cat: guide
sidebar: reference\_modules
—-

**elasticsearch** allows to configure a node to either be allowed to
store data locally or not. Storing data locally basically means that
shards of different indices are allowed to be allocated on that node. By
default, each node is considered to be a data node, and it can be turned
off by setting ``node.data`` to ``false``.

This is a powerful setting allowing to simply create smart load
balancers that take part in some of different API processing. Lets take
an example:

We can start a whole cluster of data nodes which do not even start an
HTTP transport by setting ``http.enabled`` to ``false``. Such nodes will
communicate with one another using the `transport <transport.html>`_
module. In front of the cluster we can start one or more “non data”
nodes which will start with HTTP enabled. All HTTP communication will be
performed through these “non data” nodes.

The benefit of using that is first the ability to create smart load
balancers. These “non data” nodes are still part of the cluster, and
they redirect operations exactly to the node that holds the relevant
data. The other benefit is the fact that for scatter / gather based
operations (such as search), these nodes will take part of the
processing since they will start the scatter process, and perform the
actual gather processing.

This relieves the data nodes to do the heavy duty of indexing and
searching, without needing to process HTTP requests (parsing), overload
the network, or perform the gather processing.



