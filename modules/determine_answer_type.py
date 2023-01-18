import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('all')

from modules.info_extraction import getContinuousChunk

def defineCategory(qPOS):
    status = True
    for i in qPOS:
        if status == True:
            if i[0].lower() in ["registration", "transfer", "register", "registering"]:
                print("---question category: ","REGISTRASI")
                status = False
            elif i[0].lower() in ["information", "informations", "ask","asking", "care", "administration", "marketing"]:
                print("---question category: ","ADMISI")
                status = False
            elif i[0].lower() in ["verification", "validation", "payment","-register", "-registering", "-registration"]:
                print("---question category: ","VERIFIKASI DAN PENDAFTARAN ULANG")
                status = False
            elif i[0].lower() in ["degree", "Single degree", "double degree", "master track drograms", "master","program", "programs", "tpks", "major", "majors", "majoring"]:
                print("---question category: ","INFORMASI PROGRAM")
                status = False
            elif i[0].lower() in ["schedule"]:
                print("---question category: ","JADWAL")
                status = False
            elif i[0].lower() in ["orientation", "MOS"]:
                print("---question category: ","ORIENTASI MAHASISWA BARU")
                status = False
            elif i[0].lower() in ["transfer", "line", "change", "changing", "update", "updating"]:
                print("---question category: ","PENGAJUAN PERUBAHAN")
                status = False
            elif i[0].lower() in ["refund", "cancel", "canceling", "cancelation"]:
                print("---question category: ","REFUND")
                status = False

def determineAnswerType(text):
    word = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(word)
    chunk = nltk.ne_chunk(pos_tag)
    ne_list = []
    for ele in chunk:
        if isinstance(ele, nltk.Tree):
            ne_list.append(ele.label())
    if len(ne_list)>1:
        return ne_list
    else:
        questionTaggers = ['WP', 'WDT', 'WP$', 'WRB', 'VBZ']

        qPOS = nltk.pos_tag(nltk.word_tokenize(text))
        qTag = None

        for token in qPOS:
            if token[1] in questionTaggers:
                qTag = token[0].lower()
                break
        
        # print(qTag)

        if qTag == None:
            if len(qPOS) > 1:
                if qPOS[0][0].lower() in ['are', 'can', 'should','will']:
                    qTag = "YESNO"
                    return "YESNO"
        

        if qTag == 'is':
            print("---question classified: ","APA")
            # print(qPOS)
            defineCategory(qPOS)
            



        if qTag != "YESNO":
            # who/where/what/why/when/is/are/can/should
            if qTag == "who":
                print("---question classified: ","SIAPA")
                return "ORANG"
            elif qTag == "where":
                print("---question classified: ","DIMANA")
                defineCategory(qPOS)
            elif qTag == "when":
                print("---question classified: ","KAPAN")
                defineCategory(qPOS)
                return "TANGGAL"
            elif qTag == "which":
                if len(qPOS) > 1:
                    t2 = qPOS[1]
                    if t2[0].lower() in ["year", "day", "date", "week", "month"]:
                        print("---question classified: ","KAPAN")
                        return "TANGGAL"
                    elif t2[0].lower() in ["city", "state", "country"]:
                        print("---question classified: ","DIMANA")
                        return "LOKASI"
                    elif t2[0].lower() in ["person", "man", "women", "uncle", "aunt", "male", "female"]:
                        print("---question classified: ","SIAPA")
                        return "ORANG"
                defineCategory(qPOS)
            elif qTag == "what": 
                qTok = getContinuousChunk(text)
                print("---question classified: ","APA")
                '''if len(qTok) > 1:
                    if qTok[1][1] in ['is', 'are', 'was', 'were'] and qTok[2][0] in ["NN", "NNS", "NNP", "NNPS"]:
                        text = " ".join([qTok[0][1], qTok[2][1], qTok[1][1]])
                        print("DEFINITION")'''
                for token in qPOS:
                    if token[0].lower() in ["city", "place", "country", "capital", "state", "location", "area","route"]:
                        print("---question classified: ","DIMANA")
                        return "LOKASI"
                    elif token[0].lower() in ["company", "industry", "organization"]:
                        print("---question classified: ","SIAPA")
                        return "ORGANISASI"
                    elif token[0].lower() in ["cost", "area", "number"]:
                        print("---question classified: ","APA")
                        return "NOMOR"
                defineCategory(qPOS)

            elif qTag == "how":
                print("---question classified: ","BAGAIMANA")                
                t2 = qPOS[1]
                for i in qPOS:
                    if i[0].lower() in ["few", "great", "little", "many", "much"]:
                        print("---question category: ","KUANTITAS")
                    elif i[0].lower() in ["tall", "wide", "big", "far"]:
                        print("---question category: ","PENGUKURAN LINIER")
                defineCategory(qPOS)
            # elif qTag == "is":
            #     t2 = qPOS[1]
            #     if t2[0].lower() in ["few", "great", "little", "many", "much"]:
            #         print(t2[0].lower())
            #         return "KUANTITAS"                    
            else:
                return "TIDAK TERKATEGORIKAN"
        