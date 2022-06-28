import cProfile
import pstats
import module

def repeat(iterations):
    for _ in range(iterations):
        module.my_min(2.3, 3.4, 1.2)
        module.my_max(2.3, 3.4, 1.2)
        module.my_mean(2.3, 3.4, 1.2)
        module.my_median(2.3, 3.4, 1.2)
        module.my_list_min([2.3, 3.4, 1.2])
        module.my_list_max([2.3, 3.4, 1.2])
        module.my_list_mean([2.3, 3.4, 1.2])
        module.my_list_median([2.3, 3.4, 1.2])

cProfile.run('repeat(100_000)', 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
