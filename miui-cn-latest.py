import re,requests
import sys

def get_cn_latest():
    r=requests.get("https://www.miui.com/download-360.html")
    rr=re.compile(r'https?://bigota.d.miui.com.+QFKCNXM.+zip')
    l=list(set(rr.findall(r.text)))
    if len(l)!=0 :
        return l[0]
    else:
        sys.exit()

def get_cn_dev_latest():
    return 'https://bigota.d.miui.com/20.4.30/miui_RAPHAEL_20.4.30_5972f5ffca_10.0.zip'


if __name__=='__main__':
    print(get_cn_dev_latest())
