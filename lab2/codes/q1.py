import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start = -np.pi, stop = np.pi, num = 1000)

#exponential
y1 = np.exp(x)
y1t1 = 1 + x
y1t2 = y1t1 + (x**2)/2
y1t3 = y1t2 + (x**3)/6

plt.plot(x, y1, 'k', linewidth = 2, label = r'$y$')
plt.plot(x, y1t1, 'k:', label = r'$p_1$')
plt.plot(x, y1t2, 'k--', label = r'$p_2$')
plt.plot(x, y1t3, 'k', label = r'$p_3$')
plt.legend()
plt.xlabel(r'$x$')                                                                           
plt.ylabel(r'$y$') 
plt.grid(True)
plt.figure()
plt.plot(x, np.abs(y1t1 - y1), 'k:', label = r'$e_1$')
plt.plot(x, np.abs(y1t2 - y1), 'k--', label = r'$e_2$')
plt.plot(x, np.abs(y1t3 - y1), 'k', label = r'$e_3$')
plt.grid(True)
plt.legend()
plt.xlabel(r'$x$')                                                                        
plt.ylabel('error')

#logarithmic
y2 = np.log(x)
y2t1 = x - 1
y2t2 = y2t1 - ((x-1)**2)/2
y2t3 = y2t2 + ((x-1)**3)/6
plt.figure()
plt.plot(x, y2, 'k', linewidth = 2, label = r'$y$')
plt.plot(x, y2t1, 'k:', label = r'$p_1$')                                            
plt.plot(x, y2t2, 'k--', label = r'$p_2$')                           
plt.plot(x, y2t3, 'k', label = r'$p_3$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()                                                                                 
plt.grid(True)                                                                               
plt.figure()                                                                                 
plt.plot(x, np.abs(y2t1 - y2), 'k:', label = r'$e_1$')                                       
plt.plot(x, np.abs(y2t2 - y2), 'k--', label = r'$e_2$')                                      
plt.plot(x, np.abs(y2t3 - y2), 'k', label = r'$e_3$')                                        
plt.xlabel(r'$x$')
plt.ylabel('error')
plt.grid(True)                                                                               
plt.legend()
plt.xlabel(r'$x$')                                                                        
plt.ylabel('error')

#sine
y3 = np.sin(x)
y3t1 = x
y3t2 = y3t1
y3t3 = y3t2 - (x**3)/6

plt.figure()
plt.plot(x, y3, 'k', linewidth = 2, label = r'$y$')                              
plt.plot(x, y3t1, 'k:', label = r'$p_1$')                                            
plt.plot(x, y3t2, 'k--', label = r'$p_2$')                           
plt.plot(x, y3t3, 'k', label = r'$p_3$')             
plt.legend()
plt.xlabel(r'$x$')                                                                           
plt.ylabel(r'$y$') 
plt.grid(True)                                                                               
plt.figure()                                                                                 
plt.plot(x, np.abs(y3t1 - y3), 'k:', label = r'$e_1$')                                       
plt.plot(x, np.abs(y3t2 - y3), 'k--', label = r'$e_2$')                                      
plt.plot(x, np.abs(y3t3 - y3), 'k', label = r'$e_3$')                                        
plt.grid(True)                                                                               
plt.legend()
plt.xlabel(r'$x$')                                                                        
plt.ylabel('error')

#cosine
y4 = np.cos(x)
y4t1 = x - x + 1
y4t2 = 1 - (x**2)/2
y4t3 = y4t2

plt.figure()                                                                              
plt.plot(x, y4, 'k', linewidth = 2, label = r'$y$')                              
plt.plot(x, y4t1, 'k:', label = r'$p_1$')                                             
plt.plot(x, y4t2, 'k--', label = r'$p_2$')                                            
plt.plot(x, y4t3, 'k', label = r'$p_3$')                            
plt.legend()
plt.xlabel(r'$x$')                                                                           
plt.ylabel(r'$y$') 
plt.grid(True)                                                                               
plt.figure()                                                                                 
plt.plot(x, np.abs(y4t1 - y4), 'k:', label = r'$e_1$')                                       
plt.plot(x, np.abs(y4t2 - y4), 'k--', label = r'$e_2$')                                      
plt.plot(x, np.abs(y4t3 - y4), 'k', label = r'$e_3$')                                        
plt.grid(True)                                                                               
plt.legend()
plt.xlabel(r'$x$')                                                                        
plt.ylabel('error')

plt.show()
