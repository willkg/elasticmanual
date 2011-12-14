#!/usr/bin/python2.7

import os
import sys
import textwrap
import subprocess

USAGE = 'pulldocs.py <guide-directory>'
HEADERS = '_headers'
FOOTERS = '_footers'
GUIDE = 'guide'
MANUALSOURCE = '_manualsource'

TEMPLATE = """
%(title)s

%(header)s

%(rst)s

%(footer)s
"""


def wrap(text, indent=''):
    return (
        textwrap.TextWrapper(initial_indent=indent, subsequent_indent=indent)
        .wrap(text))


def wrap_paragraphs(text):
    text = ['\n'.join(textwrap.wrap(mem)) for mem in text.split('\n\n')]
    return '\n\n'.join(text)


def err(*output, **kwargs):
    """Writes output to stderr.

    :arg wrap: If you set ``wrap=False``, then ``err`` won't textwrap
    the output.

    """
    output = 'Error: ' + ' '.join([str(o) for o in output])
    if kwargs.get('wrap') != False:
        output = '\n'.join(wrap(output, kwargs.get('indent', '')))
    elif kwargs.get('indent'):
        indent = kwargs['indent']
        output = indent + ('\n' + indent).join(output.splitlines())
    sys.stderr.write(output + '\n')


def out(*output, **kwargs):
    """Writes output to stdout.

    :arg wrap: If you set ``wrap=False``, then ``out`` won't textwrap
    the output.

    """
    output = ' '.join([str(o) for o in output])
    if kwargs.get('wrap') != False:
        output = '\n'.join(wrap(output, kwargs.get('indent', '')))
    elif kwargs.get('indent'):
        indent = kwargs['indent']
        output = indent + ('\n' + indent).join(output.splitlines())
    sys.stdout.write(output + '\n')


def exec_program(args):
    return subprocess.check_output(args)


def build_file_list(src_directory):
    file_list = []

    for root, dirs, files in os.walk(src_directory):
        file_list.extend([os.path.join(src_directory, root, f)
                          for f in files
                          if f.endswith('textile')])

    return file_list


def convert_file(filepath, src):
    dst = source_file(filepath)
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    exec_program([
            '/usr/bin/pandoc',
            '--from=textile',
            '--to=rst',
            '--output',
            '%s' % dst,
            '%s' % src])


def get_root():
    return os.getcwd()


def guide_file(filepath):
    filename = os.path.join(get_root(), GUIDE, filepath)
    filename = os.path.splitext(filename)[0] + '.rst'
    return filename


def source_file(filepath):
    filename = os.path.join(get_root(), MANUALSOURCE, filepath)
    filename = os.path.splitext(filename)[0] + '.rst'
    return filename


def get_header(filepath):
    filename = os.path.join(get_root(), HEADERS, filepath)
    filename = os.path.splitext(filename)[0] + '.rst'
    if os.path.exists(filename):
        return open(filename, 'r').read()

    return ''


def get_footer(filepath):
    filename = os.path.join(get_root(), FOOTERS, filepath)
    filename = os.path.splitext(filename)[0] + '.rst'
    if os.path.exists(filename):
        return open(filename, 'r').read()

    return ''


def build_file_skeleton(filepath):
    dst = guide_file(filepath)
    manual_src = source_file(filepath)
    if os.path.exists(dst):
        return

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    data = open(manual_src, 'r').readlines()
    title = [t for t in data if t.startswith('title: ')]
    if title:
        title = title[0][7:].strip()
    else:
        title = 'unknown'

    title = (('=' * (len(title) + 2)) + '\n' + 
             ' ' + title + ' ' + '\n' + 
             ('=' * (len(title) + 2)) +
             '\n')


    t = TEMPLATE % {
        'title': title,
        'header': get_header(filepath),
        'rst': ''.join(data),
        'footer': get_footer(filepath),
        }

    f = open(dst, 'w')
    f.write(t)
    f.close()


def main(argv):
    out(USAGE)
    if not argv:
        err('Please specify guide/ directory.')
        return 1

    # test pandoc
    try:
        exec_program(['/usr/bin/pandoc', '--version'])
    except (OSError, subprocess.CalledProcessError):
        err('pandoc not installed.  Please install pandoc.')
        return 1

    src_directory = os.path.abspath(argv[0])
    if not src_directory.endswith(os.sep):
        src_directory += os.sep
    if not os.path.exists(src_directory):
        err('guide directory "%s" does not exist' % src_directory)
        return 1

    file_list = build_file_list(src_directory)
    out('found %d files' % len(file_list))

    for src in file_list:
        out("working on %s...." % src, wrap=False)
        filepath = src[len(src_directory):]

        convert_file(filepath, src)

        build_file_skeleton(filepath)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
