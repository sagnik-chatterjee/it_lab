'''
@author Sagnik Chatterjee
Python program to reverse a content of a file and store it 
in another file.
'''


def reverse_file_contents(file_input_name:str,file_output_name:str,file_directory:str= '.\\' ):
	##some hack for windows as windows reads in this current directory as .\
	'''
	Reverse the file contents and writes to another file 
	,provided the file is persent in this directory.
	By default it will assume in current directory
	'''
	try:
		f1=open(file_directory+file_output_name,"w")

		with open(file_directory+file_input_name,"r")as fileread:
			data = fileread.read() 

		data_rev = data[::-1]

		f1.write(data_rev)
		f1.close()
		print("Done writing in output file.")
		return True  
	except Exception as e:
		print(e)
		return  False 


def main():
	file_input_name=input("Enter the input file name:- ")
	file_directory=input("Enter the directory name:- ")
	file_output_name=input("Enter the output file name:- ")

	reverse_file_contents(file_input_name,file_output_name,file_directory)


if __name__=='__main__':
	main()