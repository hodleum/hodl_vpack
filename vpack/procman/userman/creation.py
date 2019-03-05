import os
import grp
import crypt
import uuid


def csudo():
    os.system("echo '%scgrp ALL=NOPASSWD:{0}' | sudo EDITOR='tee -a' visudo".format("/usr/bin/apk"))


def cgrp():
    groups = grp.getgrall()
    group_ex = False
    for i in groups:
        if i.gr_name == "scgrp":
            group_ex = True
            break
    if not group_ex:
        print(os.system("sudo groupadd scgrp"))
        csudo()


def cuser(uname, shell="/bin/bash"):
    cgrp()
    encPass = crypt.crypt(str(uuid.uuid4()), "22")
    print(os.system("sudo useradd -p " + encPass +  # TODO: Process execution!
          " -s" + shell + " -g scgrp" + " -d " + "/home/" + uname + " -m " +
          " -c \"" + uname + "\" " + uname))


if __name__ == '__main__':
    cuser("sc_01")
