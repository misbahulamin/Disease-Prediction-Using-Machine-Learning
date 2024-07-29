svm_preds=[15,4, 16, 9, 14, 33]
nb_preds=[15,4, 16, 9, 14, 33]
rf_preds=[15,4, 16, 9, 14, 33]
#final_preds = [mode([i,j,k])[0][0] for i,j,k in zip(svm_preds, nb_preds, rf_preds)] 
#mode([i,j,k])[0][0]

final_preds=[]
for i, j, k in zip(svm_preds, nb_preds, rf_preds):
    final_preds.append([i, j, k])
print(final_preds)
