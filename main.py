from SELFRec import SELFRec
from util.conf import ModelConf

if __name__ == '__main__':
    conf = ModelConf('./conf/GCTN.conf')
    rec = SELFRec(conf)
    rec.execute()
