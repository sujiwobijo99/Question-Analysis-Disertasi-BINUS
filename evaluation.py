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