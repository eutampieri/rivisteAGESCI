import requests
import urllib3
from json import loads
import lxml.html as html
urllib3.disable_warnings()


def download(url, fn):
    f = open(fn, 'wb')
    f.write(requests.get(url, verify=False, headers={
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:58.0) Gecko/20100101 Firefox/58.0"}).content)
    f.close()
    print("Scaricato "+fn)


inizio = int(input("Anno di inizio: "))
fine = int(input("Anno di fine: "))
for datiAnno in loads(requests.post("https://www.agesci.it/?wpfilebase_ajax=1", {"root": "wpfb-cat-121", "private": "0", "sort[file]": "file_post_id", "sort[cat]": '', "wpfb_action": "tree", "type": "browser", "base": "0"}, verify=False, headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:58.0) Gecko/20100101 Firefox/58.0"}).text):
    dati = html.fromstring("<html><body>"+datiAnno["text"]+"</body></html>")
    anno = dati.xpath("body/a")
    if len(anno) == 0:
        continue
    else:
        anno = anno[0]
    if int(anno.text) >= inizio and int(anno.text) <= fine:
        for numero in loads(requests.post("https://www.agesci.it/?wpfilebase_ajax=1", {"root": datiAnno["id"], "private": "0", "sort[file]": "file_post_id", "sort[cat]": '', "wpfb_action": "tree", "type": "browser", "base": "0"}, verify=False, headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:58.0) Gecko/20100101 Firefox/58.0"}).text):
            datiNumero = html.fromstring(
                "<html><body>"+numero["text"]+"</body></html>")
            links = datiNumero.xpath("body/a")
            for link in links:
                download(link.attrib["href"], link.text+".pdf")
