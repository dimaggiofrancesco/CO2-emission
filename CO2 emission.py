
# coding: utf-8

# # Assignment 4
#
# Before working on this assignment please read these instructions fully. In the submission area,
# you will notice that you can click the link to **Preview the Grading** for each step of the assignment.
# This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
#
# This assignment requires that you to find **at least** two datasets on the web which are related,
# and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures**
# (see below) for the region of **None, None, United Kingdom**, or **United Kingdom** more broadly.
#
#
# As this assignment is for the whole course, you must incorporate principles discussed in the first week,
# such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
#
#  * State the region and the domain category that your data sets are about (e.g., **None, None, United Kingdom**
# and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files,
# or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question,
# this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses
# your stated research question.
#
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs
# to the given economy, or major changes in the economy compared to other regions.
#

import scipy.stats as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from functools import reduce
import re


# Opens 5 dataframes
CHI = pd.read_excel('CO2Chi.xlsx',sep="\t",header=(0), skiprows=3)
GER = pd.read_excel('CO2Ger.xlsx',sep="\t",header=(0), skiprows=3)
JAP = pd.read_excel('CO2Jap.xlsx',sep="\t",header=(0), skiprows=3)
UK = pd.read_excel('CO2UK.xlsx',sep="\t",header=(0), skiprows=3)
USA = pd.read_excel('CO2USA.xlsx',sep="\t",header=(0), skiprows=3)


# Merges the dataframes and cleans them
dfs  = [CHI,GER,JAP,UK,USA]
df_final = reduce(lambda left,right: pd.merge(left,right,on='Country Code'), dfs) #Merges the dataframes
df_final = df_final.drop(df_final.index[len(df_final)-3:len(df_final)]) #Deletes the last 3 lines (empty lines)
df_final = df_final.rename(columns ={"Country Code": "Year"}) #Renames a column
df_final['Year']=df_final['Year'].str.replace("\s*\[.*\\s*",'') #Deletes all the [] and everything inside
df_final = df_final.convert_objects(convert_numeric=True) #Converts objects to numeric
df_final.columns = ['Year','China','Germany','Japan','UK','USA'] #Renames the columns of the final df


# Creates the 5 plots
plt.plot(df_final['Year'], df_final['China'], color='k')
plt.annotate(('CHN'),xy=(2015,df_final.iloc[-1,1]-0.3), color='k', fontsize=12) #Creates an annotation on the right side of the graph using the last y value of the list as y value

plt.plot(df_final['Year'], df_final['Germany'], color='b')
plt.annotate(('GER'),xy=(2015,df_final.iloc[-1,2]-0.4), color='b', fontsize=12)

plt.plot(df_final['Year'], df_final['Japan'], color='r')
plt.annotate(('JAP'),xy=(2015,df_final.iloc[-1,3]), color='r', fontsize=12)

plt.plot(df_final['Year'], df_final['UK'], color='g')
plt.annotate(('GBR'),xy=(2015,df_final.iloc[-1,4]-0.5), color='g', fontsize=12)

plt.plot(df_final['Year'], df_final['USA'], color='m')
plt.annotate(('USA'),xy=(2015,df_final.iloc[-1,5]-0.5), color='m', fontsize=12)


# Formats the plot
plt.gcf().set_size_inches(9,7) #Size of the image
plt.gca().xaxis.set_label_coords(0.5,-0.06) #Locates X-axis label
plt.title("Carbon dioxide emission in the 5 countries with \n the world\'s biggest economy (from 1960 until 2014)", fontsize = 14, fontweight='bold')
plt.ylabel('Carbon dioxide emissions (metric tons per capita)', fontsize = 11, fontweight='bold')
plt.xlabel('Time (Year)', fontsize = 11, fontweight='bold')
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xlim(1958, 2019)
plt.ylim(0,25)

plt.gcf().text(.51, 0.84, 'USA = United States, JAP = Japan, CHN = China, GER = Germany, GBR = Great Britain', ha='center')

plt.show()



# In[ ]:




# In[ ]:



