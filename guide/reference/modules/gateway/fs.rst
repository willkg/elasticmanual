
===================
 Shared FS Gateway 
===================




—-
layout: guide
title: Shared FS Gateway
cat: guide
sidebar: reference\_modules\_gateway
—-

The file system based gateway stores the cluster meta data and indices
in a **shared** file system. Note, since its a distributed system, the
file system should be shared between all different nodes. Here is an
example config to enable it:

::

    gateway:
        type: fs

location
========

The location where the gateway stores the cluster state can be set using
the ``gateway.fs.location`` setting. By default, it will be stored under
the ``work`` directory. Note, the ``work`` directory is considered a
temporal directory with ElasticSearch (meaning it is safe to ``rm -rf``
it), the default location of the persistent gateway in work intentional,
**it should be changed**.

When explicitly specifying the ``gateway.fs.location``, each node will
append its ``cluster.name`` to the provided location. It means that the
location provided can safely support several clusters.

concurrent\_streams
===================

The ``gateway.fs.concurrent_streams`` allow to throttle the number of
streams (per node) opened against the shared gateway performing the
snapshot operation. It defaults to ``5``.



