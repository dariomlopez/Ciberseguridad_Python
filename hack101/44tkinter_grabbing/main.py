import socket
import tkinter as tkinter
from tkinter import ttk
from tkinter import scrolledtext as scroll
from banner_grabbing import bannerGrabber

class Main:
  def __init__(self):
    
    self.ventana = tkinter.Tk()
    self.ventana.title("- Herramientas de hacking ético -")
    
    self.parentTab = ttk.Notebook(self.ventana)
    self.parentTab.pack()
    
    self.ventana_ban_grabber()
    
    self.ventana.mainloop()
  
  def ventana_ban_grabber(self):
    self.tabBanGrabbing = ttk.Frame(self.parentTab)
    self.parentTab.add(self.tabBanGrabbing, text="Banner Grabber")
    
    self.labelFrame1 = ttk.LabelFrame(self.tabBanGrabbing, text="")
    self.labelFrame1.pack()
    
    # label y entry para tomar número de ip deseada por el usuario
    self.label_ip = ttk.Label(self.labelFrame1, text="Introduce una IP: ")
    self.label_ip.pack()
    
    self.numero_ip = tkinter.StringVar()
    
    self.entry_ip = ttk.Entry(self.labelFrame1, textvariable=self.numero_ip)
    self.entry_ip.pack()
    
    self.button_grabber = ttk.Button(self.labelFrame1, text="Obtener Banners", command=self.banner_grabbing)
    self.button_grabber.pack()
    
    self.text_result = scroll.ScrolledText(self.labelFrame1, width=100, height=20)
    # self.text_result.insert(tkinter.END, result)
    self.text_result.pack()
  
  def banner_grabbing(self):
    ip = self.numero_ip.get()
    
    try:
      # start_port = int(port_range[0].strip())
      # end_port = int(port_range[1].strip())
      # ports = list(range(start_port, end_port + 1))
      
      results = bannerGrabber(ip)
      
      self.text_result.config(state=tkinter.NORMAL)
      self.text_result.delete("1.0", tkinter.END)
      for port, result in results.items():
        self.text_result.insert(tkinter.END, f"Port: {port}: {result}\n")
      self.text_result.config(state=tkinter.DISABLED)
    
    except socket.error as err:
      self.text_result.config(state=tkinter.NORMAL)
      self.text_result.delete("1.0", tkinter.END)
      self.text_result.insert(tkinter.END, f"Error: {str(err)}\n")
      self.text_result.config(state=tkinter.DISABLED)
    
app = Main()