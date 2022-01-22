log_file = open("um-server-01.txt") # Opens um-server file to be edited


def sales_reports(log_file): # defines the function name
    for line in log_file: # iterates through the file
        line = line.rstrip() # Removes white space from the text in line
        day = line[0:3] # selects the portion of the line that makes the day variable
        if day == "Mon": # Changed from Tues to Mon
            print(line) # prints the 


sales_reports(log_file) # runs the sales_report funtion on the log_file