# import package
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, auc, roc_auc_score, classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from imblearn.over_sampling import SMOTE

plt.rcParams['font.sans-serif']=['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus']=False

# read data and create dataset for modeling 
df = pd.read_csv("../data/traindrug.csv", encoding="utf8")
X = df.drop(labels=['再犯註記'], axis=1).values
y = df['再犯註記'].values
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

model1 = RandomForestClassifier(random_state=42, n_jobs=-1)
model1.fit(train_X, train_y)
y_pred = model1.predict_proba(test_X)[:, 1]
fpr1, tpr1, _ = roc_curve(test_y, y_pred)
auc1 = round(np.mean(cross_val_score(model1, X, y, scoring='roc_auc', cv=cv, n_jobs=-1)), 4)

model2 = RandomForestClassifier(class_weight='balanced', random_state=42, n_jobs=-1)
model2.fit(train_X, train_y)
y_pred = model2.predict_proba(test_X)[:, 1]
fpr2, tpr2, _ = roc_curve(test_y, y_pred)
auc2 = round(np.mean(cross_val_score(model2, X, y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

model3 = RandomForestClassifier(class_weight='balanced_subsample', random_state=42, n_jobs=-1)
model3.fit(train_X, train_y)
y_pred = model3.predict_proba(test_X)[:, 1]
fpr3, tpr3, _ = roc_curve(test_y, y_pred)
auc3 = round(np.mean(cross_val_score(model3, X, y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

oversample = SMOTE()
X_over, y_over = oversample.fit_resample(train_X, train_y) #X, y
model4 = RandomForestClassifier(random_state=42, n_jobs=-1)
model4.fit(X_over, y_over)
y_pred = model4.predict_proba(test_X)[:, 1]
fpr4, tpr4, _ = roc_curve(test_y, y_pred)
auc4 = round(np.mean(cross_val_score(model4, X, y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

plt.figure(0).clf()

plt.plot(fpr1,tpr1,label="base model, AUC="+str(auc1))
plt.plot(fpr2,tpr2,label="balanced weight, AUC="+str(auc2))
plt.plot(fpr3,tpr3,label="balanced_subsample weight, AUC="+str(auc3))
plt.plot(fpr4,tpr4,label="oversampling with SMOTE, AUC="+str(auc4))

plt.legend(loc="lower right")
plt.title("模型比較(AUC)")
plt.xlabel("fpr")
plt.ylabel("tpr")
plt.show()