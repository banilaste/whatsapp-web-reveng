#!/usr/bin/env python
# -*- coding: utf-8 -*-

from whatsapp import WhatsAppWebClient
import webbrowser

def onOpen():
	global client
	print("connection opened")
	client.generateQRCode(onQRCode)

def onMessage(data, descriptor):
	if type(data) != list or len(data) == 1 or len(data) > 3:
		print("ignoring message : ", data)
		return
	
	# Unpacking values
	if len(data) == 2:
		message_type, metadata = data
		payload = None
	elif len(data) == 3:
		message_type, metadata, payload = data

	if metadata != None and "add" in metadata:
		print(metadata["add"])
		print("last" in metadata and metadata["last"])
		print("loaded", len(payload), "messages")

def onClose():
	print("connection closed")

def onQRCode(a):
	print("qr code obtained :")
	webbrowser.open(a["image"], new=2)
	print(a["image"])
	
client = WhatsAppWebClient(onOpen, onMessage, onClose)
client.connect()

input()