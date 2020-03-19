#!/usr/bin/env python
# coding: utf-8

# ---

# # A Basic functionality and features
# 
# We include examples of useful noetebook features such as getting help, using tab, and Jupyter's magic functions.
# 
# ## Jupyter Features
# * [Basic Keyboard Shortcuts](#srt)
# * [Getting Help](#help)
# * [Tab Completion](#tab)
# * [Jupyter Magic Functions](#mag)
# * [Convert Notebook to Python Script](#cvt)

# ## Jupyter Features
# ---
# ### Basic Keyboard Shortcuts <a id = "srt"> </a>
# * `Shift + Enter` to run cell
# * `Escape` to leave cell
# * `m` to change cell to Markdown (after pressing escape)
# * `y` to change cell to Code (after pressing escape)
# *  Arrow keys move cells (after pressing escape)
# * `Enter` to enter cell

# ---

# ### Getting Help <a id = "help"> </a>
# Add question mark to the end of object

# In[1]:


# Get the numpy arrange docstring
import numpy as np
get_ipython().run_line_magic('pinfo', 'np.arange')


# In[2]:


# Get the python sort function docstring
get_ipython().run_line_magic('pinfo', 'sorted')


# ---

# ### Tab Completion <a id = "tab"> </a>
# Example of Jupyter tab completion include:
# - listing available modules on import   
# `import <tab>`   
# `from numpy import <tab>`   
# `from numpy import <tab>`
# - listing available modules after import         
# `np.<tab>`   
# - function completion    
# `np.ar<tab>`   
# `sor<tab>([2, 3, 1])`   
# - variable completion    
# `myvar_1 = 5`   
# `myvar_2 = 6`   
# `my<tab>`   
# - listing relative path directory contents   
# `../<tab>`   
# (then press enter on a folder and tab again to show its contents)

# ---

# ### Jupyter Magic Functions <a id = "mag"></a>
# - List of the available magic commands:

# In[3]:


get_ipython().run_line_magic('lsmagic', '')


# - Display plots inline

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# - Timers   

# In[5]:


a = [1, 2, 3, 4, 5] * int(1e5)
len(a)
# repeat from 1 to 5, 100000 times


# In[6]:


get_ipython().run_cell_magic('time', '', '\n# Get runtime for the entire cell\nfor i in range(len(a)):\n    a[i] += 5')


# In[7]:


# Get runtime for one line
get_ipython().run_line_magic('time', 'a = [_a + 5 for _a in a]')


# In[8]:


# Average results of many runs
get_ipython().run_line_magic('timeit', 'set(a)')


# * ipython-sql   
# External magic functions can be installed, e.g. ipython-sql

# In[9]:


# Source: https://github.com/catherinedevlin/ipython-sql
# do pip install ipython-sql in the terminal
get_ipython().run_line_magic('load_ext', 'sql')


# In[10]:


get_ipython().run_cell_magic('sql', 'sqlite://', "\nSELECT *\nFROM (\n    SELECT 'Hello' as msg_1\n) A JOIN (\n    SELECT 'World!' as msg_2\n) B;")


# Document versions for reproducability and datestamp the notebook

# In[11]:


# pip install version_information
# https://github.com/jrjohansson/version_information
#
# alternate option: https://github.com/rasbt/watermark

get_ipython().run_line_magic('load_ext', 'version_information')
get_ipython().run_line_magic('version_information', 'requests, numpy, pandas, matplotlib, seaborn, sklearn')


# ---

# ### Convert Notebook to Python Script <a id = "cvt"></a>

# jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb

# **For example, type the following command in terminal**   
# `jupyter nbconvert --to script Yalin-lesson-1.ipynb`

# ---
# * Another useful tool called `pipreqs`, This tool determines the **libraries used in a project** and **exports them into a requirements.txt file**   
# * The command is called from **outside the folder** containing your .py files.
# 

# `pipreqs [YOUR PATH]/`   
# **For example, in here, we use**   
# `pipreqs lesson-1/`   
