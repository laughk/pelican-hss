import unittest
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

from jinja2 import Environment, FileSystemLoader


class CanonicalParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'head':
            self.in_head = True
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.links.append((self.in_head, attrs.get('href')))

    def handle_endtag(self, tag):
        if tag == 'head':
            self.in_head = False


class CanonicalTests(unittest.TestCase):
    def setUp(self):
        self.env = Environment(loader=FileSystemLoader(
            Path(__file__).resolve().parents[1] / 'templates'))

    def check(self, template, expected, **context):
        values = dict(SITEURL='https://example.com/blog/')
        if template in ('index', 'category', 'tag', 'author'):
            values['articles_page'] = SimpleNamespace(url='index.html', object_list=[])
        values.update(context)
        parser = CanonicalParser()
        parser.feed(self.env.get_template(template + '.html').render(**values))
        self.assertEqual(parser.links, [] if expected is None else [(True, expected)])

    def test_paginated_lists(self):
        for template in ('index', 'category', 'tag', 'author'):
            for url in ('index.html', 'category/test.html', 'listing/page/2/'):
                with self.subTest(template=template, url=url):
                    self.check(template, 'https://example.com/blog/' + url,
                               output_file='different/save/path.html',
                               articles_page=SimpleNamespace(url=url, object_list=[]))

    def test_direct_templates(self):
        for template in ('index', 'archives', 'categories', 'tags', 'authors'):
            with self.subTest(template=template):
                self.check(template, 'https://example.com/blog/' + template + '.html')

    def test_custom_direct_urls(self):
        for template in ('archives', 'categories', 'tags', 'authors'):
            for url in ('custom/', ''):
                with self.subTest(template=template, url=url):
                    self.check(template, 'https://example.com/blog/' + url,
                               **{template.upper() + '_URL': url,
                                  'output_file': 'different/save/path.html'})

    def test_unpaginated_lists(self):
        for template in ('index', 'category', 'tag', 'author'):
            context = {template: SimpleNamespace(url='custom/list/')}
            if template == 'index':
                context = {'canonical_path': 'custom/list/'}
            rendered = self.env.get_template('modules/canonical.html').render(
                SITEURL='https://example.com',
                **context)
            parser = CanonicalParser()
            parser.feed(rendered)
            self.assertEqual(parser.links, [(False, 'https://example.com/custom/list/')])

    def test_content_and_metadata(self):
        for template in ('article', 'page'):
            content = SimpleNamespace(url='posts/test/', title='Test', summary='',
                                      tags=[], category=SimpleNamespace(url='cat.html'))
            self.check(template, 'https://example.com/blog/posts/test/',
                       **{template: content})
            content.canonical_url = 'https://original.example/post?a=1&b="two"'
            self.check(template, content.canonical_url, **{template: content})
            self.check(template, content.canonical_url, SITEURL='', **{template: content})

    def test_empty_siteurl(self):
        for template in ('index', 'category', 'tag', 'author', 'archives',
                         'categories', 'tags', 'authors'):
            self.check(template, None, SITEURL='')

    def test_output_fallback(self):
        self.check('base', 'https://example.com/blog/custom.html',
                   output_file='custom.html')


if __name__ == '__main__':
    unittest.main()
