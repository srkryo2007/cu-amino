import amino
import json
import time
from BotAmino import *
from BotAmino import BotAmino
import sys
from gtts import gTTS, lang
import emoji
import urllib.request
import time
from pathlib import Path
from google_trans_new import google_translator
import random
import os
from os import path
from random import uniform, choice, randint

client=BotAmino("teu nome", "tua senha")
client.self_callable = True

@client.command("ping") 
def ping(data):
    data.subClient.send_message(data.chatId, message="pong!")


@client.command("pong") # "pong" the command, the test function is not necessary
def pong(data):
        data.subClient.send_message(data.chatId, message="ping!")

#agora os comandos principais:


@client.command("cu")
def cu(data):
        data.subClient.send_message(data.chatId, message="π de barro ππππππππππππππππ")

@client.command("stoppost")
def stoppost(data):
        data.subClient.send_message(data.chatId,message="STOP POSTING ABOUT AMONG US! I'M TIRED OF SEEING IT! MY FRIENDS ON TIKTOK SEND ME MEMES, ON DISCORD IT'S FUCKING MEMES! I was in a server, right? and ALL OF THE CHANNELS were just among us stuff. I-I showed my champion underwear to my girlfriend and t-the logo I flipped it and I said hey babe, when the underwear is sus HAHA DING DING DING DING DING DING DING DI DI DING I fucking looked at a trashcan and said THATS A BIT SUSSY I looked at my penis I think of an astronauts helmet and I go PENIS? MORE LIKE PENSUS AAAAAAAAAAAAAAHGESFG")

@client.command("pico")
def pico(data):
        data.subClient.send_message(data.chatId,message="Goπ«Picoπ«yeahπ«yeahπ«goπ«Picoπ«ohπ«ππ«")

@client.command("dababy")
def dababy(data):
        data.subClient.send_message(data.chatId,message="ππππLezzzz GOOOOOOOOOOOOOOOO πππ")

@client.command("tiadomox")
def tiadomox(data):
        data.subClient.send_message(data.chatId, message="*fap* *fap* ela nΓ£o esta disponivel no momento π€‘", messageType=109)


@client.command("cringe")
def cringe(data):
        data.subClient.send_message(data.chatId, message="Cringe? hahaha Cringe Γ© o barulho do meu pau quando lhe atingeπ")

@client.command("zabiv")
def zabiv(data):
	msg = data.message + " null null "
	msg = msg.split(" ")
	try:
		rounds = int(msg[0])
	except (TypeError, ValueError):
		rounds = 5
		msg[2] = msg[1]
		msg[1] = msg[0]
		msg[0] = 5
	data.subClient.send_message(chatId=data.chatId, message=f"A rinha entre  {msg[1]} e {msg[2]} vai comeΓ§ar...")
	win1 = 0
	win2 = 0
	round = 0
	agress = ''
	defens = ''
	for zabiv in range(0, rounds):
		round = round + 1
		data.subClient.send_message(chatId=data.chatId, message=f"[bc]Round {round}/{rounds}")
		punch = randint(0, 1)
		if punch == 0:
			win1 = win1 + 1
			agress = msg[1]
			defens = msg[2]
		else:
			     	win2 = win2 + 1
			     	agress = msg[2]
			     	defens = msg[1]
		time.sleep(4)
		data.subClient.send_message(chatId=data.chatId, message=f"[ic] {agress} atingiu {defens}!")
		if win1 > win2:
		  data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} Ganhou essa rodada!")
		elif win1 < win2:
		  	data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} Ganhou essa rodada!")
		elif win1 == win2:
		  		data.subClient.send_message(chatId=data.chatId, message=f"[iC]Empate! Nenhum dos dois ganharam uma pontuaΓ§Γ£o")

@client.on_member_join_chat()
def say_hello(data):
    data.subClient.send_message(data.chatId, f"""Ola{data.author}, seja bem vindo a esse chat de merda, leia as regras pra nΓ£o acabar tomando no c-, para ver a lista de comandos, digite "!lista" agora se divirta!""")

@client.on_member_leave_chat()
def say_goodbye(data):
    data.subClient.send_message(data.chatId, f"Quem saiu do chat ama o BluezΓ£o e contraiu aids 2.5, e pelo visto o/a {data.author} ama ele!")

