#Função criada para enviar uma mensagem
#Tem MENSAGEM e NOME como parâmetros
def saudacao(msg, nome):
    return f'{msg}, {nome}'

#Função criada para montar e executar outra função. 
#Tem uma FUNÇÃO e seu ARGUMENTO como parâmetros
def executa(funcao, *args):
    return funcao(*args)

print(
    executa(
        saudacao, 'Bom dia', 'Vinicius'))

#O print executa a função EXECUTA, que recebe os argumentos
#passados dentro do print:  SAUDACAO (funcao), 'Bom dia' (arg) 
#e 'Vinicius' (arg). A funcao EXECUTA é executada e retorna
#saudacao('Bom dia', 'Vinicius'), executando a função SAUDACAO
#que, por sua vez, retorna a string com os argumentos   
