# ZeroSystems take home for Saurav Datta

## Input provided as part of the exercise
- table_A.csv
- table_B.csv
- template.csv

## Goal
> In the financial sector, one of the routine tasks is mapping data from various sources in Excel tables. 
> For example, a company may have a target format for employee health insurance tables (Template) and may receive tables from other departments with essentially the same information, but with different column names, different value formats, and duplicate or irrelevant columns.
>Your task is to devise an approach using LLM for mapping tables A and B to the template by transferring values and transforming values into the target format of the Template table 

## Steps
- I interacted with ChatGPT "Code interpreter" to transform files table_A.csv and table_B.csv
- You can see the chat history in directory "script_chat_prompts"
- I asked ChatGPT to save the transformations to a Python file "transformations.py" 
- The transformed files are present as transformed_data_A_updated.csv and transformed_data_B_updated.csv
- I also asked ChatGPT to generate a config file that will have the input files and the field mappings including the functions present in the Python file. This can be seen in "config.json"
- I then duplicated table_A.csv and table_B.csv to table_C.csv and table_D.csv respectively to test the approach. I renamed and updated the config and Python file. The new names are config_for_files_C_D.json and transformations_C_D.py
- The transformed files are present as transformed_data_C.csv and transformed_data_D.csv
