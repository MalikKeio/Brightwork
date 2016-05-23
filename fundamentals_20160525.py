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
    print i*4

for i in str_array:
    print i*4


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

# 画像表示を追加する
