def evaluate(test_result,groundtruth):
    pred = test_result
    test = groundtruth

    qc_tp = 1
    qc_tn = 0
    qc_fp = 0
    qc_fn = 0

    ac_tp = 1
    ac_tn = 0
    ac_fp = 0
    ac_fn = 0

    qc_pred = []
    qc_gt = []
    ac_pred = []
    ac_gt = []

    for qc in test:
        item = qc[0]
        qc_gt.append(item)
    for ac in test:
        item = ac[1]
        ac_gt.append(item)
    for qc in pred:
        item = qc[0]
        qc_pred.append(item)
    for ac in pred:
        item = ac[1]
        ac_pred.append(item)
    
    # qc_eval
    for i in range(len(qc_pred)):
        if qc_pred[i]!= 'TIDAK TERKLASIFIKASIKAN':
            if qc_pred[i]==qc_gt[i]:
                qc_tp += 1
            elif qc_pred[i]!=qc_gt[i]:
                qc_fp += 1
                print("QC Predicted:", qc_pred[i], "| QC Groundtruth:", qc_gt[i])
        else:
            qc_fn += 1

    # ac_eval
    for i in range(len(ac_pred)):
        if ac_pred[i]!= 'TIDAK TERKATEGORIKAN':
            if ac_pred[i]==ac_gt[i]:
                ac_tp += 1
            elif ac_pred[i]!=ac_gt[i]:
                print("AC Predicted:", ac_pred[i], "| AC Groundtruth:", ac_gt[i])
                ac_fp += 1
        else:
            ac_fn += 1


    qc_acc = (qc_tp+qc_tn)/(qc_tp+qc_fp+qc_tn+qc_fn)
    qc_rcl = qc_tp/(qc_tp+qc_fn)
    qc_prc = qc_tp/(qc_tp+qc_fp)
    qc_f1 = 2*(qc_rcl*qc_prc)/(qc_rcl+qc_prc)

    ac_acc = (ac_tp+ac_tn)/(ac_tp+ac_fp+ac_tn+ac_fn)
    ac_rcl = ac_tp/(ac_tp+ac_fn)
    ac_prc = ac_tp/(ac_tp+ac_fp)
    ac_f1 = 2*(ac_rcl*ac_prc)/(ac_rcl+ac_prc)


    print("---QC_Accuracy:", qc_acc)
    print("---QC_Recall:", qc_rcl)
    print("---QC_Precision:", qc_prc)
    print("---QC_f1-measure:", qc_f1)
    print("\n")
    print("---AC_Accuracy:", ac_acc)
    print("---AC_Recall:", ac_rcl)
    print("---AC_Precision:", ac_prc)
    print("---AC_f1-measure:", ac_f1)



