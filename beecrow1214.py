# encoding : utf-8
ordem = int(input())
for i in range(ordem):
    array = [int(i) for i in input().split(" ")]
    media = sum(array[1:]) / float(array[0])
    print(
        "%.3f%%" % (100.0 * len([k for k in array[1:] if k > media]) / float(array[0]))
    )
