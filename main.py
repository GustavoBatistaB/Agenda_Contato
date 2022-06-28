import sqlite3,os,time,winsound
from click import confirm

from colorama import Cursor

class Manager:
    def __init__(self): 
        self.name =''
        self.phone=''
        self.address=''
    
    def add(self):
        running = True
        while running:
            os.system('cls')
            print('----- Adicionar um novo contato ----')
            print('Precione Q + ENTER para sair ')
            print()
            temp_name = input('Name: ')
            if len(temp_name) !=0 and temp_name != 'Q' and temp_name !='q':            
                db =sqlite3.connect('connection')
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM contacts")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i : 
                        print('Esse nome já existe no banco de dados ')
                        time.sleep(3)
                        self.add()
                self.name = temp_name
                temp_name = ''

                time.sleep(0.20)
                self.phone = input('Telefone:  ')
                time.sleep(0.20)              
                self.address = input(' Endereço: ')
                cursor.execute(""" INSERT INTO contacts\
                                    
                                (Name , Phone , Address )VALUES(?,?,?)                           
                                    
                                """,\
                                ( self.name, self.phone, self.address))
                db.commit()
                add_more = input('Adiconar mais contatos? (Y/N):')
                if add_more =='Y' or add_more =='y':
                    continue
                else:
                    db.close()
                    running = False
                    print('Voltando para o menu  ')
                    time.sleep(2)
                    self.menu()
            elif temp_name =='Q' or temp_name =='q':
                print('Voltando para o menu  ')
                time.sleep(2)
                self.menu()  
            else:
                winsound.Beep(3000,100)
                winsound.Beep(3000,100)                
                print('Por favor, coloque um nome para o contato ')                 
                time.sleep(2)       
    
    def update(self):
        
        print(' -------------- ATUALIZAR CADASTRO  --------------')
        print()
        name = input('Digite o nome do contato para atualizar: ')
        confirm = input(F'Atualizar o contato do (a) {name} ? (Y/N):')
        if confirm == 'Y' or confirm =='y':
            db = sqlite3.connect('connection')
            cursor = db.cursor()
            phone_update = input(F'Atualizar o telefone ? (Y/N):')
            if phone_update == 'Y' or phone_update =='y':
                phone = input(' Digite o numero de telefone: ')
                cursor.execute("UPDATE contacts  SET Phone =? WHERE Name =? ",(phone,name))
                db.commit()
                print(' TELEFONE FOI ATUALIZADO COM SUCESSO ')
                time.sleep(3)

            address_update = input(F'Atualizar o endereço ? (Y/N):')
            if address_update == 'Y' or address_update =='y':
                address = input(' Digite o novo endereço: ')
                cursor.execute("UPDATE contacts  SET Address =? WHERE Name =? ",(address,name))
                db.commit()
                time.sleep(3)
            if phone_update !='y' and address_update !='y':                    
                    print('Saindo sem atualizar')
                    time.sleep(3)
                    self.menu()
            print('ENDEREÇO ATUALIZZADO COM SUCESSO ')
            db.close()
            time.sleep(3)
            self.menu()
        else:
               print('Saindo sem atualizar ')
               time.sleep(3)
               self.menu()
            
    def remove(self):
        print(' -------------- DELETAR CADASTROS  --------------')
        print()
        name_remove = input('Digite o nome do contato para deletar: ')
        confirm = input(F'Deletar o contato do (a) {name_remove} ? (Y/N):')
        if confirm == 'Y' or confirm =='y':
            db = sqlite3.connect('connection')
            cursor = db.cursor()
            cursor.execute("DELETE FROM contacts  WHERE Name =?",(name_remove,))
            db.commit()
            print(' CADASTRO DELETADO COM SUCESSO ')
            time.sleep(3)
            self.menu()
        else:
            print('Saindo para menu ')
            time.sleep(3)
            self.menu()    

       
     
    def get_list(self):
        count = 0 
        count_2 = 0
        db = sqlite3.connect('connection')
        cursor = db.cursor()
        os.system('cls')
        print(' -------------- CONTATOS --------------')
        time.sleep(0.50)
        cursor.execute('SELECT Name, Phone, Address FROM contacts   ')
        results = cursor.fetchall()
        for row in results:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2, row)
            if count ==5:
                n = input('Precione ENTER para continuar ou N para voltar para o menu  ') 
                count = 0
                print()
                if n == 'n' or n =='N':
                    self.menu()
                
      
        print()
        print('Fim do resultado ')  
        print()
        option = input (F'APERTE: \n(A) - ATUALIZAR \n(D) - DELETAR \n(N) - VOLTAR  ')
        if option == 'a' or option == 'A':
            self.update()
        elif option ==  'd'or option == 'D':
            self.remove()
        elif option =='n'or option == 'N':
            self.menu()    
                
    def terminate(self):
        confirm = input ('Deseja sair do sistema ? (Y/N)')
        if confirm =='y' or confirm =='Y':
            print('SAINDO DO SISTEMA ')
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            time.sleep(0.5)
            print('Saindo...')                                    
            exit()
        else: 
            self.menu()       
    
    
    def menu(self):
        os.system('cls')
        winsound.Beep(2000,50)
        print('----------------- Menu -----------------')
        time.sleep(0.05)
        print()
        print('1 :) Add')
        time.sleep(0.05)
        
        print('2 :) Update')
        time.sleep(0.05)
        
        print('3 :) Remove')
        time.sleep(0.05)
        
        print('4 :) List')  
        time.sleep(0.05)
        
        print('5 :) Terminate')    
        print()
        opcao=input('Selecione uma opção:')
        if opcao == '1':
            self.add()
        elif opcao == '2':
            self.update()
        elif opcao == '3':
            self.remove() 
        elif opcao == '4':
            self.get_list() 
        elif opcao == '5':       
            self.terminate()
        else: 
            winsound.Beep(2500,100)
            print('Error, Tente Novamente ')
            time.sleep(2)    
            self.menu() 
                        
    def main(self):
        os.system('cls')
        if os.path.isfile('connection'):
            db=sqlite3.connect('connection')
            time.sleep(3)
            winsound.Beep(2000,50)
            print()
            print('Conectado ao Banco de Dados ')
            time.sleep(3)
            self.menu()
            
        else:
              print('Essa conecxão não exister ')  
              print()
              time.sleep(3)
              winsound.Beep(2000,50)
              
              print('Creating new connection File ')
              time.sleep(3)              
              db=sqlite3.connect('connection')
              cursor = db.cursor()
              cursor.execute(""" CREATE TABLE contacts
                             
                                (Name TEXT, Phone TEXT, Address TEXT)                           
                             
                                """)
              
                          
              winsound.Beep(2000,50)
              print()
              print('Conecxão criada com sucesso  ')
              print('Conectado ao Banco de Dados ')
              time.sleep(3)
              self.menu() 
              
        self.menu()   
contacts_manager = Manager() 
contacts_manager.main()       