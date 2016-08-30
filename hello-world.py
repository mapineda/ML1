#import decision tree from sklearn lib
from sklearn import tree
# Step 1: collect training data
# Legend: 1: orange, 0: apple
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels= [0, 0, 1, 1]
# Step 2: train the classifier
# here, we're going to use a Descision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[160, 0]])
