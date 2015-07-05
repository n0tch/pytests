#!/usr/bin/env python

import gtk, webkit

def go_but(widget):
	add = addressBar.get_text()
	if add.startswith('http://'):
		web.open(add)
	else:
		add = 'http://' + add
		addressBar.set_text(add)
		web.open(add)

win = gtk.Window()
win.connect('destroy', lambda w: gtk.main_quit())

box1 = gtk.VBox()
win.add(box1)

box2 = gtk.HBox()
box1.pack_start(box2, False)

addressBar = gtk.Entry()
box2.pack_start(addressBar)

goButton = gtk.Button("Go")
box2.pack_start(goButton)
goButton.connect("clicked", go_but)

scroller = gtk.ScrolledWindow()
box1.pack_start(scroller)

web = webkit.WebView()
scroller.add(web)

win.show_all()
gtk.main()