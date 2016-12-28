import tweepy as ty
import os
import json as js
import time

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except ty.RateLimitError:
            time.sleep(15 * 60)
        except ty.error.TweepError as err:
            if '401' in str(err):
                print('probably the tweet account is protected cannot read it...')

            elif '429' in str(err):
                print('Twitter API rate limit reached, waiting 15 minutes...')
                time.sleep(15 * 60)
            else:
                raise

def getUserinformationtimeline(userID,api,count):
    Filename = 'timeline/' + str(userID) + '-timeline' + '.json'
    for statuses in limit_handled(ty.Cursor(api.user_timeline,screen_name=str(userID),count=count).pages()):
        for status in statuses:
            status = str(status) + '\n'
            saveInformationUserFile(Filename,status)



def getFriendList(userID,api,ty):
    try:
        nameFile = 'friend/' + str(userID) + '-' + 'friend' + '.txt'
        print nameFile
        for friend in limit_handled(ty.Cursor(api.friends,screen_name=str(userID)).items()):
            print friend.id
            friend = str(friend.id) + '\n'
            saveInformationUserFileTextPlane(nameFile,friend)
    except Exception as ex:
        print(type(ex))
        print(ex)

def getFollowerList(userID,api,ty):
    try:
        nameFile = 'follower/' + str(userID) + '-' + 'follower' + '.txt'
        print nameFile
        for follow in limit_handled(ty.Cursor(api.followers,screen_name=str(userID)).items()):
            print follow.id
            if follow.friends_count <= 1000:
                valueFollow = str(follow.id) + '\n'
                saveInformationUserFileTextPlane(nameFile,valueFollow)
    except Exception as ex:
        print(type(ex))
        print(ex)


def getUserFileList(nombreArchivo):
    try:
        file = open(nombreArchivo,'r')
        listaUsuario = file.read().splitlines()
        return listaUsuario
    except Exception as ex:
        print(type(ex))
        print(ex)


def saveInformationUserFile(namefile,diccionarioInformacion):
    try:
        with open(namefile,'a+') as f:
            js.dump(diccionarioInformacion,f,sort_keys= True, indent=4,ensure_ascii=True,separators=(',', ':'))
    except  IOError:
        print "error al guardar informacion en el archivo"

def saveInformationUserFileTextPlane(namefile,datos):
    try:
        with open(namefile,'a+') as f:
            f.write(datos)
    except  IOError:
        print "error al guardar informacion en el archivo"


if __name__ == '__main__':
    lista = []
    print "1.-Descargar timeline de los usuarios \n"
    print "2.-Descargar los friend de los usuarios\n"
    print "3.-Descargar los followers de los usuarios \n"
    auth = ty.OAuthHandler('uOr4jg73BdKyJ2cSC2wC1yBHF','5AK5maocpZ0Z9zMSbcZKWv04ozrSqasD2RAAWQyyLE6Dskbjf0')
    auth.set_access_token('733743988059033600-lc5PY0Och88cQtjXiOz8kESqty4Uq5m','M8ANqav2Wt3ckgsiPOnu3BNlk8WfAIKSmfHblnT2agmsX')
    api = ty.API(auth,timeout=60,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    print api
    opcion = input()
    print opcion
    lista = getUserFileList("screen_name.txt")
    print lista
    if (opcion==1):
        for i in lista:
            print "comenzo hacer crawler \n"
            getUserinformationtimeline(i,api,200)
    elif (opcion==2):
        for j in lista:
            print "comenzo a descargar a los amigos \n"
            print j
            getFriendList(j,api,ty)
    elif (opcion==3):
        for k in lista:
            print "comenzo a descargar los seguidores \n"
            getFollowerList(k,api,ty)
