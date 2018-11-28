# encoding: utf-8
import json
import re

class Cleanup():
    def parse(self, readpath, writepath):
        with open(readpath, "r", encoding="utf8") as g, open(writepath, 'w', encoding="utf8") as fout:
            pattern2 = r'(\\u0019)'
            pattern3 = r'(\\u0014)'
            pattern4 = r'(\\u001c)'
            pattern5 = r'(\\u001d)'
            pattern6 = r'(\\u0013)'
            for l in g:
                #l = re.sub(complete_pattern, " ", l)
                #l = re.sub(pattern2, "\b`", l)
                l = re.sub(pattern2, "\u0008\u0027", l)
                l = re.sub(pattern3, "(pause)", l)
                l = re.sub(pattern4, "", l)
                l = re.sub(pattern5, "", l)
                l = re.sub(pattern6, "", l)
                print(l)
                fout.write(l)

cleanup = Cleanup()
cleanup.parse("trumpspeeches.json", "cleanedTrumpSpeeches.json")
