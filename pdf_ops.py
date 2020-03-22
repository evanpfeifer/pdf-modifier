# Evan Pfeifer Presents PDF Operations

# Imports
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

# PDF Splitter Function
def split(path):
	'''
	Splits the pages of a pdf into separate PDF documents.

	Takes the path of the pdf file as a string as it's one argument.

	Path name can start from current directory:
	i.e. use 'file.txt' instead of 'home/User/Desktop/file.txt' if current
	directory is home/User/Desktop.

	Original PDF document is not mutated.
	'''
	fname = os.path.splitext(os.path.basename(path))[0]

	pdf = PdfFileReader(path)

	for page in range(pdf.getNumPages()):
		writer = PdfFileWriter()
		writer.addPage(pdf.getPage(page))

		output_name = '{}_page_{}'.format(fname, page + 1)

		with open(output_name, 'wb') as file:
			writer.write(file)

		print('Successfully created: {}'.format(output_name))


# PDF Merger Function
def merge(input_paths, output_path=None):
	'''
	Merges multiple PDF documents into one.

	Argument input_paths should be an list of input path(s), stored
	in an iterable. Documents are concatenated in order given to input_paths.

	Optional argument output_path gives the option to name the outputted document.
	The default name is the combination of all names of inputted documents.

	Original PDF is not mutated.
	'''
	merger = PdfFileMerger()

	for path in input_paths:
		merger.append(path)

	new_inputs = []
	for name in input_paths:
		new_inputs.append(os.path.splitext(os.path.basename(name))[0])

	if not output_path:
		output_name = ''
		for path in new_inputs:
			if output_name:
				output_name += '_' + path
			else:
				output_name += path

	else:
		output_name = output_path

	with open(output_name, 'wb') as file:
			merger.write(file)


# Notes

# os.path.splitext(path) splits a path into a tuple containing the pair of the root and extension.
# >>> os.path.splitext('/home/User/Desktop/file.txt')
# ('/home/User/Desktop/file', '.txt')

# os.path.basename(path) returns the base name of the path.
# >>> os.path.basename('/home/User/Desktop/file.txt')
# 'file.txt'

# PdfFileReader(path) instantiates a PdfFileReader object.