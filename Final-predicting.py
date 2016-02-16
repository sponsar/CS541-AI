import os,sys
from PIL import Image
from numpy import *
import mahotas
import mahotas.features
from numpy import array
from sklearn.feature_extraction.image import PatchExtractor,extract_patches_2d
from sklearn.pipeline import Pipeline
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier#0.75
from sklearn.tree import DecisionTreeClassifier#0.7(random)
from sklearn.linear_model import LogisticRegression, SGDClassifier#0.65, 0.5(random)
from sklearn.naive_bayes import MultinomialNB,GaussianNB#0.65, 0.75
from sklearn.ensemble import AdaBoostClassifier,BaggingClassifier,ExtraTreesClassifier,RandomForestClassifier#0.65, 0.7,0.75(the best random),0.8(random)
from sklearn.svm import SVC,LinearSVC,NuSVC#0.6, 0.5(random), 0.6

def loadImage(path):
	jpgfile = Image.open(path)
	#print jpgfile.size
	temp = asarray(jpgfile)
	
	if len(temp.shape) == 3:
		x=temp.shape[0]
		y=temp.shape[1]*temp.shape[2]
		temp.resize((x,y)) # a 2D array
	
	#result = mahotas.features.lbp(temp, 0.1,20)
	result = extract_patches_2d(temp,(7,7))
	return result

def loadFile(path):
	f = open(path);
	images = []
	ratings = []
	pathes = []
	for line in f:
		imagePath,rating = line.strip().split(' ')
		ratings.append(rating)
		pathes.append(imagePath)
	counts = len(pathes)
	i = 1
	for imagePath in pathes:
		#print imagePath, rating
		sys.stdout.write("\r%d%%" % (100 * i / counts))
		sys.stdout.flush()
		i += 1
		result = loadImage(imagePath)
		images.append(result)
	f.close()
	return images, ratings, pathes

if len(sys.argv) != 5:
	print 'Arguments is not equal to 4!'
	sys.exit();
trainingFilePath = sys.argv[1]
testingFilePath = sys.argv[2]
outputFilePath = sys.argv[3]
method = (int)(sys.argv[4])

print 'start loading training file'
training_images , training_ratings, training_pathes = loadFile(trainingFilePath)
print
print 'start loading testing file'
testing_images , testing_ratings, testing_pathes = loadFile(testingFilePath)
print


#build a 3-NN classifier on the training data
clf1=KNeighborsClassifier()
clf2=GaussianNB()
clf3=NuSVC()
#eclf = VotingClassifier(estimators=[('knn', clf1), ('gas', clf2)], voting='soft', weights=[2,1])
for i in range(10):
	clf1.fit(training_images,training_ratings)
	#use the classifier to predict
	predicted=clf1.predict(testing_images)# a list of number 0 or 1  
	#print predicted
	print accuracy_score(predicted, testing_ratings)

i = 0
f = open(outputFilePath,'w')
for path in testing_pathes:
	f.write(path + ' ' + predicted[i] + '\n')
	i += 1
f.close()