def evaluate_question(test_result,groundtruth):
    myObj = {"APA":{"tp" : 0, "tn":0, "fp":0, "fn":0}, "DIMANA":{"tp" : 0, "tn":0, "fp":0, "fn":0}, "KAPAN":{"tp" : 0, "tn":0, "fp":0, "fn":0}, "SIAPA":{"tp" : 0, "tn":0, "fp":0, "fn":0}, "BAGAIMANA":{"tp" : 0, "tn":0, "fp":0, "fn":0}, "MENGAPA":{"tp" : 0, "tn":0, "fp":0, "fn":0}}
    
    pred = test_result
    test = groundtruth

    qc_pred = []
    qc_gt = []
    ac_pred = []
    ac_gt = []
    
    for qc in test:
        item = qc[0]
        qc_gt.append(item)
    for ac in test:
        item = ac[1]
        ac_gt.append(item)
    for qc in pred:
        item = qc[0]
        qc_pred.append(item)
    for ac in pred:
        item = ac[1]
        ac_pred.append(item)

    # qc_eval
    for i in range(len(qc_pred)):
        if qc_pred[i]!= 'TIDAK TERKLASIFIKASIKAN':
            if qc_pred[i]==qc_gt[i]:
                myObj[qc_gt[i]]["tp"] += 1
            elif qc_pred[i]!=qc_gt[i]:
                myObj[qc_gt[i]]["fp"] += 1
                print("QC Predicted:", qc_pred[i], "| QC Groundtruth:", qc_gt[i])
        # else:
        #     qc_fn += 1

    # Variable to calculate
    a = "APA"
    b = "DIMANA"
    c = "SIAPA"
    d = "KAPAN"
    e = "MENGAPA"
    f = "BAGAIMANA"

    print(myObj)

    # APA CALCULATE
    APA_acc = (myObj[a]["tp"]+myObj[a]["tn"])/(myObj[a]["tp"]+myObj[a]["fp"]+myObj[a]["tn"]+myObj[a]["fn"])
    APA_rcl = myObj[a]["tp"]/(myObj[a]["tp"]+myObj[a]["fn"])
    APA_prc = myObj[a]["tp"]/(myObj[a]["tp"]+myObj[a]["fp"])
    APA_f1 = 2*(APA_rcl*APA_prc)/(APA_rcl+APA_prc)
        
    # DIMANA CALCULATE
    DIMANA_acc = (myObj[b]["tp"]+myObj[b]["tn"])/(myObj[b]["tp"]+myObj[b]["fp"]+myObj[b]["tn"]+myObj[b]["fn"])
    DIMANA_rcl = myObj[b]["tp"]/(myObj[b]["tp"]+myObj[b]["fn"])
    DIMANA_prc = myObj[b]["tp"]/(myObj[b]["tp"]+myObj[b]["fp"])
    DIMANA_f1 = 2*(DIMANA_rcl*DIMANA_prc)/(DIMANA_rcl+DIMANA_prc)

    # SIAPA CALCULATE
    SIAPA_acc = (myObj[c]["tp"]+myObj[c]["tn"])/(myObj[c]["tp"]+myObj[c]["fp"]+myObj[c]["tn"]+myObj[c]["fn"])
    SIAPA_rcl = myObj[c]["tp"]/(myObj[c]["tp"]+myObj[c]["fn"])
    SIAPA_prc = myObj[c]["tp"]/(myObj[c]["tp"]+myObj[c]["fp"])
    SIAPA_f1 = 2*(SIAPA_rcl*SIAPA_prc)/(SIAPA_rcl+SIAPA_prc)

    # KAPAN CALCULATE
    KAPAN_acc = (myObj[d]["tp"]+myObj[d]["tn"])/(myObj[d]["tp"]+myObj[d]["fp"]+myObj[d]["tn"]+myObj[d]["fn"])
    KAPAN_rcl = myObj[d]["tp"]/(myObj[d]["tp"]+myObj[d]["fn"])
    KAPAN_prc = myObj[d]["tp"]/(myObj[d]["tp"]+myObj[d]["fp"])
    KAPAN_f1 = 2*(KAPAN_rcl*KAPAN_prc)/(KAPAN_rcl+KAPAN_prc)

    # MENGAPA CALCULATE
    MENGAPA_acc = (myObj[e]["tp"]+myObj[e]["tn"])/(myObj[e]["tp"]+myObj[e]["fp"]+myObj[e]["tn"]+myObj[e]["fn"])
    MENGAPA_rcl = myObj[e]["tp"]/(myObj[e]["tp"]+myObj[e]["fn"])
    MENGAPA_prc = myObj[e]["tp"]/(myObj[e]["tp"]+myObj[e]["fp"])
    MENGAPA_f1 = 2*(MENGAPA_rcl*MENGAPA_prc)/(MENGAPA_rcl+MENGAPA_prc)

    # BAGAIMANA CALCULATE
    BAGAIMANA_acc = (myObj[f]["tp"]+myObj[f]["tn"])/(myObj[f]["tp"]+myObj[f]["fp"]+myObj[f]["tn"]+myObj[f]["fn"])
    BAGAIMANA_rcl = myObj[f]["tp"]/(myObj[f]["tp"]+myObj[f]["fn"])
    BAGAIMANA_prc = myObj[f]["tp"]/(myObj[f]["tp"]+myObj[f]["fp"])
    BAGAIMANA_f1 = 2*(BAGAIMANA_rcl*BAGAIMANA_prc)/(BAGAIMANA_rcl+BAGAIMANA_prc)

    # AVERAGE CALCULATE
    AVERAGE_acc = (APA_acc + DIMANA_acc +SIAPA_acc + KAPAN_acc + MENGAPA_acc + BAGAIMANA_acc)/6
    AVERAGE_rcl = (APA_rcl + DIMANA_rcl +SIAPA_rcl + KAPAN_rcl + MENGAPA_rcl + BAGAIMANA_rcl)/6
    AVERAGE_prc = (APA_prc + DIMANA_prc +SIAPA_prc + KAPAN_prc + MENGAPA_prc + BAGAIMANA_prc)/6
    AVERAGE_f1 = (APA_f1 + DIMANA_f1 +SIAPA_f1 + KAPAN_f1 + MENGAPA_f1 + BAGAIMANA_f1)/6


    print("---APA_Accuracy:", APA_acc)
    print("---APA_Recall:", APA_rcl)
    print("---APA_Precision:", APA_prc)
    print("---APA_f1-measure:", APA_f1)
    print("\n")
    print("---DIMANA_Accuracy:", DIMANA_acc)
    print("---DIMANA_Recall:", DIMANA_rcl)
    print("---DIMANA_Precision:", DIMANA_prc)
    print("---DIMANA_f1-measure:", DIMANA_f1)
    print("\n")
    print("---SIAPA_Accuracy:", SIAPA_acc)
    print("---SIAPA_Recall:", SIAPA_rcl)
    print("---SIAPA_Precision:", SIAPA_prc)
    print("---SIAPA_f1-measure:", SIAPA_f1)
    print("\n")
    print("---KAPAN_Accuracy:", KAPAN_acc)
    print("---KAPAN_Recall:", KAPAN_rcl)
    print("---KAPAN_Precision:", KAPAN_prc)
    print("---KAPAN_f1-measure:", KAPAN_f1)
    print("\n")
    print("---MENGAPA_Accuracy:", MENGAPA_acc)
    print("---MENGAPA_Recall:", MENGAPA_rcl)
    print("---MENGAPA_Precision:", MENGAPA_prc)
    print("---MENGAPA_f1-measure:", MENGAPA_f1)
    print("\n")
    print("---BAGAIMANA_Accuracy:", BAGAIMANA_acc)
    print("---BAGAIMANA_Recall:", BAGAIMANA_rcl)
    print("---BAGAIMANA_Precision:", BAGAIMANA_prc)
    print("---BAGAIMANA_f1-measure:", BAGAIMANA_f1)
    print("\n")
    print("---AVERAGE_Accuracy:", AVERAGE_acc)
    print("---AVERAGE_Recall:", AVERAGE_rcl)
    print("---AVERAGE_Precision:", AVERAGE_prc)
    print("---AVERAGE_f1-measure:", AVERAGE_f1)
    print("\n")
