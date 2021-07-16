from jobfinder import db
from jobfinder.models import Job
import csv 
import time

#Loads data from a csv file 
def Load_Data(file_name):
	"""
	This function loads data from a csv file and returns the data in a list
	"""
	data= []
	with open(f'./{file_name}.csv','rt', encoding="utf-8") as file:
		reader = csv.reader(file, delimiter=',')
		next(reader)
		for row in reader:
			#print(row[0], row[2])
			data.append(row)
	return data	

if __name__=="__main__":
	start = time.time()

	try:
		file_name ="15-07-21"
		data = Load_Data(file_name) 
		print("Data Loaded successfully.....")

		for i in data:
			job_record = Job(
				jobid = i[1],
				position = i[2],
				location = i[3],
				company = i[4],
				remote = i[5],
				status = i[6],
				description = i[7],
				joburl = i[8],
				categor = i[9],
				subcategor = i[10],
				tags = i[11]    
				)
			#Adding each records
			db.session.add(job_record) 
			print(f"Adding job: {i[0]}....")

		#Adding all the data to database	    
		db.session.commit() #Attempt to commit all the records
		print("Added all jobs to database successfully....")
	except:

		# If error occurs rollback the changes made
		db.session.rollback() #Rollback the changes on error
		print("Nothin Happened")

	end = time.time()	
	print("Time elapsed: " + str(end - start) + " s.") 

	"""
	Aj S, [16.07.21 00:20]
ssh root@185.149.22.32

Aj S, [16.07.21 00:21]
CVzZ2EyhrGdE3W6
	"""