
def SomarAgora1(valor1, valor2):

    resultado = valor1 + valor2

    if (resultado / 10) < 10 and (resultado / 10) >= 1:

        print 'O valor digitado e uma dezena'
    elif (resultado / 100) < 10 and (resultado / 100) >= 1:
        print 'O valor digitado e uma centena'
    elif (resultado / 1000) < 10 and (resultado / 1000) >= 1:
        print 'O valor digitado e uma milhar'
    elif (resultado / 10000) < 10 and (resultado / 10000) >= 1:
        print 'O valor digitado e uma dezena de milhar'
    else:
        print 'O valor digitado e uma unidade'


SomarAgora1(2, 10)
