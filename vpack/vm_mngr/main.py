import vagrant as vagr
import subprocess


class VM:
    AUTO_DEL = True
    ALREADY_SUSPENDED = False

    class Task:
        def __init__(self, file, state="running"):
            pass
            # TODO: SC Init

    def __init__(self, lim=-1, autostart=True):
        self.vagr = vagr.Vagrant()
        try:
            self.vagr.status()
        except subprocess.CalledProcessError:
            self.vagr.init(box_name="alpine/alpine64")
        if self.vagr.status()[0].state == "not_created":
            self.vagr.up()
            self.ALREADY_SUSPENDED = False

            if not autostart:
                self.vagr.suspend()
                self.ALREADY_SUSPENDED = True
        if self.vagr.status()[0].state == "saved":
            self.ALREADY_SUSPENDED = True
        if self.vagr.status()[0].state != "running" and autostart:
            self.vagr.up()
            self.ALREADY_SUSPENDED = False

    def __del__(self):
        try:
            self.vagr.suspend()
        except subprocess.CalledProcessError:
            print("Some Problems Happened in Suspending Process. Please, suspend it manually")

    def start(self):
        if self.vagr.status()[0].state != "running":
            self.vagr.up()
            self.ALREADY_SUSPENDED = False

    def stop(self, force=False):
        if self.vagr.status()[0].state != "aborted" or self.vagr.status()[0].state != "saved" and not force:
            self.vagr.suspend()
            self.ALREADY_SUSPENDED = True
        elif force:
            self.vagr.halt(force=force)
            self.ALREADY_SUSPENDED = True

    def destroy(self):
        try:
            self.vagr.destroy()
            self.ALREADY_SUSPENDED = True
        except subprocess.CalledProcessError:
            pass
