'''Profilerar modulen euler_pi'''
import cProfile
import pstats
import euler_pi

for n in range(1, 7):
    cProfile.run('euler_pi.euler_pi('+str(n)+')', 'euler_pi_stats')
    p = pstats.Stats('euler_pi_stats')
    p.sort_stats('cumulative').print_stats(20)
