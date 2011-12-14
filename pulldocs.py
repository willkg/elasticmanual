#!/usr/bin/python2.7

import os
import sys
import textwrap
import subprocess

USAGE = 'pulldocs.py <guide-directory>'
MANUALSOURCE = 'manualsource'
GUIDE = 'guide'

TEMPLATE = """
===========
 %(title)s
===========

.. include:: %(filename)s
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


def convert_file(filepath, src, dst):
    print filepath, src, dst
    exec_program([
            '/usr/bin/pandoc',
            '--from=textile',
            '--to=rst',
            '--output',
            '%s' % dst,
            '%s' % src])


def build_file_skeleton(root, filepath):
    filename = os.path.join(root, GUIDE, filepath.replace(os.sep, '_'))
    filename = os.path.splitext(filename) + '.rst'
    if os.path.exists(filename):
        return

    t = TEMPLATE % {
        'title': os.path.split(os.path.splitext(filename)[0])[-1],
        'filename': os.path.join(MANUALSOURCE, filepath)
        }

    f = open(filename, 'w')
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
    print 'found %d files' % len(file_list)

    root = os.getcwd()
    guide_dir = os.path.join(root, MANUALSOURCE)

    for src in file_list:
        filepath = src[len(src_directory):]
        dst = os.path.join(guide_dir, filepath)
        dst = os.path.splitext(dst)[0] + '.rst'
        dst_dir = os.path.dirname(dst)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        convert_file(filepath, src, dst)

        build_file_skeleton(root, filepath)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
