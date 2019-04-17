from block import Block
from system import System
from train import Train


sys = System('2018-01-01 00:00:00', [20] * 10)
i = 0
while sys.refresh_time < 1000:
    i += 1
    # print(i)
    # print("Train number: {}".format(sys.train_num))
    sys.refresh()

print(sys.train_num)
for t in sys.trains:
    t.print_blk_time()