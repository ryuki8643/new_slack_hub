import sys

sys.dont_write_bytecode = True

from qiita import qiita


def main():
    qiita.read_rss_qiita()


if __name__ == '__main__':
    main()
