# CKIP-Transformers-Word-Segmentation
使用CKIP Transformers進行文字斷詞

如果想使用GPU加快速度可以將

ws_driver = CkipWordSegmenter(level=3,device=-1)

改變成

ws_driver = CkipWordSegmenter(level=3,device=0)

device可以選擇使用第幾張GPU

如果不用GPU設為-1



Word Segmentation斷詞是訓練中文詞嵌入模型重要的前處理

無論簡體或繁體都需要
