#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
from random import randint
import re
import threading
import math

DICE_RX = u'(?:^|\s)(\d*)[d|D](\d+)(?:$|[\s,?;./:!])'

MEGA_DICEFEST = 200000
DICE_MAX_DISPLAYED = 100
DICE_HANDFUL = 10


class DiceActivity:
    def __init__(self, botInstance):
        self.botInstance = botInstance
            
    def private_message(self, msg):
        return
        #senderRealJid = self.plugin['xep_0045'].getJidProperty(self.room, msg['mucnick'], 'jid')
        #print "Private msg - From : " + str(msg['from']) + " type :  " + msg['type'] + " mucnick : " + msg['mucnick']
    
    def muc_message(self, msg):
        matches = re.finditer(DICE_RX, msg['body'].decode('utf8'), re.IGNORECASE | re.UNICODE)
        for match in matches:
            group = match.group(1)
            print group
            if (group == ''):
                numberOfDice = 1
            else:
                numberOfDice = int(match.group(1))
                
            diceValue = int(match.group(2))
            
            diceRollStr = ""
            total = 0
            
            if (diceValue <= 1):
                self.botInstance.sendMucMessage("/me a fait " + str(randint(1,1000)))
                return
            
            if (numberOfDice > 6666666):
                self.botInstance.sendMucMessage("/me fait la grêve. Reconductible.")
            else:
                if (numberOfDice == 1):
                    diceRollStr = "/me lance le dé : "
                elif (numberOfDice <= DICE_HANDFUL):
                    diceRollStr = "/me lance une poignée de dé : "
                elif (numberOfDice <= DICE_MAX_DISPLAYED):
                    diceRollStr = "/me lance un seau de dés : "
                elif (numberOfDice > DICE_MAX_DISPLAYED):
                    self.botInstance.sendMucMessage("/me se jette dans une piscine de dés.")
                    
                remainingDices = numberOfDice
                wentToAdventures = False
                while (remainingDices > 0):
                    if (remainingDices != numberOfDice):
                        self.botInstance.sendMucMessage("/me " + messages[total % len(messages)]) 
                        wentToAdventures = True
                        
                    dicesToRoll = min(remainingDices, MEGA_DICEFEST)
                    for i in xrange(0, dicesToRoll):
                        diceRoll = randint(1, diceValue)
                        total += diceRoll
                        if (numberOfDice <= DICE_MAX_DISPLAYED):
                            diceRollStr += str(diceRoll)
                            if (i != dicesToRoll - 1):
                                diceRollStr += ", "
                            else:
                                diceRollStr += ". "
                                
                    remainingDices -= dicesToRoll
                
                if (wentToAdventures):
                    self.botInstance.sendMucMessage("/me a fait " + str(total))
                else:
                    if (numberOfDice != 1):
                        diceRollStr += "Le total est " + str(total)
                        
                    self.botInstance.sendMucMessage(diceRollStr)                  
                    
                if (numberOfDice > MEGA_DICEFEST):
                    if (total > numberOfDice * (diceValue + 1) / 2):
                        self.botInstance.sendMucMessage("/me se sent bien mieux, quelque chose a grandi en lui.") 
                    else:
                        self.botInstance.sendMucMessage("/me a échoué dans sa quête.")
                        
messages = [
                "nage parmi les dés.",
                "se noie dans les dés.",
                "perd espoir.",
                "aperçoit un kraken.",
                "a des hallucinations.",
                "jette un D666.",
                "rate son D1.",
                "effectue un test de Santé Mentale.",
                "voit double.",
                "ne sait plus si l'abîme a un fond.",
                "rencontre un étrange murmure.",
                "ne voit plus la troisième dimension.",
                "fait un commentaire sexiste.",
                "va voter.",
                "mène une politique de réduction de la dette publique.",
                "le sait, il faut tailler un totem.",
                "sent la lune le regarder.",
                "est suivi par un raton laveur.",
                "atteint la transcendance.",
                "s'étouffe avec des spaghettis.",
                "a perdu le compte.",
                "pense a un chaton. L'espoir renait.",
                "étrangle un chaton.",
                "découvre la force.",
                "découvre la solitude.",
                "a trouvé le Zbeul.",
                "a perdu sa 86.",
                "privatise la recherche.",
                "mange chez McDonald's.",
                "se nourrit de morceaux de cadavre.",
                "gagne la Coupe du Monde.",
                "théorise l'islamisme radical.",
                "terrorise les anarcho-syndicalistes.",
                "combat Daesh et la CGT.",
                "ignore le lacrymo omniprésent et continue à compter.",
                "perd la vue.",
                "s'aperçoit qu'on lui ment.",
                "fait l'amour avec une chèvre.",
                "vend du crack à la sortie de l'église.",
                "chie sur la constitution.",
                "rejoint l'OTAN.",
                "vend la hanche synthétique de sa tante.",
                "abat un arbre.",
                "se dit que la mer est brûlée.",
                "vole un cendrier.",
                "s'élance au travers de la piece.",
                "se rend compte que si on éteint la lumière on ne peut plus le voir",
                "se redéfinit en tant que mouvement.",
                "prend conscience du complot rasta."]
                
                                      