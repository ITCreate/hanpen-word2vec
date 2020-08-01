import gensim
import sys
hogeword = sys.argv #コマンドライン引数
hogehoge = gensim.models.Word2Vec.load('./ja/ja.bin') #データベース読み込み
print(hogeword)
print(len(hogeword))
if len(hogeword) == 6:
    UpTab = hogeword[1]
    DownTab = hogeword[2]
    LeftTab = hogeword[3]
    RightTab =  hogeword[4]
    Word = hogeword[5]
    #単語の類似度を表示
    #Y軸の値を算出
    UpAxis = hogehoge.wv.similarity(UpTab,Word) #上下軸の単語と検証する単語の類似性を出す
    DownAxis = hogehoge.wv.similarity(DownTab,Word)
    DownAxis *= -1
    YAxis = DownAxis + UpAxis /2
    #X軸の値を算出
    LeftAxis = hogehoge.wv.similarity(LeftTab,Word)#左右軸の単語と検証する単語の類似性を出す
    RightAxis = hogehoge.wv.similarity(RightTab,Word)
    RightAxis *= -1
    XAxis = RightAxis + LeftAxis /2
    #printでY軸　X軸　wordを入力
    print("XY単語",YAxis,XAxis,Word)
else:
    print("エラー　入力する単語が多すぎるか少なすぎます")
print("デバッグ",UpAxis,DownAxis,LeftAxis,RightAxis)