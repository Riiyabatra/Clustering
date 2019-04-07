from rake_nltk import Rake
import operator
#rake_object = Rake("SmartStoplist.txt", 5, 3, 4)
sample_file = open("SmartStoplist.txt", 'r')
text = sample_file.read()
keywords = rake_object.run(text)
print ("Keywords:", keywords)