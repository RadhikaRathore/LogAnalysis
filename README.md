# Logs Analysis Project

Logs Analysis Project is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

### Prerequisites

   - Install [VirtualBox](https://www.virtualbox.org/)
   - Install [Vagrant](https://www.vagrantup.com/)
   - Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
     These files configure the virtual machine and install all the tools needed to run this project.
   - Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   - Unzip the data to get the newsdata.sql file.
   - Put the newsdata.sql file into the vagrant directory
   - Load the data using the following command: ``` psql -d news -f newsdata.sql ```
   
## Views created to simplify queries:
     
#statusinlog:

create view statusinlog as
select time ::date,status from log;

#failedstatusnum:

create view failedstatusnum as
select time,count(*) as num
from statusinlog
where status = '404 NOT FOUND'
group by time;

#allstatus:

create view allstatus as
select time,count(*) as num
from statusinlog
where status = '404 NOT FOUND'
or status = '200 OK'
group by time;

#errorpercent:

create view errorpercent as
select allstatus.time,
       allstatus.num as totalstatus,
       failedstatusnum.num as totalfailed,
       failedstatusnum.num::double precision/allstatus.num::double precision * 100 AS percentageoffailure
from allstatus,
     failedstatusnum
where allstatus.time = failedstatusnum.time;
        
  
## Getting Started

  - Download the code
  - Extract compressed file 
  - unzip the folder and copy in shared vagrant folder.
  - Open terminal and cd to the vagrant folder
  - Run the application, `reporting_tool.py`
  
## Expected Output:

                The most popular three articles of all time

 "Candidate is jerk, alleges rival" -- 338647 views
 "Bears love berries, alleges bear" -- 253801 views
 "Bad things gone, say good people" -- 170098 views

                 The most popular article authors of all time

 Ursula La Multa -- 507594 views
 Rudolf von Treppenwitz -- 423457 views
 Anonymous Contributor -- 170098 views

                Days with more than one percentage of error requests

July 17, 2016
            -- 2.26 % errors
  


# Creator

**Radhika Rathore**



