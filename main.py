from ingresso import Ingresso, IngressoVip

ingresso = Ingresso(10)

vip = IngressoVip(10, 5)

def menu():
    try:
        print('*' * 30)
        print('BILHETERIA BARUC')
        print('*' * 30)        
        print('1- Ingresso')
        print('2- Ingresso Vip')
        opcao = int(input('Escolha uma opção: '))
        print('*' * 30)
    except ValueError:
        print('Opção Inválida!')
        main()
    return opcao  

   
def submenu(opcao):
    try:
        if opcao == 1:            
            print(f'Ingresso no valor de: {ingresso.getValor():.2f}') 
            main()
        if opcao == 2:
            print(f'Ingresso no valor de: {vip.getAdicional():.2f}') 
            main()
    except ValueError:
            print('Opção inválida')
            main()


def main():
   retornaOpcao = menu() 
   retornaSubmenu = submenu(retornaOpcao)
   return retornaSubmenu

if __name__ == '__main__':
    main()