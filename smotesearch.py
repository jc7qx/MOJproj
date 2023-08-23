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
from imblearn.over_sampling import BorderlineSMOTE

# read data and create dataset for modeling 
df = pd.read_csv("../data/traindrug.csv", encoding="utf8")
X = df.drop(labels=['再犯註記'], axis=1).values
y = df['再犯註記'].values
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)



model1 = RandomForestClassifier(random_state=42, n_jobs=-1)
model1.fit(test_X, test_y)
y_pred = model1.predict_proba(test_X)[:, 1]
fpr1, tpr1, _ = roc_curve(test_y, y_pred)
auc1 = round(np.mean(cross_val_score(model1, test_X, test_y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

model2 = RandomForestClassifier(class_weight='balanced', random_state=42, n_jobs=-1)
model2.fit(test_X, test_y)
y_pred = model2.predict_proba(test_X)[:, 1]
fpr2, tpr2, _ = roc_curve(test_y, y_pred)
auc2 = round(np.mean(cross_val_score(model2, test_X, test_y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

model3 = RandomForestClassifier(class_weight='balanced_subsample', random_state=42, n_jobs=-1)
model3.fit(test_X, test_y)
y_pred = model3.predict_proba(test_X)[:, 1]
fpr3, tpr3, _ = roc_curve(test_y, y_pred)
auc3 = round(np.mean(cross_val_score(model3, test_X, test_y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

oversample = SMOTE()
X_over, y_over = oversample.fit_resample(train_X, train_y) #X, y
model4 = RandomForestClassifier(random_state=42, n_jobs=-1)
model4.fit(X_over, y_over)
y_pred = model4.predict_proba(test_X)[:, 1]
fpr4, tpr4, _ = roc_curve(test_y, y_pred)
auc4 = round(np.mean(cross_val_score(model4, test_X, test_y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)

oversample2 = BorderlineSMOTE(random_state=42, kind='borderline-2')
X_over, y_over = oversample2.fit_resample(train_X, train_y) #X, y
model5 = RandomForestClassifier(random_state=42, n_jobs=-1)
model5.fit(X_over, y_over)
y_pred = model5.predict_proba(test_X)[:, 1]
fpr5, tpr5, _ = roc_curve(test_y, y_pred)
auc5 = round(np.mean(cross_val_score(model5, test_X, test_y, scoring='roc_auc', cv=cv, n_jobs=-1)),4)


print("AUC score for base model is %7.4f" % (auc1))
print("AUC score for balanced weight model is %7.4f" % (auc2))
print("AUC score for balanced_subsample weight model is %7.4f" % (auc3))
print("AUC score for SMOTE model is %7.4f" % (auc4))
print("AUC score for borderSMOTE model is %7.4f" % (auc5))

for k in [1, 2, 3, 4, 5, 6, 7]:
    oversample = SMOTE(random_state=42, k_neighbors=k)
    X_over, y_over = oversample.fit_resample(train_X, train_y) #X, y
    model5 = RandomForestClassifier(random_state=42, n_jobs=-1)
    model5.fit(X_over, y_over)
    y_pred = model5.predict_proba(test_X)[:, 1]
    auck = np.mean(cross_val_score(model5, test_X, test_y, scoring='roc_auc', cv=cv, n_jobs=-1))
    print("AUC scores for smote sample with k=%d is %7.4f" % (k, auck))