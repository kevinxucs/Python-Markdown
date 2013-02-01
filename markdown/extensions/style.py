"""
Styling Extension for Python-Markdown
=====================================

A.k.a Markupdown. This extension adds styling support to markdown.

Copyright 2013
* [Kaiwen Xu](http://kevxu.net/)

"""

import re
import markdown

class MarkupdownExtension(markdown.Extension):
	""" Styling Extension for Python-Markdown. """

	def extendMarkdown(self, md, md_globals):
		