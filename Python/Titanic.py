import numpy as np
import pandas as pd
data = pd.read_csv('titanic.csv')
print(data.isnull().sum())
group = pd.DataFrame(data, columns=['SibSp', 'Parch'])
data['Relatives'] = data[['SibSp','Parch']].sum(axis=1)
group = pd.DataFrame(data, columns=['SibSp', 'Parch'])
data['Relatives'] = group.any(axis = 1)
group = pd.DataFrame(data, columns=['SibSp', 'Parch', 'Relatives'])
print(group)
male = data['Sex'].value_counts()
print(male)
data.loc[(data['Pclass'] == 1), 'Pclass'] = 'elite'
data.loc[(data['Pclass'] == 2), 'Pclass'] = 'middle'
data.loc[(data['Pclass'] == 3), 'Pclass'] = 'redneck'
print(data['Pclass'])
data['Fare_bin'] = data['Fare']
data.loc[(data['Fare'] < 20), 'Fare_bin'] = 'Дешево'
data.loc[(data['Fare'] >= 20), 'Fare_bin'] = 'Дорого'
print(data['Fare_bin'])
print(data['Fare_bin'].value_counts())

data[["Sex", "Survived"]].pivot_table(index=["Sex"], columns=["Survived"], aggfunc=len)
data[data["Survived"]==1][["Sex", "Age"]].pivot_table(values=["Age"], index=["Sex"], aggfunc="mean")
data.groupby("Pclass").mean()["Age"]

plt.figure()
_ = plt.boxplot(df['normal'],whis=[0,100])
data["Age"].mean()
data[["Sex", "Survived", "Age"]].pivot_table(values=["Age"], index=["Sex"], columns=["Survived"], aggfunc="mean")
data.hist();
data["Age"].plot("kde", xlim=(data["Age"].min(), data["Age"].max()));
data["Sex"].value_counts().plot(kind="pie", figsize=(7, 7), fontsize=20);
data["Pclass"].value_counts().plot(kind="pie", figsize=(7, 7), fontsize=20);
data[["Sex", "Survived"]].pivot_table(index=["Sex"], columns=["Survived"], aggfunc=len).plot(kind="bar");

