#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class AnonyTalkActivity:
    def __init__(self, botInstance):
        self.botInstance = botInstance

    def private_message(self, msg):
        self.botInstance.sendMucMessage("(anonyme) " + msg['body'])

    def muc_message(self, msg):
        return
        
