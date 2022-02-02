#!/usr/bin/env python
# coding: utf-8

# # Machine Learning 5

# ## 1. What are the key tasks that machine learning entails? What does data pre-processing imply?

# In[ ]:


# Data preprocessing is a process of preparing the raw data and making it suitable for a machine learning model. 
# It is the first and crucial step while creating a machine learning model. When creating a machine learning project
# it is not always a case that we come across the clean and formatted data.


# ## 2. Describe quantitative and qualitative data in depth. Make a distinction between the two.

# In[ ]:


# Quantitative data is anything that can be counted or measured; it refers to numerical data. Qualitative data is 
# descriptive, referring to things that can be observed but not measured—such as colors or emotions.


# ## 3. Create a basic data collection that includes some sample records. Have at least one attribute from each of the machine learning data types.

# In[ ]:


# Most data can be categorized into 4 basic types from a Machine Learning perspective: numerical data, 
# categorical data, time-series data, and text.


# ## 4. What are the various causes of machine learning data issues? What are the ramifications?

# In[ ]:


# One of the significant issues that machine learning professionals face is the absence of good quality data.
# Unclean and noisy data can make the whole process extremely exhausting. We don't want our algorithm to make 
# inaccurate or faulty predictions. Hence the quality of data is essential to enhance the output.


# ## 5. Demonstrate various approaches to categorical data exploration with appropriate examples.

# In[ ]:


# Logistic Regression is a classification algorithm so it is best applied to categorical data.


# ## 6. How would the learning activity be affected if certain variables have missing values? Having said that, what can be done about it?

# In[ ]:


# Missing values can be replaced by some measure of central tendecy like mode
# we can also remove the missing values and then model the data


# ## 7. Describe the various methods for dealing with missing data values in depth.

# In[ ]:


# A common technique is to use the mean or median of the non-missing observations. This can be useful in cases 
# where the number of missing observations is low. However, for large number of missing values, using mean or
# median can result in loss of variation in data and it is better to use imputations.


# ## 8. What are the various data pre-processing techniques? Explain dimensionality reduction and function selection in a few words.

# In[ ]:


# Principal Component Analysis (PCA), Factor Analysis (FA), Linear Discriminant Analysis (LDA) and 
# Truncated Singular Value Decomposition (SVD) are examples of linear dimensionality reduction methods.


# ## 9. i. What is the IQR? What criteria are used to assess it?
# ## ii. Describe the various components of a box plot in detail? When will the lower whisker surpass the upper whisker in length? How can box plots be used to identify outliers?

# In[ ]:


# The difference between Q3 and Q1 is called the Inter-Quartile Range or IQR. IQR = Q3 - Q1. To detect the outliers
# using this method, we define a new range, let's call it decision range, and any data point lying outside this 
# range is considered as outlier and is accordingly dealt with.

# A box and whisker plot—also called a box plot—displays the five-number summary of a set of data. The five-number
# summary is the minimum, first quartile, median, third quartile, and maximum.


# ## 10. Make brief notes on any two of the following:
# ## 1. Data collected at regular intervals
# ## 2. The gap between the quartiles
# ## 3. Use a cross-tab

# In[ ]:


# Examples of interval data includes temperature (in Celsius or Fahrenheit), mark grading, IQ test and CGPA. These 
# interval data examples are measured with equal intervals in their respective scales. Interval data are often used
# for statistical research, school grading, scientific studies and probability.

# In a set of data, the quartiles are the values that divide the data into four equal parts. The median of a set of
# data separates the set in half. ... The interquartile range or IQR is the range of the middle half of a set of
# data. It is the difference between the upper quartile and the lower quartile.

# Cross tabulation is a method to quantitatively analyze the relationship between multiple variables. Also known 
# as contingency tables or cross tabs, cross tabulation groups variables to understand the correlation between 
# different variables. It also shows how correlations change from one variable grouping to another.

