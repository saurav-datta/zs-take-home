# ZeroSystems take home for Saurav Datta

## Input provided as part of the exercise
- table_A.csv
- table_B.csv
- template.csv

## Goal
> In the financial sector, one of the routine tasks is mapping data from various sources in Excel tables. 
> For example, a company may have a target format for employee health insurance tables (Template) and may receive tables from other departments with essentially the same information, but with different column names, different value formats, and duplicate or irrelevant columns.
>Your task is to devise an approach using LLM for mapping tables A and B to the template by transferring values and transforming values into the target format of the Template table 

## Steps I executed
- I interacted with ChatGPT "Code interpreter" to transform files _table_A.csv_ and _table_B.csv_ to the template format
- You can see the chat history in [chat_history_code_interpreter.html](https://htmlpreview.github.io/?https://github.com/saurav-datta/zs-take-home/blob/main/script_chat_prompts/chat_history_code_interpreter.html)
- I asked ChatGPT to save the transformations to a Python file [transformations.py](https://github.com/saurav-datta/zs-take-home/blob/main/data_output/transformations.py) 
- The transformed files are present as _transformed_data_A_updated.csv_ and _transformed_data_B_updated.csv_, see [HERE](https://github.com/saurav-datta/zs-take-home/tree/main/data_output)
- I also asked ChatGPT to generate a config file that will have the input files and the field mappings including the functions present in the Python file. This can be seen in [config.json](https://github.com/saurav-datta/zs-take-home/blob/main/data_output/config.json)
- I then duplicated _table_A.csv_ and _table_B.csv_ as _table_C.csv_ and _table_D.csv_ respectively to test the approach. I renamed and updated the config and Python file. The new names are [config_for_files_C_D.json](https://github.com/saurav-datta/zs-take-home/blob/main/data_input/config_for_files_C_D.json) and [transformations_C_D.py](https://github.com/saurav-datta/zs-take-home/blob/main/data_input/transformations_C_D.py)
- I asked ChatGPT to apply the transformations to the new files using the new config. See chat history at  [chat_history_code_interpreter.html](https://htmlpreview.github.io/?https://github.com/saurav-datta/zs-take-home/blob/main/script_chat_prompts/chat_history_code_interpreter.html)
- The transformed files are present as _transformed_data_C.csv_ and _transformed_data_D.csv_, see [HERE](https://github.com/saurav-datta/zs-take-home/tree/main/data_output)

## Steps to replicate
- Create your equivalent files for _table_C.csv_ and _table_D.csv_
- No change to _template.csv_ 
- Update _config_for_files_C_D.json_ with your config
- Update _transformations_C_D.py_ with your transformations
- Upload the 5 files to "Code interpreter"
- Note: It is possible to not  refer to "template.csv" anymore. But I have left it as is for now
- The prompt is as present in chat history, but stating it here again:
>table_C.csv and table_D.csv are  files that need to be transformed. The file "config_for_files_C_D.json" contains the 
>instructions for transformations, including certain Python functions present in  "transformations_C_D.py" 

