
==================
 Pattern Analyzer 
==================




—-
layout: guide
title: Pattern Analyzer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

An analyzer of type ``pattern`` that can flexibly separate text into
terms via a regular expression. Accepts the following settings:

The following are settings that can be set for a ``pattern`` analyzer
type:

Setting
Description
``lowercase``
Should terms be lowercased or not. Defaults to ``true``.
``pattern``
The regular expression pattern, defaults to ``\W+``.
``flags``
The regular expression flags.
**IMPORTANT**: The regular expression should match the **token
separators**, not the tokens themselves.

Flags should be pipe-separated, eg ``"CASE_INSENSITIVE|COMMENTS"``.
Check `Java Pattern
API <http://download.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#field_summary>`_
for more details about ``flags`` options.

Pattern Analyzer Examples
-------------------------

In order to try out these examples, you should delete the ``test`` index
before running each example:

::

        curl -XDELETE localhost:9200/test

Whitespace tokenizer
~~~~~~~~~~~~~~~~~~~~

::

        curl -XPUT 'localhost:9200/test’ -d '
        {
            “settings”:{
                “analysis”: {
                    “analyzer”: {
                        “whitespace”:{
                            “type”: “pattern”,
                            “pattern”:”\\s+”
                        }
                    }
                }
            }
        }’

        curl 'localhost:9200/test/_analyze?pretty=1&analyzer=whitespace’ -d 'foo,bar baz’
        # “foo,bar”, “baz”

Non-word character tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::


        curl -XPUT 'localhost:9200/test’ -d '
        {
            “settings”:{
                “analysis”: {
                    “analyzer”: {
                        “nonword”:{
                            “type”: “pattern”,
                            “pattern”:”[^\\w]+”
                        }
                    }
                }
            }
        }’

        curl 'localhost:9200/test/_analyze?pretty=1&analyzer=nonword’ -d 'foo,bar baz’
        # “foo,bar baz” becomes “foo”, “bar”, “baz”

        curl 'localhost:9200/test/_analyze?pretty=1&analyzer=nonword’ -d 'type_1-type_4’
        # “type_1”,“type_4”

        

CamelCase tokenizer
~~~~~~~~~~~~~~~~~~~

::


        curl -XPUT 'localhost:9200/test?pretty=1’ -d '
        {
            “settings”:{
                “analysis”: {
                    “analyzer”: {
                        “camel”:{
                            “type”: “pattern”,
                            “pattern”:”(\\p{L}\\d]+)|(?<=\\D)(?=\\d)|(?<=\\d)(?=\\D)|(?<=[\\p{L}&&[\\p{Lu}]])(?=\\p{Lu})|(?<=\\p{Lu})(?=\\p{Lu}[\\p{L}&&[^\\p{Lu}]])”
                        }
                    }
                }
            }
        }’

        curl 'localhost:9200/test/_analyze?pretty=1&analyzer=camel’ -d '
            MooseX::FTPClass2_beta
        '
        # “moose”,“x”,“ftp”,“class”,“2”,“beta”

        

The regex above is easier to understand as:

::


          ([^\\p{L}\\d]+)                 # swallow non letters and numbers,
        | (?<=\\D)(?=\\d)                 # or non-number followed by number,
        | (?<=\\d)(?=\\D)                 # or number followed by non-number,
        | (?<=[ \\p{L} && [^\\p{Lu}]])    # or lower case
          (?=\\p{Lu})                     #   followed by upper case,
        | (?<=\\p{Lu})                    # or upper case
          (?=\\p{Lu}                      #   followed by upper case
            [\\p{L}&&[^\\p{Lu}]]          #   then lower case
          )




