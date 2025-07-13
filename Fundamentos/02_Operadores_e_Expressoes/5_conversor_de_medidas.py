metros = float(input('digite a medida em metros: '))
print ('a medida de {} corresponde a'.format(metros))
print(' {:.0f} km  \n {:.0f} hm  \n {:.0f}dam \n {:.0f}m \n {:.0f}dm \n {:.0f}cm '  .format(metros/ 1000, metros/ 100, metros/ 10, metros*10,metros* 100, metros* 1000))

