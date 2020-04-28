#!/usr/bin/env python
# -*- coding: utf-8 -*-

from whatsapp import WhatsAppWebClient


def onOpen():
	global client
	print("connection opened")
	client.generateQRCode(onQRCode)

def onMessage(data, descriptor):
	print("message received")
	print(data)
	print(descriptor)

def onClose():
	print("connection closed")

def onQRCode(a):
	print("qr code obtained :")
	print(a)
	
client = WhatsAppWebClient(onOpen, onMessage, onClose)
client.connect()

input()