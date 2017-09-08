
import argparse

# use a function to parse arguments
def parse_arguments(args):
    parser = argparse.ArgumentParser(description='Remember your arguments!')
    parser.add_argument('mode', type=str,
                        help='This is a required argument that specifies some mode setting.')
    parser.add_argument('--option1', nargs='+', type=str,
                        help='This is an optional switch.  Remember to provide a bunch of arguments after it.')
    parser.add_argument('--option2', nargs='+', type=str,
                        help='This is another optional switch that also takes a bunch of arguments after it.')
    return parser.parse_args(args)


# usage
args = parse_arguments(sys.argv[1:])
if args.mode == 'a':
    ...
elif args.mode == 'b':
    ...
else:
    raise Exception

if args.option1:
    x = SomethingTakesManyArgs(*args.option1)
elif args.option2:
    x = SomethingTakesManyArgsAlso(*args.option2)
else:
    raise Exception

# unit testing
import unittest
from util import parse_arguments

class TestUtil(unittest.TestCase):
    def test_parse_arguments(self):
        args = parse_arguments(['mode', '--option1', 'arg1', 'arg2'])
        self.assertEqual(args.mode, 'mode')
        self.assertListEqual(args.option1, ['arg1', 'arg2'])
        self.assertEquals(args.option2, None)
