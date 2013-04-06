# coding: utf-8
import sys
import argparse
from storage import Storage


storage = Storage()


def list_labels():
    labels = storage.get_all()
    for label, path in labels.iteritems():
        print label, '\t\t', path


def change_directory(label):
    try:
        path = storage.get(label)
        print '<PATH>'
        print path
    except:
        sys.stderr.write('%s is not a valid label.\n' % label)
        sys.exit(1)


def main():
    """Entrypoint for the `goto` utility."""
    parser = argparse.ArgumentParser()
    parser.add_argument('label', nargs='?', help='name of the label')

    args = parser.parse_args()

    storage.open_or_create()

    if args.label:
        change_directory(args.label)
    else:
        list_labels()