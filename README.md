# DS4002 Prototyping - Project 1, Group 9: Constitution Preamble Analysis
This repository is to store our data, scripts, and output for our project. All contributions are done by Vaibhav Jha, Nick Kellogg, and Megan Vander Wiele. 

## Repository Contents
- #### Software and Platform (MAC OSX): To collect our data, we used python scripts with Regular Expressions, HTML scraping (requests and BeautifulSoup packages). We deployed these on the website https://constituteproject.org/constitutions?lang=en&status=in_force&status=is_draft, which houses lists of all current constitutions, and stored the preambles in an excel file. After we had the data, we used Microsoft Excel Macro Scripts to organize and clean the data to make it easier to analyze. Finally, for analysis we used a python script with the following packages: pandas, numpy, sentence transformer, seaborn, matplotlib, sklearn, scipy (SCH), word cloud. analysisScript.py imports all of these, however a few may have to be downloaded to your device before use.  

- #### Documentation Map:    
                root/DS4002projects    
                 ┣ README.md   
                 ┣ LICENSE.md   
                 ┣ 📂 DATA/    
                 ┃ ┣ preambles.xlsx    
                 ┃ ┣ preambles_data.csv   
                 ┃ ┣ preambles_data.xlsm   
                 ┃ ┣ preambles_data.xlsx  
                 ┣ 📂 SCRIPTS/    
                   ┣ EDA.ipynb  
                   ┣ analysisScript.py  
                   ┣ preambles_scrape.py  
                 ┣ 📂 anaconda_projects/  
                   ┣ .DS_store  
                   ┣ 📂 db/  
                     ┣ project_filebrowser.db   
                 ┣ 📂 .ipynb_checkpoints/     
                 ┃ ┗ EDA-checkpoint.ipynb   
                 ┣ 📂 .jupyter/desktop/workspaces/   
                 ┃ ┗ default-37a8.jupyterlab-workspace  

 
 - #### Result Reproduction: To collect data, run the preambles_scrape.py file, which should access the URL provided (if not in the script, copy paste from above) and output an excel file with all of the data. Data cleaning can be done through the use of the excel macros that are present in the preambles_data.xlsm file. You have to individually run all of these a few times to successfully encapsulate all of the data. Export a CSV version of the data. Once the CSV file is obtained, install the aforementioned python packages as necessary. Begin the analysis with feature extraction, concatenating observations into list form and producing sentence embeddings. Use sentence transformer model: "all-MiniLM-L6-v2." Next, calculate cosine-similarity measures between each of the embeddings, producing a cosine-similarity matrix. Afterwards, plot a dendogram to assess clustering potentialities (and the cut-off to perform hierarchical clustering). This will inform your next decision in conducting hierarchical clustering with a specified distance threshold. The output of this clustering model will be observations assigned to one of the clusters produced. Export this output into a CSV file to study which countries are grouped in which clusters. Finally, calculate a silhouette score to evaluate the efficacy of the clustering model. Assuming no further data cleaning and a distance threshold of 0.8, the resultant silhouette score should be 0.049. This output can be paired with word cloud outputs of each cluster to demonstrate which countries share similar constitutions with an emphasis on shared words.
