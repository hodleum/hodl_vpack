import os


def run_as(username, path):
    os.system("sudo -u {u} {p}".format(u=username, p=path))
