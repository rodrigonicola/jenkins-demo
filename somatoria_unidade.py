
def SomarAgora1(valor1, valor2):

    testeinutil = ""

    Resultado = valor1 + valor2

    if (Resultado / 10) < 10 and (Resultado / 10) >= 1:

        print 'O valor digitado e uma dezena'
    elif (Resultado / 100) < 10 and (Resultado / 100) >= 1:
        print 'O valor digitado e uma centena'
    elif (Resultado / 1000) < 10 and (Resultado / 1000) >= 1:
        print 'O valor digitado e uma milhar'
    elif (Resultado / 10000) < 10 and (Resultado / 10000) >= 1:
        print 'O valor digitado e uma dezena de milhar'
    else:
        print 'O valor digitado e uma unidade'


SomarAgora1(2, 10)
