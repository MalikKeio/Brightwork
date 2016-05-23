######################## numpy ############################
# numpyの標準的な使い方
import numpy as np

# arrayを作りましょう
my_array = np.array( [0,1,2,3] )

# arrayの変数型を返す
my_array.dtype
# arrayの長さを返す
len(my_array)

# 今は64-bit integer型のではないかと思います。
# 編集型を変換することが可能です。例えば、文字列に変換しましょう
str_array = my_array.astype(str)

# これでarrayの差分が表示されます
for i in my_array:
    print(i*4)

for i in str_array:
    print(i*4)


# これは多少listですね。numpyは複数次元arrayにもっと便利です。
dim2_array = np.array([[0,1,2,3], [0,1,2,3], [0,1,2,4]])

# 次元数を返す
dim2_array.ndim
# 行列のサイズ(n,m)を返す
dim2_array.shape
# 要素数(n*m)を返す
dim2_array.size

# arrayの中の全ての変数の平均
np.mean(dim2_array)
# これで、arrayを平たくすることができます
np.mean(dim2_array, axis = 0)
np.mean(dim2_array, axis = 1)

# ！これは最高です！ sliceと言います。
# arrayをコピーする（同じarrayを返す）
dim2_array[:]
# それぞれを実行してみてください。
dim2_array[:2]
dim2_array[:2,:]
dim2_array[:2,:2]
# 逆！
dim2_array[0][::-1]

# csvとして保存
np.savetxt('lookatarray.csv', dim2_array, delimiter = ',')

# csvを開く
np.genfromtxt('lookatarray.csv', delimiter = ',')


######################## matplotlib ############################
# matplotlibとnumpyの全ての関数をglobal namespaceにimportする
# 危険なので、テスト以外は使わないでください。
from pylab import *
# -20から20のiteratorを作成
x = range(-20, 20)
# iterate over x! これは死ぬほど便利です。
y = [i*i for i in x]
# 曲線を描画する
plot(x, y)
# 表示する
show()

################# matplotlibにおける画像処理の簡単な事例 ###########

# 曲線の描画moduleをインポート。表示としてpltと名づけます。
import matplotlib.pyplot as plt
# 画像処理moduleをインポート
import matplotlib.image as mpimg
# 画像を読み込む
img = mpimg.imread('stinkbug.png')
# 画像を描画
plt.imshow(img)
# 新しいWindowを作る
plt.figure()
# sliceのパワー：RGBからRだけを残す。lum_imgは二次元arrayになりました。
lum_img = img[:,:,0]
# 現在のWindow（＝Figure）画像を描画
plt.imshow(lum_img, cmap="hot")
# colorbarを追加する
plt.colorbar()
# 新しいWindowを作る
plt.figure()
# 画像のhistogramを作る
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0))
plt.figure()
# histogramのデータを考慮し、コントラストを増加しよう。
plt.imshow(lum_img, clim=(0.0, 0.7))
plt.colorbar()
# 結局、全てのWindowを表示する
plt.show()
