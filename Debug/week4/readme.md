Debug issue
You have a start_date_report.py Python script with a bunch of functions like get_start_date(), list_newer() and others. This script will operate on the data file employees-with-date.csv, which is generated from a file URI within the script. The script then generates a report of all employees that started on the given start date.

To list the files on the home directory, use the following command:

ls
Copied!
Output:

1.png

Grant the executable and editable file permission to the start_date_report.py

sudo chmod 777 ~/start_date_report.py
Copied!
Now, run the python program start_date_report.py

./start_date_report.py
Copied!
Enter the values for the year, month, and day respectively as the prompt appears.

Output:

2.png

The program crashes with a TypeError. This is because it reads the value entered at prompts as a string. Refer to the function datetime.datetime() within the script. The arguments passed to the datetime.datetime() function should be of integer type, but in our case, the input values are strings.

In order to fix this ERROR, open start_date_report.py by using the following command:

nano ~/start_date_report.py
Copied!
Now, search for get_start_date() function and typecast the string variable that’s taken from user input to the integer. Here, we have to explicitly cast the data type of these three variables: year, month, and day from string to integer.

Eg. year = int(input('Enter a value for the year: '))

Similarly, you can cast the values of month and day to an integer.

The get_start_date() function should now looks like this:

3.png

Save the start_date_report.py script file by clicking Ctrl-o, the Enter key, and Ctrl-x.

Run the start_date_report.py Python script:

./start_date_report.py
Copied!
Output:

4.png

Click Check my progress to verify the objective.
Success: Debug and fix issue
Debug and fix issue
Success: Debug and fix issue

Improve performance
Once you debug the issue, the program will start processing the file but it takes a long time to complete. This is because the program goes slowly line by line instead of printing the report quickly. You need to debug why the program is slow and then fix it. In this section, you need to find bottlenecks, improve the code, and make it finish faster.

The problem with the script is that it’s downloading the whole file and then going over it for each date. The current script takes almost 2 minutes to complete for 2019-01-01. An optimized script should generate reports for the same date within a few seconds.

To check the execution time of a script, add a prefix "time" and run the script.

Example:

time ./test.py
Copied!
In order to fix this issue, open the start_date_report.py script using nano editor. Now, modify the get_same_or_newer() function to preprocess the file, so that the output generated can be used for various dates instead of just one.

nano ~/start_date_report.py
Copied!
This is a pretty challenging task that you have to complete by modifying the get_same_or_newer() function.

Here are few hints to fix this issue:

Download the file only once from the URL.

Pre-process it so that the same calculation doesn't need to be done over and over again. This can be done in two ways. You can choose any one of them:

To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.
To sort the data by start_date and then go date by date.
Choose any one of the above preprocessing options and modify the script accordingly.

Once you’ve completed modifying the Python script, save the file by clicking Ctrl-o, the Enter key, and Ctrl-x.

Run the start_date_report.py python script:

./start_date_report.py
Copied!
Output:

5.png

Now, you’ve improved the performance of the script.

Click Check my progress to verify the objective.
Success: Improve performance
Improve performance
Success: Improve performance

Congratulations!
Congrats! You've successfully fixed errors, bugs, and increased the performance of execution. Debugging an issue from a program and reducing execution time by fixing a repeatable call will be beneficial as an IT Specialist.

End your lab
When you have completed your lab, click End Lab. Qwiklabs removes the resources you’ve used and cleans the account for you.

You will be given an opportunity to rate the lab experience. Select the applicable number of stars, type a comment, and then click Submit.

The number of stars indicates the following:

1 star = Very dissatisfied
2 stars = Dissatisfied
3 stars = Neutral
4 stars = Satisfied
5 stars = Very satisfied
You can close the dialog box if you don't want to provide feedback.

For feedback, suggestions, or corrections, please use the Support tab.