@client.command("pedepera")
def pera(data):
        data.subClient.send_message(data.chatId, message="Subi no pΓ© de pera π³π pa rancar uma pera ππ  a pera π tava podi π€’ e deci com uma goiaba π O trem π anda no ar π¬οΈ o aviΓ£o π«  anda na linha πͺ‘  a vaca π? bota ovo π₯ e tu tira leite π₯ da galinha π eu vou falar denovo πΊπ Subi no pΓ© de pera π³π pa rancar uma pera ππ  a pera π tava podi π€’ e deci com uma goiaba π O trem π anda no ar π¬οΈ o aviΓ£o π«  anda na linha πͺ‘  a vaca π bota ovo π₯ e tu tira leite π₯ da galinha π E vai novinha π πββοΈ E vai novinha π πββοΈ E vai novinha vai tirar leite da galinha π π π₯ πββοΈ  E vai novinha π πββοΈ E vai novinha π πββοΈ E vai novinha vai tirar leite da galinha π π π₯ πββοΈ")

@client.command("OeJosuke")
def OeJosuke(data):
        data.subClient.send_message(data.chatId, message="OE JOSUKE! EU USEI O ZAHANDO PARA APAGAR TEU PAU E AINDA COMER O CU DE QUEM TA LENDO, ISSO NΓO Γ DOIDO?")        

@client.command("frifai")
def frifai(data):
        data.subClient.send_message(data.chatId, message="AVEπMARIAπ³DOIDOOOOOOOOOOOπ΅Γ O FAMOSOπ€© 3βοΈCAPAπ«TROPAπ₯ΎAAAAAAAAAAAINπ«NOBRUπAPELAAAOπ€‘ππππππππππππ")

@client.command("pizza")
def pizza(data):
        data.subClient.send_message(data.chatId, message=" π¨βπ³ Ola! Aqui Γ© da Dominous Pizza! Aqui a Pizza que vocΓͺ pediu, Aproveite ela!π Agora presciso voltar ao trabalho, bibiiiiiiiπ΅")

@client.command("amogus")
def amogus(data):
        data.subClient.send_message(data.chatId, message="ΰΆΰΆΰΆΰΆΰΆΰΆπ³When the impostor is susπ³ΰΆΰΆΰΆΰΆΰΆΰΆΰΆ", messageType=109)


@client.command("SeloTsuki")
def SeloTsuki(data):
        data.subClient.send_message(data.chatId, message=' β β β β β πSELO DE PIADA TSUKI DE QUALIDADEππππ')

@client.command("π₯")
def Avocados(data):
        data.subClient.send_message(data.chatId, message='avocados π₯ from mexico π²π½')

@client.command("DK")
def DK(data):
        data.subClient.send_message(data.chatId, message='''π«π ParabΓ©ns π₯³ππππ vocΓͺ foi convidado para participar da tropa do Donkey Kong com  Shotgun π« π Antes de  se juntar,  para confirmar sua presenΓ§a eu gostaria de 4 informaΓ§Γ΅es suas π€ -O nome completo da sua mΓ£e -Os dΓ­gitos da parte frontal do cartΓ£o de crΓ©dito dela. 
-A data de validade. 
-Os outros trΓͺs dΓ­gitos que se encontram na parte de trΓ‘s do cartΓ£o. ApΓ³s fazer isso, vocΓͺ estarΓ‘ participando, espero vocΓͺ! π''')


        

@client.command("surpresa")
def surpresa(data):
    text = data.author
    with open('surpresa.png', 'rb') as file:
        data.subClient.send_message(file=file, fileType="image", chatId=data.chatId)

@client.command("casada")
def casada(data):
    text = data.author
    with open("casada.jpg", "rb") as file:
        data.subClient.send_message(file=file, fileType="image", chatId=data.chatId)

@client.command("π₯")
def avocados(data):
    text = data.author
    with open("avocados.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio", message="avocados π₯ from mexico π²π½")

@client.command("?")
def misterio(data):
    text = data.author
    with open("fogos.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")

@client.command("pg")
def pg(data):
    text = data.author
    with open("pg.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")

@client.command("android")
def samsung(data):
    text = data.author
    with open("e.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")

@client.command("megalozap")
def megalozap(data):
    text = data.author
    with open("zap.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")

@client.command("AcordaCorno")
def acordaCorno(data):
    text = data.author
    with open("ACORDA.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")


@client.command("tocar jimin do bts")
def bts(data):
    text = data.author
    with open("bts.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")

@client.command("comandossecretos")
def cs(data):
	data.subClient.send_message(data.chatId, message="""
[CBIU]--LISTA DE COMANDOS(π³π³π³secretosπ³π³π³)--
[c]!surpresa
[c]!?
[c]!pg

""")
        
