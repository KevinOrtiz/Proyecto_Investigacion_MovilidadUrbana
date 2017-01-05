import glob
import numpy as ny
import matplotlib.pyplot as plt

def contarElementosDeUnArchivo(listaElementos):
    return len(listaElementos)



def extraerListaElementosDeUnArchivo(nameFile):
    try:
        file = open(nameFile,'r')
        listaID = file.read().splitlines()
        return listaID
    except Exception as ex:
        print(type(ex))
        print(ex)



def graficarHistograma(nameusuario,totalFollowers,totalFriends,nameFileOut):
    try:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        N = 1
        datosFriendFollower = [totalFriends,totalFollowers]
        labelFriendFollower = [1,2]
        ind = ny.arange(N)
        width = 0.35
        recta1 = ax.bar(ind, datosFriendFollower[0], width, color='black',yerr=labelFriendFollower[0],error_kw = dict(elinewidth=2,ecolor='red'))
        recta2 = ax.bar(ind+width,datosFriendFollower[1],width,color='red',yerr=labelFriendFollower[1],error_kw = dict(elinewidth=2,ecolor='black'))
        ax.set_xlim(-width,len(ind)+width)
        if(totalFriends >=30 and totalFollowers<=99):
            ax.set_ylim(0,200)
        elif(totalFriends>=100 and totalFollowers<=200):
            ax.set_ylim(100,300)
        elif(totalFriends>=201 and totalFollowers<=300):
            ax.set_ylim(200,400)
        elif(totalFriends>=301 and totalFollowers<=500):
            ax.set_ylim(300,600)
        elif(totalFriends>=501 and totalFollowers<=700):
            ax.set_ylim(500,800)
        elif(totalFriends>=701 and totalFollowers<=900):
            ax.set_ylim(700,980)
        elif(totalFriends>=901 and totalFollowers<=1800):
            ax.set_ylim(900,1880)
        elif(totalFriends>=1850 and totalFollowers<=2850):
            ax.set_ylim(1850,2875)
        elif(totalFriends>=2851 and totalFollowers<=4000):
            ax.set_ylim(2851,4000)
        else:
            ax.set_ylim(0,700)



        ax.set_ylabel('Cantidad')
        ax.set_title('Cantidad de Amigos y Seguidores')
        xTickMarks = ['Friend-Followers']
        ax.set_xticks(ind+width)
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=0, fontsize=10)
        ax.legend( (recta1[0], recta2[0]), ('Friend', 'Followers') )
        plt.savefig(nameFileOut)
        print "GraficoGenerado:" + nameFileOut

    except Exception as ex:
        print(type(ex))
        print(ex)

if __name__ == '__main__':
    listaFriend = []
    listaFollower = []
    dicFollower = {}
    dicFriend = {}
    ##dicUsuariosTwitter = {}
    ##listaUsuario =["07rafaello","1DarwinArce","2MontalezaM","6krls9","_xaviermora95","AAngelo10","AAron_plimplom","AbMonoUIO","acajamarca73","acerofeli","adrianharo","AdryPC1988","aiditahm","alejandrovaras","alejo_zv87","AlexCedeno28","AlexJimboViteri","alfredocruz26","alfzuniga","alinstante2016","and1188","andreromero_","AndresCrespoA","AndresGrandaE","andresnovillo","AndresOchoaD","andreuch_ldu","andrscdno","AnggieAroca","antbriones","ArgPaula","arnoldboneta","ArroboRodas","AtilaUno","aureliagrce","autumnzira","AVAstudillo","AvileQuionez","AzenethFlores6","bailaconbruce","BarceGianSG","BeatPDesign","bebaferreira","BetoAlvarez4","BladyFS","borys_bismark","ByronBaque","Carito_Ponton","CarlosAbarcaj","CarlosMenaM","castillo_shanty","castro_jakob","cceres_pato","ccplazashopping","CEBAGGIOS","Cec4Mar","CeciliaZavalaM","CesarVG","cesgmejia7","cfsalvadorm","chapaca_marco","Charitovergara","ChinitaLeydi","chogori2010","Chriscalicc","chrisdusac","ChrisRoblesCh","Cinarice","CinhoMurillo"]
    for follower,friend in zip(glob.iglob('follower/*.txt'),glob.iglob('friend/*.txt')):
        print "friend:" + friend
        print "follower:" + follower
        listaFriend = extraerListaElementosDeUnArchivo(friend)
        listaFollower = extraerListaElementosDeUnArchivo(follower)
        labelFriend1 = friend.split("/")
        labelFriend2 = labelFriend1[1].split("-")
        labelFriend = labelFriend2[0]
        print 'nombre_friend:' + labelFriend
        labelfollower1 = follower.split("/")
        labelfollower2 = labelfollower1[1].split("-")
        labelfollower = labelfollower2[0]
        print 'nombre_follower:' + labelfollower
        dicFriend[labelFriend]=listaFriend
        dicFollower[labelfollower]=listaFollower


    for keyFriend,valueFriend in dicFriend.iteritems():
        for keyFollower,valueFollower in dicFollower.iteritems():
            if keyFriend == keyFollower:
                print "se valido el primer archivo:" + keyFriend
                sizeFriend = contarElementosDeUnArchivo(valueFriend)
                print "tamano_de_los_amigos:" + str(sizeFriend)
                sizeFollower = contarElementosDeUnArchivo(valueFollower)
                print "tamano_de_los_follower:" + str(sizeFollower)
                nameFileOut = 'GraficasFrecuencia/' + keyFriend + '_histograma' + '.png'
                graficarHistograma(keyFriend, sizeFollower,sizeFriend, nameFileOut)
                break
