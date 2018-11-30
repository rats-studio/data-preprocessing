# encoding: utf-8
import json
import re
import codecs

class Cleanup():
    def parse(self, readpath, writepath):
        with open(readpath, "r") as g, codecs.open(writepath, 'w', encoding="utf-8") as fout:
            pattern2 = r'(\\u0019)'
            pattern3 = r'(\\u0014)'
            pattern4 = r'(\\u001c)'
            pattern5 = r'(\\u001d)'
            pattern6 = r'(\\u0013)'
            j = json.loads(g.read().decode("utf-8-sig"))
            for l in j:
                l = re.sub(pattern2, "\u0008\u0027", l)
                l = re.sub(pattern3, "(pause)", l)
                l = re.sub(pattern4, "", l)
                l = re.sub(pattern5, "", l)
                l = re.sub(pattern6, "", l)
                json.dump(j, writepath, indent=4, sort_keys=True, ensure_ascii=False)


cleanup = Cleanup()
cleanup.parse("trumpspeeches.json", "cleanedTrumpSpeeches.json")