@client.command("lista")
def vkidsnusovski2(data):
	data.subClient.send_message(data.chatId, message="""
[CBIU]--LISTA DE COMANDOS--

[C]!Ping - o Bot vai te responder com pong!

[C]!Pong - o Bot vai te responder com ping!

[C]!Perfil - vocΓͺ poderΓ‘ ver informaΓ§Γ΅es sobre seu perfil.

[C]!Pizza - pizza direto da Dominous Pizza hmmmm.

[C]!Dababy - Um dos melhores conversΓ­veis que vocΓͺ vai ver.

[C]!Stoppost - PARE DE POSTAR SOBRE AMONG US!

[C]!Pico - Go pico yeah yeah.

[C]!SeloTsuki - Melhor selo para aprovar piadas de qualidade duvidosas.

[C]!Cu - de barro.

[C]!pedepera - Subi no pΓ© de pera pa pega uma pera

[C]!Cringe - Cringe? Oq seria cringe?

[C]!TiadoMox - Converse com a Tia do Moximous N

[C]!OeJosuke - OKUYASU USOU O ZAHANDO PARA UMA COISA DO BALACO BACO

[C]!π₯ - Abacate

[C]!Frifai - NOBRU APELAAAAO

[C]!Amogus - Sussy baka

[C]!Casada - Oi casada

[C]!Google - o Bot vai pesquisar algo pra vc no google

[C]!Emojo - O Bot vai mandar uma sequencia aleatoria de emojis

[c]!Diga (insira uma palavra) - O bot irΓ‘ dizer o que vocΓͺ digitar... por voz!π³

[C]!Piada - o bot vai te contar piadas tΓ£o ruins q vc vai querer se matar

[c]!Figimg - marque o bot em uma figurinha do amino e ele irΓ‘ transforma-la em uma imagem

[c]!Fantasma - o bot vai mandar uma "mensagem fantasma"

[c]!Check - Veja se o bot ta on

[c]!Global - Veja o perfil global de alguΓ©m

[c]!comandossecretos -- descubra uma lista de comandos secretos

[c]!bts - xinxongxingling

[c]!ja - bot vai repitir tudo que vocΓͺ fala, em voz... e em japones

[c]!DK - Donkey Kong

[c]!acordaCorno - ACORDAAAAAAAAAAAAAAAAAAAAAAAA

[c]!samsung/!android - a famosa notificaΓ§Γ£o

[c]!megalozap - sans whatsapp

[c]!es -  bot vai repitir tudo que vocΓͺ fala, em voz... e em espanhol

[c]!cn -  bot vai repitir tudo que vocΓͺ fala, em voz... e em chines

[c]!ko -  bot vai repitir tudo que vocΓͺ fala, em voz... e em coreano

[c]!en -  bot vai repitir tudo que vocΓͺ fala, em voz... e em inglΓͺs

[c]!Seguir - o bot vai seguir vocΓͺ

[c]!zabiv - rinha de duas coisas, fale duas palavras ou duas pessoas, e veja a luta!

""") 

@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")


@client.command("emojo")
def randemoji(data):
	lis = ['π°π¨π±ππ€―', 'ππ€‘π₯΄π€π', 'ππ₯Έπ»π', 'πΊπΉπππ©', 'πππππ₯³', 'π€£πππ₯°π', 'βΊοΈπππΆπ€', 'π€©πππβΊοΈ', 'π€«π€π₯Ίππ€', 'π§π€π π³π€―', 'ππ₯π©ππ΅', 'ππ€?π€§π€π', 'πππ€­π₯²π', 'πππ€£π­π°', 'π€¬π‘π?π―π²', 'π€π€π€ ππ·', 'π₯΅π₯ΆπΊβ οΈπ½', 'πΈπΉπΊπ»πΌ', 'π½ππΏπΎπ', 'β€οΈπ§‘πππ', 'ππ€π€π€β₯οΈ', 'πππππ', 'ππππβ£οΈ', 'πππππ', 'π¦Ύπ¦ π¦·π΅οΈπ', 'π§π§π§π§π₯·', 'πͺπ΄π₯±π€€π', 'πΏππ₯β­π', 'πππ³οΈπ€π¦', 'ππ»π€π’β‘', 'β¨π«ποΈπβοΈ', 'π§ π«π«π©Έπ‘οΈ', 'πππΊπ·π', 'π¦π»πΌπ¨πΉ', 'π­π·πΈππΆ', 'ππ πππ', 'ποΈπ¦π¦π¦₯π¦', 'π²π¦π’π¦?π', 'ππ¦¬πππ', 'π¦π¦§πΏοΈπ¦¦π¦', 'ππ ππ¦π', 'ππππ­π₯ͺ', 'π₯π³π«π?π', 'ππππ«π', 'π§π₯π₯ππ¦ͺ', 'π§π±π₯ππ’', 'π°ππ‘π£π', 'π§π₯―π―π₯π₯‘', 'π­π©πͺπ₯?π¨', 'π₯π²π«π₯πΏ', 'π₯πΎπΉπΈπ»', 'πΏοΈπΎοΈπβΉοΈππΏ', 'π€βπππ', 'πΎπΉοΈπ?π²π', 'π΅π΄πΆπ·π°', 'πΊπΈπΉπ¨πΈπ»πΊπ¦πΌπΈ', 'π€π£π¨π₯π©']
	data.subClient.send_message(data.chatId, message=str(random.choice(lis)))

