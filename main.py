import os
import sys

sys.dont_write_bytecode = True

from qiita.throw_qiita_toslack import *
from zenn.throw_zenn_toslack import *
from itmedia.throw_itmedia_toslack import *

# アプリを起動します
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
