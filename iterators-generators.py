# iterators/イテレータ
# with list/listを用いて
for i in [1, 2, 3, 4]:
    print(i)
# with range!
for i in range(5, 2, -1):
    print(i)
# with string/文字列を用いて
for c in "python":
    print(c)
# with dictionary
for k in {"x": 1, "y": 2}:
    print(k)
# with file!
for line in open("a.txt"):
    print(line)

# これでiteratorと直接に接触することができます。
anIterator = iter("python")
next(anIterator)
next(anIterator)
next(anIterator)
next(anIterator)
next(anIterator)
next(anIterator)

# 自分の好きなIteratorは作れることができますよ！
# __next__関数を定義すればいい！
class MyIterator:
    """
    私のすご〜いイテレータ！
    """
    def __init__(self, n):
        self.i = n

    def __next__(self):
        if self.i > 0:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()

    def __iter__(self):
        return self

myIterator = MyIterator(10)
next(myIterator)
next(myIterator)

for i in MyIterator(5):
    print(i)


# Generatorを使って、iteratorを作りましょう！
def reverse_range(n):
    i = n
    while i > 0:
        yield i #yieldキーワードは数列の中の一つの値を返します。
        i -= 1
r = reverse_range(4)
print(next(r))
print(next(r))
for i in reverse_range(10):
	print(i)

# Generatorは格好いい！
a = (x*x for x in range(10))
sum(a)
# []を使うとlistも作れます
l = [x*x for x in range(10)]
print(l)
# pythagorean triplesの計算！
pyt = ((x, y, z) for z in range(100) for y in range(0, z) for x in range(0, y) if x*x + y*y == z*z)
print(list(pyt))
