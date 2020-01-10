#prépration module "os" et variables
import os
stat = 1

while stat == 1:
    print("=====SESSION-START=====")
    
    #lecture fichier programmes
    pg_list = open('programmes.txt.txt', 'a+')
    pg_list.seek(0)
    pg_list_read = pg_list.read()
    pg_list_convert =  pg_list_read.split()
    pg_list.close()

    #ajouter un programme
    def ajout():
        d_aj = input("ajout d'un programme car la liste est vide ou demande manuelle ? (y/n) : ")
        if d_aj == "y":
            print("Ne pas mettre d'espaces utiliser des _ ")
            nom_pg = input("nom du programme : ")
            contenu_2 = open("programmes.txt.txt", "w")
            if not(pg_list_convert) :
               contenu_2.write(pg_list_read + nom_pg)
            else:
               contenu_2.write(pg_list_read + " " + nom_pg)
            contenu_2.close()
            cont_pg = input(" CODE use Ctrl+C/V ")
            nom = nom_pg + '.txt'
            fichier_pg = open(nom, 'w+')
            fichier_pg.write(cont_pg)
            fichier_pg.close()

    #supprimer un programme
    def supprimer():
        print(pg_list_convert)
        del_pg = input("programme a supprimer : ")
        os.remove(del_pg + ".txt")
        if len(pg_list_convert) > 1 :
           if pg_list_convert.index(del_pg) == 1:
                 del_pg = " " + del_pg
                 print(del_pg)
           else:
                 del_pg = del_pg + " "
                 print(del_pg)
        elif len(pg_list_convert)== 1:
             del_pg = del_pg
        contenu_del_1 = pg_list_read
        contenu_del_1.replace(del_pg,'')
        contenu_del = open("programmes.txt.txt", "w")
        contenu_del.write(contenu_del_1.replace(del_pg,''))
        contenu_del.close()
    
    #défiinr le statut de la recherche
    def vide():
        if not(pg_list_convert) :
            print("nothing")
            ajout()
        else:
            print(pg_list_convert)
    
    #recherche_main
    def recherche():
        pg_r = input(" laisser vide pour lister les programmes sinon éssayez de chercher un nom  :       ")
        if pg_r == "":
            vide()
        elif pg_r == "ajout":
            ajout()
        elif pg_r == "delete":
            supprimer()
        elif pg_r == "quit":
            quit()            
        else:
            file = pg_r + ".txt"
            print() # saut
            print("========START========")
            exec(open(file).read())
            print("=========END=========")
            print() # saut
            print(" entrez recherche() pour réutiliser le programme | programme utiles : delete , ajout, quit ")
    recherche()
    
    print("=====END-SESSION=====")
    print() # saut
