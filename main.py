import timeit
from argparse import Namespace
import argparse
from datetime import timedelta
from common.constants import RMUArgParser


def main():
    args: Namespace = setup_argparser()
    start_time: float = timeit.default_timer()

    print(f"ARGS: {args}")
    if args.command in RMUArgParser.UTILITY_COMMANDS:
        print(args.command[0])

    else:
        print(f"else: {args}")

    time_elapsed: float = timeit.default_timer() - start_time
    print(f"The operation took {str(timedelta(seconds=time_elapsed))}")


def setup_argparser() -> Namespace:
    parser = argparse.ArgumentParser(description="utility to aid in day to day operations")
    subparsers = parser.add_subparsers(help="commands", dest="command", required=True)

    utility_parser = subparsers.add_parser("util", help="all utility functions")
    utility_parser.add_argument("--kill-java", help="kills all current java processes", dest="kill_java", action="store_true")
    utility_parser.add_argument("--cherry-pick-logs", help="retrieves all commits ready for cherry-picking", action="store_true")
    utility_parser.add_argument("--health-check", help="uses the console to display all current running java processes", action="store_true")
    utility_parser.add_argument("--clear-logs", help="removes all logs in known log or temp dirs for a given project", action="store_true")

    git_parser = subparsers.add_parser("git", help="utility for most git commands")
    git_parser.add_argument("--pull", help="pulls all repos in focus branch (from remote base branch)", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
