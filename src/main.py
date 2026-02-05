from problems.problem_switcher import execute
import sys


"""main"""
def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    print("argv:", argv)
    if len(argv) > 0:
        execute(argv[0])
    return


"""entry point"""
if __name__ == "__main__":
    main()
