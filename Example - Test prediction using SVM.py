import numpy
from sklearn.neural_network import MLPClassifier
from sklearn.svm.classes import SVC
from machinelearning import Features_manager
from utils import Database_manager
import csv
"""
You could use this script for generating your prediction
"""

#initializate database_manager
database_manager=Database_manager.make_database_manager()
#initializate feature_manager
feature_manager=Features_manager.make_feature_manager()


tweets_training=numpy.array(database_manager.return_tweets_training())
labels_training=numpy.array(database_manager.get_label(tweets_training))

tweets_test=numpy.array(database_manager.return_tweets_test())
labels_test=numpy.array(database_manager.get_label(tweets_test))


# feature_type=[
#             "unigram",
#             "userinfobio",
#             ]

# feature_type = ['bert']
# feature_type = ['chargrams']

# feature_type = ['bert', 'numhashtag', 'network_friend_community']
# feature_type = ['bert', 'network_quote_community', 'network_friend_community']
feature_type = ['bert', 'network_retweet_community', 'network_friend_community']

#feature_type=feature_manager.get_availablefeaturetypes()


X,X_test,feature_name,feature_index=feature_manager.create_feature_space(tweets_training,feature_type,tweets_test)

print(feature_name)
print("feature space dimension X:", X.shape)
print("feature space dimension X_test:", X_test.shape)


# clf = SVC(kernel="linear")
clf = MLPClassifier(max_iter=1000,hidden_layer_sizes=(512, 128))

clf.fit(X,labels_training)
test_predict = clf.predict(X_test)



csvfile = open('machinelearning/results/TEST_PREDICTION.tsv', 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter='\t',quotechar='"', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(['tweet_id', 'label'])
for i in range(0,len(tweets_test)):
    spamwriter.writerow([tweets_test[i].id, test_predict[i]])






