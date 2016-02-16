ReadMe

1. Download the python environment
	install relative module of python, such as PIL, numpy, mahotas, sklearn

2. prepare the datasets
	download 101_ObjectCategories from the internet
	run generateTestFile.py with 4 parameters path of datasets, category, halftraining number, halfpredicting number , for example:
	python generateTestFile.py 101_ObjectCategories yin_yang 50 10 

3. run Predicting.py with 4 parameters, training.txt, testing.txt, output.txt, method
	for example: python Predicting.py training.txt testing.txt output.txt 1
	now there is only one method
	the result would be stored in output.txt, and it will show the prediction of the data

4. Todo list:
	evaluate the method
	3 more algorithm needed
	write the report
