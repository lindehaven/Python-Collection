'''Profilerar modulen fibonacci1'''
import cProfile
import pstats
import fibonacci1
cProfile.run('fibonacci1.fibonacci(37)', 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