@client.command("check")
def test(data):
    data.subClient.send_message(data.chatId, f"Sim vadia, estou online {data.author}")

@client.command("global")
def g(data):
																		mention=data.subClient.get_message_info(chatId=data.chatId,messageId=data.messageId).mentionUserIds
																		for user in mention:
																			link=client.get_from_id(user,0).shortUrl
																			data.subClient.send_message(data.chatId,message=link)											


@client.command("perfil")
def profileinfo(data):
	repa = data.subClient.get_user_info(data.authorId).reputation
	lvl = data.subClient.get_user_info(data.authorId).level
	crttime = data.subClient.get_user_info(data.authorId).createdTime
	followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
	profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
	commentz = data.subClient.get_user_info(data.authorId).commentsCount
	posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
	followed = data.subClient.get_user_info(data.authorId).followingCount
	sysrole = data.subClient.get_user_info(data.authorId).role
	data.subClient.send_message(data.chatId, message=f"""
[C]Seu nome Γ©: {data.author}

[C]Seu Id Γ©: {data.authorId}

[C]VocΓͺ entrou na comu em: {crttime}

[C]A ΓΊltima vez que vocΓͺ editou seu perfil foi: {profilchange}

[C]VocΓͺ tem {repa} de REP

[C]VocΓͺ estΓ‘ Level {lvl}

[C]VocΓͺ criou: {posts} posts

[C]VocΓͺ tem {commentz} comentΓ‘rios no seu mural

[C]VocΓͺ seguiu {followed} pessoas

[C]VocΓͺ tem {followers} seguidores
	""")

@client.command("diga")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='pt-BR', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)


@client.command("seguir")
def follow(data):
    data.subClient.send_message(data.chatId, f'{data.author}, foi seguido')
    data.subClient.follow_user(data.authorId)


@client.command("ja")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='ja', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("en")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='en', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("en")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='en', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("ko")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='ko', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("es")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='es', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("cn")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='zh-CN', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)


@client.command("piada")
def randemoji(data):
	lis = ['''Qual Γ© a profissΓ£o mais frustrante do mundo?

Professor de NataΓ§Γ£o. Sabe porquΓͺ? Ele ensina, ensina e ensina e o aluno NADA.''', '''
O que se pode dizer da Γ‘gua que nΓ£o cabe dentro de um pote?

Que a Γ‘gua nΓ£o Γ© potΓ‘vel.''','''
Sabe uma piada? VocΓͺ!!!''','''
PorquΓͺ um louco pulou dum prΓ©dio enquanto passava shampoo na cabeΓ§a?

PorquΓͺ o Shampoo era anti-quedas''', '''
PorquΓͺ um louco comeu um relogio?

Pra consumir tempo''','''
Havia dez pessoas jogando mentos na rua, qual o nome do filme?

Os dez manda-mentos''', '''
Sabe qual o perso de fnf com nome de sorvete?

o PICOlΓ©''', '''um homem filosofo chegou em um cadeirante depressivo e falou "qual Γ© o problema?"
dai o cadeirante falou "minha vida Γ© sΓ³ desgraΓ§a"
sabe oque o filosofo falou?

amigo, sempre corra atras de seus sonhos.''']
	data.subClient.send_message(data.chatId, message=str(random.choice(lis)))

@client.command("figimg")
def stickmg(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "image"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
	os.remove(filename)

@client.command("figif")
def stickm(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "gif"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="gif")
	os.remove(filename)

  


@client.command("fantasma")
def fantasma(data):
	data.subClient.send_message(data.chatId, message=data.message, messageType=109)


	
client.launch(True)
print("ready")
