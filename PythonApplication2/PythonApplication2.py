import socket               # Import socket module

# PLEASE FIRST SELECT IMAP OR POP3 PROTOCOL OPTION IN IMAP/POP3 SERVER MODULE PROJECT

host = socket.gethostname() # Get local machine name"22.12.33.22"
port = 80                # Reserve a port for your service.


#İŞLEM
Istemcifunction(host,port); #İSTEMCİ SOKETİ OLUŞTUR, SUNUCUDAKİ MAİLLERİ GETİR. CONNECT TO SERVER  AND GET THE DATA
IstemcidekiMailleriGoster():  #ISTEMCI MAİL KUTUSUNDAKİ MAİLLERİ GÖSTER, SHOW MAILS IN THE CLIENT


def IstemcidekiMailleriGoster(): #show emails in client.
    dosyamiz = open("istemciMailKutusu.txt", "r+") #client mailbox
    satir="bos";
    while True:
     satir = dosyamiz.readline()
     print satir
     
     if not satir:
        dosyamiz.close()
        break
  


def Istemcifunction(host,port): # CONNECT TO SERVER  AND GET THE DATA AND SAVE THEM INTO CLIENT MAILBOX
    import socket               # Import socket module
    s = socket.socket()         # Create a socket object
    s.connect((host, port)) # HOST AND PORT IS SAME FOR SERVER AND CLIENT FOR THIS APP
    data =0;
    while True:
     data = s.recv(1024)  #Read 1014 byte, this is a blocking call. 
     if not data: break   
    #print (data) 
    dosyamiz = open("istemciMailKutusu.txt", "w+") //write mails from server to the local(client) mail box.
    dosyamiz.write(data)
    dosyamiz.close()
    s.close    


