# Oahu-Weather-Analysis

## Purpose
- Collect and analyze data regarding weather patterns to help make business decisions for potential start up company
- Utilize SQLite and SQLAlchemy to query database using Python and Jupyter notebook
- Provide summary statistics regarding mean temperatures in desired location

## Project Overview
- Using Python, Pandas, SQLite and SQLAlchemy, query a provided dataset to provide information regarding weather patterns 
- Create a histogram to provide a visualization showing temperature observations
- Showcase analysis on a webpage using Flask 

### Challenge Overview
- Query the database using filters to provide specific temperature information in the months of June and December
- Use Pandas built in describe method to provide summary statistics, such as average temperature and standard deviation, about temperature observations

## Resources
- Data Source: Hawaii weather SQLite file
- Software:  Python 3.7.6, Conda 4.13.0, Jupyter Notebook 6.4.8, Pandas 1.4.3, SQLite3 3.38.2
- MSU Bootcamp Spot Module 9: https://courses.bootcampspot.com/courses/2508/pages/9-dot-0-4-investing-in-waves-and-ice-cream?module_item_id=635874

## Results

### June Temperature Observations
- A total of 1,700 temperature observations were made for the month of June in the data set. 
- The average temperature was approximately 75 degrees and the median temperature was exactly 75 degrees, so the data is not skewed. 
- The maximum temperature was 85 degrees, and the minimum temperature was 64 degrees, so the range of temperature is not very drastic.

![image](https://user-images.githubusercontent.com/104038813/182623288-89e36f51-d992-40fd-a9cc-da4ba91bc9c1.png)

### December Temperature Observations
- A total of 1,517 observations were recorded in the month of December, so there is a lot of data to provide reliable analysis. 
- The average temperature was approximately 71 degrees and the median was exactly 71 degrees, so again the data is not skewed.  
- The maximum temperature was 83 degrees, and the minimum temperature was 56 degrees.

![image](https://user-images.githubusercontent.com/104038813/182623877-ea52bc1b-e9c3-41ac-a752-f7317d00c71c.png)


