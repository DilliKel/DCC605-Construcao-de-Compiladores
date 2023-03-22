# Kelvin Araújo Ferreira 2019037653

class Scanner:
    def __init__(self):
        self.table = []  # tabela de lexemas encontrados
    
    def scan(self, code):
        keywords = ['int', 'float', 'char', 'bool']  # palavras-chave da linguagem
        
        # percorre o código fonte caractere por caractere
        i = 0
        while i < len(code):
            char = code[i]
            
            # se o caractere for um espaço em branco, pula para o próximo caractere
            if char.isspace():
                i += 1
            
            # se o caractere for um dígito, começa a ler um número
            elif char.isdigit():
                num = char
                i += 1
                while i < len(code) and code[i].isdigit():
                    num += code[i]
                    i += 1
                self.table.append(('NUM', num))
            
            # se o caractere for uma letra, começa a ler um identificador ou uma palavra-chave
            elif char.isalpha():
                word = char
                i += 1
                while i < len(code) and code[i].isalnum():
                    word += code[i]
                    i += 1
                if word in keywords:
                    self.table.append(('PR', word))
                else:
                    self.table.append(('ID', word))
            
            # se o caractere for um operador ou pontuação, adiciona à tabela
            elif char in '+-*/=();':
                self.table.append(('SYMBOL', char))
                i += 1
            
            # se o caractere não for reconhecido, lança uma exceção
            else:
                raise Exception('Caractere não reconhecido: {}'.format(char))
        
        # adiciona o caractere $ para indicar o final do código fonte
        self.table.append(('END', '$'))

def main(input_file, output_file):
    # lê o código fonte do arquivo de entrada
    with open(input_file, 'r') as f:
        code = f.read()
    
    # realiza a varredura de lexemas
    scanner = Scanner()
    scanner.scan(code)
    
    # escreve a tabela de lexemas no arquivo de saída
    with open(output_file, 'w') as f:
        for lex in scanner.table:
            f.write('{} {}\n'.format(lex[0], lex[1]))

if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'
    main(input_file, output_file)
