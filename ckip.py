import logging
import time
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker

# 对input.txt的文件分词输出到output.txt中
# 开20个进程

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

ws_driver = CkipWordSegmenter(level=3,device=-1)


# ------------------test--------------------------#
# text = [
#    "傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。",
#    "美國參議院針對今天總統布什所提名的勞工部長趙小蘭展開認可聽證會，預料她將會很順利通過參議院支持，成為該國有史以來第一位的華裔女性內閣成員。",
#    "空白 也是可以的～",
# ]
# ws  = ws_driver(text)
# print(ws)
# ------------------test--------------------------#

#
output = open('ckip.txt', 'w', encoding='utf-8')
with open('chinese.txt', 'r', encoding='utf-8') as content :
    for texts_num, line in enumerate(content):
        line = line.strip('\n')
        # words = jieba.cut(line, cut_all=False)
        line = str(line)
        line = [(line)]
        # print(line)
        words = ws_driver(line)
        # print(words)
        for word in words:
            # print("Here")
            # print(word)
            word = str(word)
            output.write(word + ' ')
        output.write('\n')

        if (texts_num + 1) % 10000 == 0:
            logging.info("已完成前 %d 行的斷詞" % (texts_num + 1))
output.close()

