lp=float(input('Largura da parede: '))
ap=float(input('Altura da parede: '))
a=(lp*ap)
t=(a/2)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lp, ap, a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(t))