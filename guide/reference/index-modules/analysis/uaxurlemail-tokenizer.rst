
=========================
 UAX Email URL Tokenizer 
=========================




—-
layout: guide
title: UAX Email URL Tokenizer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A tokenizer of type ``uax_url_email`` which works exactly like the
``standard`` tokenizer, but also handles emails and urls.

The following are settings that can be set for a ``uax_url_email``
tokenizer type:

Setting
Description
``max_token_length``
The maximum token length. If a token is seen that exceeds this length
then it is discarded. Defaults to ``255``.



