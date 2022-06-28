'''Profilerar modulen fibonacci2'''
import cProfile
import pstats
import fibonacci2
cProfile.run('fibonacci2.fibonacci(37)', 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
