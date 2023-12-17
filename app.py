import gobject
import gtk
import threading
import time
 
class TestThread(threading.Thread):
    def __init__(self, mainview):
        threading.Thread.__init__(self)
        self.mainview = mainview
 
    def run(self):
        self.work_complete = False
        self.amount_completed = 0
        gobject.timeout_add(100, self._update_bar)
 
        for i in range(10):
            time.sleep(0.3)
            self.amount_completed += .1
 
        self.work_complete = True
 
    def _update_bar(self):
        self.mainview.progressbar.set_fraction(self.amount_completed)
        if self.work_complete:
            self.mainview.progressbar.set_text("Complete!")
        else:
            self.mainview.progressbar.set_text("%d%%" % (self.amount_completed * 100))            
        return not self.work_complete
 
class MainView(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect('delete_event', self.handle_window_delete_event)
        self.connect('destroy', self.quit)
 
        self.progressbar = gtk.ProgressBar()
        button1 = gtk.Button("Test")
        button1.connect('clicked', self.button1_click)
        box = gtk.VBox()
        box.pack_start(self.progressbar)
        box.pack_start(button1)
        self.add(box)
 
    def quit(self, *args):
        gtk.main_quit()
 
    def handle_window_delete_event(self, *args):
        return False
 
    def button1_click(self, *args):
        self.progressbar.set_fraction(0)
        worker = TestThread(self)
        worker.start()
 
if __name__ == "__main__":
    gobject.threads_init()
    MainView().show_all()
    gtk.main()
 