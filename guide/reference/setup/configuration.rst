
===============
 Configuration 
===============




—-
layout: guide
title: Configuration
cat: guide
sidebar: reference\_setup
—-

**elasticsearch** configuration files can be found under
``ES_HOME/config`` folder. The folder comes with two files, the
``elasticsearch.yml`` for configuring ElasticSearch different
`modules <../modules>`_, and ``logging.yml`` for configuring the
ElasticSearch logging.

Settings
========

The configuration format is `YAML <http://www.yaml.org/>`_. Here is an
example of changing the address all network based modules will use to
bind and publish to:

::

    network :
        host : 10.0.0.4

In production use, you will almost certainly want to change paths for
data and log files:

::

    path:
      logs: /var/log/elasticsearch
      data: /var/data/elasticsearch

Also, don’t forget to give your production cluster a name, which is used
to discover and auto-join other nodes:

::

    cluster:
      name: 

Internally, all settings are collapsed into “namespaced” settings. For
example, the above gets collapsed into ``network.host``. This means that
its easy to support other configuration formats, for example,
`JSON <http://www.json.org>`_. If JSON is a preferred configuration
format, simply rename the ``elasticsearch.yml`` file to
``elasticsearch.json`` and add:

::

    {
        “network” : {
            “host” : “10.0.0.4”
        }
    }

It also means that its easy to provide the settings externally either
using the ``ES_JAVA_OPTS`` or as parameters to the ``elasticsearch``
command, for example:

::

    $ elasticsearch -f -Des.network.host=10.0.0.4

Another option is to use the ``${...}`` notation within the
configuration file which will resolve to an environment setting, for
example:

::

    {
        “network” : {
            “host” : “${ES_NET_HOST}”
        }
    }

The location of the configuration file can be set externally using a
system property:

::

    $ elasticsearch -f -Des.config=/path/to/config/file

Index Settings
==============

Indices created within the cluster can provide their own settings. For
example, the following creates an index with memory based storage
instead of the default file system based one (the format can be either
YAML or JSON):

::

    $ curl -XPUT http://localhost:9200/kimchy/ -d \
    '
    index :
        store:
            type: memory
    '

Index level settings can be set on the node level as well, for example,
within the ``elasticsearch.yml`` file, the following can be set:

::

    index :
        store:
            type: memory

This means that every index that gets created on the specific node
started with the mentioned configuration will store the index in memory
**unless the index explicitly sets it**. In other words, any index level
settings override what is set in the node configuration. Of course, the
above can also be set as a “collapsed” setting, for example:

::

    $ elasticsearch -f -Des.index.store.type=memory

All of the index level configuration can be found within each `index
module </guide/reference/index-modules>`_.

Logging
=======

ElasticSearch uses an internal logging abstraction and comes, out of the
box, with `log4j <http://logging.apache.org/log4j/>`_. It tries to
simplify log4j configuration by using `YAML <http://www.yaml.org/>`_ to
configure it, and the logging configuration file is
``config/logging.yml`` file.



