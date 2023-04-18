import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('all')

from modules.info_extraction import getContinuousChunk


def defineCategory(text):
    qPOS = nltk.pos_tag(nltk.word_tokenize(text))
    # print(qPOS)
    status = True
    for i in qPOS:
        # print(i[0])
        if status == True:
            if i[0].lower() in ["registration", "transfer", "register", "registering"]:
                # print("---question category: ","REGISTRASI")
                status = False
                return "REGISTRASI"
            elif i[0].lower() in ["schedule", "schedules"]:
                # print("---question category: ","JADWAL")
                status = False
                return "JADWAL"
            elif i[0].lower() in ["degree", "master", "program", "programs", "tpks", "major", "majors", "majoring", "learning", "lectures", "lecture", "student", "studets"]:
                # print("---question category: ","INFORMASI PROGRAM")
                status = False
                return "INFORMASI PROGRAM"
            elif i[0].lower() in ["information", "informations", "ask", "asking", "service", "services", "serving", "care", "administration", "marketing"]:
                # print("---question category: ","ADMISI")
                status = False
                return "ADMISI"
            elif i[0].lower() in ["cost", "scholar", "scholarship", "tuition"]:
                # print("---question category: ","ADMISI")
                status = False
                return "BIAYA PERKULIAHAN"
            elif i[0].lower() in ["verification", "validation", "payment", "-register", "-registering", "-registration"]:
                # print("---question category: ","VERIFIKASI DAN PENDAFTARAN ULANG")
                status = False
                return "VERIFIKASI DAN PENDAFTARAN ULANG"
            elif i[0].lower() in ["orientation", "MOS"]:
                # print("---question category: ","ORIENTASI MAHASISWA BARU")
                status = False
                return "ORIENTASI MAHASISWA BARU"
            elif i[0].lower() in ["transfer", "line", "change", "changes", "changing", "update", "updating"]:
                # print("---question category: ","PENGAJUAN PERUBAHAN")
                status = False
                return "PENGAJUAN PERUBAHAN"
            elif i[0].lower() in ["refund", "cancel", "canceling", "cancelation"]:
                # print("---question category: ","REFUND")
                status = False
                return "PENGEMBALIAN DANA"

    if status == True:
        return "TIDAK TERKATEGORIKAN"


def determineAnswerTypeFactoid(text):
    # Bagaimana
    if 'which' in text.lower():
        return "YANG MANA"
    for i in ['how much', 'how many', 'how great', 'how litle']:
        if i in text.lower():
            return "BERAPA BANYAK"
    for i in ['how often']:
        if i in text.lower():
            return "BERAPA SERING"
    for i in ['how far', 'how long the way']:
        if i in text.lower():
            return "BERAPA JAUH"
    for i in ['how long', 'how small', 'how short']:
        if i in text.lower():
            return "BERAPA PANJANG"
    for i in ['how old', 'how young', 'how mature']:
        if i in text.lower():
            return "BERAPA TUA"


def determineAnswerType(text):
    word = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(word)
    chunk = nltk.ne_chunk(pos_tag)
    ne_list = []
    for ele in chunk:
        if isinstance(ele, nltk.Tree):
            ne_list.append(ele.label())
    if len(ne_list) > 1:
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
                if qPOS[0][0].lower() in ['are', 'can', 'should', 'will']:
                    qTag = "APA"
                    return "APA"

        if qTag == 'is':
            # print("---question classified: ","APA")
            return "APA"
            # print(qPOS)

        if qTag != "YESNO":
            # who/where/what/why/when/is/are/can/should
            if qTag == "who":
                # print("---question classified: ","SIAPA")
                return "SIAPA"
            elif qTag == "where":
                # print("---question classified: ","DIMANA")
                return "DIMANA"
            elif qTag == "when":
                # print("---question classified: ","KAPAN")
                return "KAPAN"
            elif qTag == "why":
                # print("---question classified: ","MENGAPA")
                return "MENGAPA"
            elif qTag == "which":
                if len(qPOS) > 1:
                    t2 = qPOS[1]
                    if t2[0].lower() in ["year", "day", "date", "week", "month"]:
                        # print("---question classified: ","KAPAN")
                        return "KAPAN"
                    elif t2[0].lower() in ["city", "state", "country"]:
                        # print("---question classified: ","DIMANA")
                        return "DIMANA"
                    elif t2[0].lower() in ["person", "man", "women", "uncle", "aunt", "male", "female"]:
                        # print("---question classified: ","SIAPA")
                        return "SIAPA"

            elif qTag == "what":
                qTok = getContinuousChunk(text)
                # print("---question classified: ","APA")
                '''if len(qTok) > 1:
                    if qTok[1][1] in ['is', 'are', 'was', 'were'] and qTok[2][0] in ["NN", "NNS", "NNP", "NNPS"]:
                        text = " ".join([qTok[0][1], qTok[2][1], qTok[1][1]])
                        print("DEFINITION")'''
                for token in qPOS:
                    if token[0].lower() in ["city", "place", "country", "capital", "state", "location", "area", "route"]:
                        # print("---question classified: ","DIMANA")
                        return "DIMANA"
                    elif token[0].lower() in ["company", "industry", "organization"]:
                        # print("---question classified: ","SIAPA")
                        return "SIAPA"
                    elif token[0].lower() in ["cost", "area", "number"]:
                        # print("---question classified: ","APA")
                        return "APA"
                    else:
                        return "APA"

            elif qTag == "how":
                # print("---question classified: ","BAGAIMANA")
                t2 = qPOS[1]
                for i in qPOS:
                    if i[0].lower() in ["few", "great", "little", "many", "much"]:
                        # print("---question category: ","KUANTITAS")
                        return "HOW MANY"
                    elif i[0].lower() in ["tall", "wide", "big", "far"]:
                        # print("---question category: ","PENGUKURAN LINIER")
                        return "HOW FAR"
                    else:
                        return "BAGAIMANA"

            # elif qTag == "is":
            #     t2 = qPOS[1]
            #     if t2[0].lower() in ["few", "great", "little", "many", "much"]:
            #         print(t2[0].lower())
            #         return "KUANTITAS"
            else:
                return "TIDAK TERKLASIFIKASIKAN"
