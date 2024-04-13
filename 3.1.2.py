import sys

# Get the user input from the command line argument
user_input = sys.argv[1]

import os
import requests
import datetime
import pandas as pd
from urllib.parse import urlparse
import os
import requests
import re
import pandas as pd
import shutil
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from datetime import date

year_range1 =sys.argv[2];
start_year1, end_year1 = map(int, year_range1.split('-'))
year_range2 =sys.argv[3];
start_year2, end_year2 = map(int, year_range2.split('-'))
year_range3 =sys.argv[4];
start_year3, end_year3 = map(int, year_range3.split('-'))
year_range4 =sys.argv[5];
start_year4, end_year4 = map(int, year_range4.split('-'))
year_range5 =sys.argv[6];
start_year5, end_year5 = map(int, year_range5.split('-'))

Lakhs7 = sys.argv[7];
Lakhs8 = sys.argv[8];
Lakhs9 = sys.argv[9];
Lakhs10 = sys.argv[10];
Lakhs11 = sys.argv[11];

def extract_file_id_from_link(link):
    """Extracts the file ID from a Google Drive shareable link."""
    match = re.search(r'/file/d/([a-zA-Z0-9_-]+)', str(link))
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Google Drive shareable link")

def download_file_from_google_drive(file_id, destination_folder):
    """Downloads a file from Google Drive given its file ID."""
    URL = "https://docs.google.com/uc?export=download"
    destination = os.path.join(destination_folder, f"{file_id}.pdf")

    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

def get_confirm_token(response):
    """Extracts the confirmation token from the response cookies."""
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    """Saves the content of the response to the destination file."""
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

def to_txt(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    text = output_string.getvalue()
    output_string.close()
    # Convert text to uppercase and remove spaces
    return ''.join(text.upper().split())

def pdf_download(pdf_path):
    filenames = []
    for filename in os.listdir(pdf_path):
        if filename.endswith(".pdf"):
            filenames.append(os.path.join(pdf_path, filename))
    return filenames

global cntt
cntt = 0

def scan_text_for_word(txt, target_word):
    global cntt
    if str(target_word) in txt:
        print(f"Found '{target_word}' in the text.")
        cntt += 1
    else:
        print(f"'{target_word}' not found in the text.")
        pass

def download_google_sheets_as_excel(sheet_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    parsed_url = urlparse(sheet_url)
    sheet_id = parsed_url.path.split('/')[3]

    download_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"
    response = requests.get(download_url)
    
    if response.status_code == 200:
        filename = os.path.join(output_folder, f"{sheet_id}.xlsx")
        with open(filename, 'wb') as f:
            f.write(response.content)
        #print(f"Excel file downloaded successfully: {filename}")
    else:
        print("Failed to download Excel file.")

def rename_excel_in_directory(directory_path, new_name):
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".xlsx"):
                old_name = os.path.join(directory_path, filename)
                new_name_with_extension = os.path.join(directory_path, new_name)
                os.rename(old_name, new_name_with_extension)
                #print(f"File '{old_name}' renamed to '{new_name_with_extension}' successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
new_data =0        
def go_to_search_for(Money,year_column, index):
    global Money_data1
    global Money_data2
    global Money_data3
    global Money_data4
    global Money_data5
    if year_column and Money is not None:

        year_data = df.loc[index, year_column]
        Money_data = df.loc[index, Money]

        if year_data == start_year1 or year_data == end_year1 :
         Money_data1 += Money_data
        if year_data == start_year2 or year_data == end_year2  :
         Money_data2 += Money_data
        if  year_data == start_year3 or year_data == end_year3  :
         Money_data3 += Money_data
        if year_data == start_year4 or year_data == end_year4  :
         Money_data4 += Money_data
        if  year_data == start_year5 or year_data == end_year5  :
         Money_data5 += Money_data

if __name__ == "__main__":
    output_folder = 'Downloaded_EXCEL'
    sheet_url = str(user_input)
    #"https://docs.google.com/spreadsheets/d/1DL2MsEK1PAqitg0LNyYcg22bY32bqRoBZz7A1zavL2A/edit?usp=sharings"
    download_google_sheets_as_excel(sheet_url, output_folder)

    directory_path = r'C:\xampp\htdocs\Nacc_front_php\Downloaded_EXCEL'
    new_excel_name = 'sss.xlsx'
    rename_excel_in_directory(directory_path, new_excel_name)

    excel_path = 'C:\\xampp\\htdocs\\Nacc_front_php\\Downloaded_EXCEL\\sss.xlsx'
    df = pd.read_excel(excel_path)

    link_column = None
    for col in df.columns:
        if any(df[col].apply(lambda x: isinstance(x, str) and x.startswith('http'))):
            link_column = col
            break
    for col in df.columns:
        if 'Money' in col:
         Money = col
         break
    
    for col in df.columns:
        if 'Month and Year of Award' in col:
         year_column = col
         break
    
    if link_column is not None:
        print(f"The column containing links is '{link_column}'")
        true_count = 0  # Initialize a variable to count the number of 'TRUE' occurrences
        Money_data1 = Money_data2 = Money_data3 = Money_data4 = Money_data5 = 0
        for index, shareable_link in df[link_column].items():
            file_id = extract_file_id_from_link(shareable_link)
            destination_folder = "Download_pdf"  # Absolute path to the destination folder
            os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists or create it if not
            download_file_from_google_drive(file_id, destination_folder)
            pdf_path = 'C:\\xampp\\htdocs\\Nacc_front_php\\Download_pdf\\'

            pdf_dwn = pdf_download(destination_folder)[0]
            temp=True
            for column_name in df.columns:
                if column_name == link_column:
                    continue  # Skip this column

                column_data = df.loc[index, column_name]
                if isinstance(column_data, date):
                    if pd.notnull(column_data):
                        target_word = pd.to_datetime(column_data).strftime('%Y-%m-%d')
                    else:
                        target_word = "NaT (Not a Time)"
                else:
                    target_word = str(column_data).upper().replace(' ', '')

                text = to_txt(pdf_dwn)
                scan_text_for_word(text, target_word)
            if cntt == 4:
                print("TRUE")
                go_to_search_for(Money,year_column,index)
                true_count += 1  # Increment the count for each 'TRUE' occurrence
            else:
                print("False")
                pass
            cntt = 0  # Reset the count for the next iteration
            shutil.rmtree(destination_folder)
        
        print(f"{true_count}")
        print(f"Money_data1: {Money_data1}") 
        print(f"Money_data2: {Money_data2}") 
        print(f"Money_data3: {Money_data3}") 
        print(f"Money_data4: {Money_data4}") 
        print(f"Money_data5: {Money_data5}") 
        total_money=Money_data1+Money_data2+Money_data3+Money_data4+Money_data5
        print(f"total_money: {total_money}")  
        average = total_money/5
        print(f"average: {average}")
        if average<1 :
            total_point=0
            print("the average value is 0")
        elif average >=1 and average<5 :
            total_point=1
            print ("the average value is 1")
        elif average >=5 and average<10 :
            total_point=2
            print ("the average value is 2")
        elif average >=10 and average<20 :
            total_point=3
            print ("the average value is 3")
        elif average >=20 :
            total_point=4
            print ("the average value is 4")
        highest_point =4
        highest_point_in_naac =8
        cnt_point =highest_point_in_naac/highest_point
        total_point_to_be_printed=cnt_point*total_point
        print(f"{total_point_to_be_printed}")
        shutil.rmtree(r'C:\xampp\htdocs\Nacc_front_php\Downloaded_EXCEL')

    else:
        print("No column contains links.")
