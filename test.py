# Open a file in read-write mode
fo = open("myfile.txt", "w+")
print ("Name of the file: ", fo.name)

# Assuming file has the following line
txt = "This is 1st line,"
fo.writelines( txt )

seq = " This is 2nd line, This is 3rd line"
# Write sequence of lines at the end of the file.
fo.seek(0, 2)
fo.writelines( seq )

# Now read complete file from beginning.
fo.seek(0,0)
line = fo.readlines()
print ("Read Line: %s" % (line))

# Close the file
fo.close()