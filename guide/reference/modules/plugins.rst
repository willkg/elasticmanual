
=========
 Plugins 
=========




—-
layout: guide
title: Plugins
cat: guide
sidebar: reference\_modules
—-

Plugins
=======

Plugins are a way to enhance the basic elasticsearch functionality in a
custom manner. They range from adding custom mapping types, custom
analyzers (in a more built in fashion), native scripts, custom discovery
and more.

Installing plugins
------------------

Installing plugins can either be done manually by placing them under the
``plugins`` directory, or using the ``plugin`` script. Several plugins
can be found under the
`elasticsearch <https://github.com/elasticsearch>`_ organization in
GitHub, starting with ``elasticsearch-``.

Plugins can also be automatically downloaded and installed from gitub
using: ``user_name/repo_name`` structure, or, for explicit versions,
using ``user_name/repo_name/version_number``. When no version number is
specified, first a version based on the elasticsearch version is tried,
and if it does not work, then master is used.

Site Plugins
------------

Plugins can have “sites” in them, any plugin that exists under the
``plugins`` directory with a ``_site`` directory, its content will be
statically served when hitting ``/_plugin/[plugin_name]/`` url. Those
can be added even after the process has started.

Installed plugins that do not contain any java related content, will
automatically be detected as site plugins, and their content will be
moved under ``_site``.

The ability to install plugins from github allows to easily install site
plugins hosted there, for example, running:

::

    bin/plugin -install mobz/elasticsearch-head
    bin/plugin -install lukas-vlcek/bigdesk

Will install both of those site plugins, with ``elasticsearch-head``
available under ``http://localhost:9200/_plugin/head/`` and ``bigdesk``
available under ``http://localhost:9200/_plugin/bigdesk/``.



