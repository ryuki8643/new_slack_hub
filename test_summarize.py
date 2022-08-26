from qiita import qiita_rss, qiita_API

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("Pysummarization:")
    for texts in qiita_API.summaries_of_qiita_pop():
        print(texts)