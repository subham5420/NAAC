import sys

# Get the user input from the command line argument
user_input = sys.argv[1]

import PyPDF3
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
from datetime import datetime

year_range1 = str(sys.argv[2])
#print(f"{year_range1}")
start_year1, end_year1 = map(int, year_range1.split('-'))
Month_start_year1 = 'July' + " " +str(start_year1)
Month_end_year1 ='June'+ " "+ str(end_year1)
#print(f"{Month_start_year1}")
#print(f"{Month_end_year1}")
start_date1 = datetime.strptime(Month_start_year1, "%B %Y").date()
end_date1 = datetime.strptime(Month_end_year1, "%B %Y").date()
#print(f"{start_date1}")
#print(f"{end_date1}")

year_range2 =sys.argv[3];
start_year2, end_year2 = map(int, year_range2.split('-'))
Month_start_year2 = 'July' +" "+ str(start_year2)
Month_end_year2 ='June'+" "+ str(end_year2)
start_date2 = datetime.strptime(f"{Month_start_year2}", "%B %Y").date()
end_date2 = datetime.strptime(f"{Month_end_year2}", "%B %Y").date()
#print(f"{start_date2}")
#print(f"{end_date2}")


year_range3 =sys.argv[4];
start_year3, end_year3 = map(int, year_range3.split('-'))
Month_start_year3 = 'July' +" "+ str(start_year3)
Month_end_year3 ='June'+" "+ str(end_year3)
start_date3 = datetime.strptime(f"{Month_start_year3}", "%B %Y").date()
end_date3 = datetime.strptime(f"{Month_end_year3}", "%B %Y").date()
#print(f"{start_date3}")
#print(f"{end_date3}")

year_range4 =sys.argv[5];
start_year4, end_year4 = map(int, year_range4.split('-'))
Month_start_year4 = 'July' +" "+ str(start_year4)
Month_end_year4 ='June'+" "+ str(end_year4)
start_date4 = datetime.strptime(f"{Month_start_year4}", "%B %Y").date()
end_date4 = datetime.strptime(f"{Month_end_year4}", "%B %Y").date()
#print(f"{start_date4}")
#print(f"{end_date4}")

year_range5 =sys.argv[6];
start_year5, end_year5 = map(int, year_range5.split('-'))
Month_start_year5 = 'July' +" "+ str(start_year5)
Month_end_year5 ='June'+" "+ str(end_year5)
start_date5 = datetime.strptime(f"{Month_start_year5}", "%B %Y").date()
end_date5 = datetime.strptime(f"{Month_end_year5}", "%B %Y").date()
#print(f"{start_date5}")
#print(f"{end_date5}")

Lakhs7 = sys.argv[7];
Lakhs8 = sys.argv[8];
Lakhs9 = sys.argv[9];
Lakhs10 = sys.argv[10];
Lakhs11 = sys.argv[11];

def check_link_in_set(shareable_link, empty_set):
    if shareable_link in empty_set:
        return True
    else:
        empty_set.add(shareable_link)
        return False
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

def restricted_or_not_pdf(url):
    try:
        file_id = re.search(r"/file/d/([a-zA-Z0-9_-]+)", url).group(1)
        download_url = f"https://drive.google.com/uc?id={file_id}"
        response = requests.get(download_url)
        if response.status_code == 200:
           # with open("downloaded_file.pdf", "wb") as file:
            #   file.write(response.content)
            return False
            print("PDF file can be downloaded.")
        else:
            print("PDF file can not  be downloaded.")
            return True
    except (requests.exceptions.RequestException, AttributeError) as e:
        return True     
        print ("Error: " + str(e)) 
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
def is_pdf_corrupted(file_path):
    try:
        with open(file_path, "rb") as file:
            _ = PyPDF3.PdfFileReader(file)
        return False
    except:
        return True
global cntt
cntt = 0
def exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
def scan_text_for_word(txt, target_word):
    global cntt
    if str(target_word) in txt:
        print(f"Found '{target_word}' in the text.")
        cntt += 1
    else:
        print(f"'{target_word}' not found in the text.")
        pass
def contains_folder_in_google_drive(shareable_link):
    if 'https://drive.google.com/drive/folders/' in shareable_link :
     return True
    else :
     return False
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
new_data =0        
def go_to_search_for(cntt,index):
    global Money_data1, Money_data2, Money_data3, Money_data4, Money_data5
    if cntt > 0:
        try:
            df[Date_column] = pd.to_datetime(df[Date_column]).dt.strftime('%B %Y')
            Date_data_in_excel = df.loc[index, Date_column]
            Date_data = datetime.strptime(str(Date_data_in_excel), "%B %Y").date()
            #print(f"start_date1: {start_date1}")
            #print(f"end_date1: {end_date1}")
            #print(f"{Date_data}")
            if start_date1 <= Date_data <= end_date1:
                #print("True")
                Money_data1 += 1
            if start_date2 <= Date_data <= end_date2:
                #print("True")
                Money_data2 += 1
            if start_date3 <= Date_data <= end_date3:
                Money_data3 += 1
                #print("True")
            if start_date4 <= Date_data <= end_date4:
                #print("True")
                Money_data4 += 1
            if start_date5 <= Date_data <= end_date5:
                #print("True")
                Money_data5 += 1
        except Exception as e:
            print(f"Error parsing date data: {e}")

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
    column_names = df.columns.tolist()
    num_row = df.shape[1]-1
    link_column = None
    for col in df.columns:
        if any(df[col].apply(lambda x: isinstance(x, str) and x.startswith('http'))):
            link_column = col
            break
    global Date_column
    target_word = 'Year'
    # Search for a specific word in column names
    Date_index =0
    found_columns = [(i, col) for i, col in enumerate(column_names) if target_word.lower() in col.lower()]

    if found_columns:
     #print(f"Columns containing '{target_word}':")
     for idx, col in found_columns:
        Date_index = idx
        Date_column =col
        #print(f"Index: {idx}, Name: {col}")
    else:
        
     print(f"No columns containing '{target_word}' found.")
   
    if link_column is not None:
        empty_set = set()
        #print(f"The column containing links is '{link_column}'")
        true_count = 0  # Initialize a variable to count the number of 'TRUE' occurrences
        Money_data1 = Money_data2 = Money_data3 = Money_data4 = Money_data5 = 0
        for index, shareable_link in df.iloc[2:, df.columns.get_loc(link_column)].items():
            if pd.isna(shareable_link):
             print(f"Skipping empty link at index {index + 1}")
             continue  # Skip empty links
            if not exists(shareable_link):
             print(f"Skipping inaccessible link at index {index + 1}")
             print(f"{shareable_link}")
             continue
            if contains_folder_in_google_drive(shareable_link):
                print(f"folder is in the link at index {index + 1}")
                continue
            if restricted_or_not_pdf(shareable_link):
                print("restricted")
                continue
            if check_link_in_set(shareable_link,empty_set):
                print(f"This link is duplicate  at {index + 1} as it is present at the excel in the above column")
                continue
            file_id = extract_file_id_from_link(shareable_link)
            destination_folder = "Download_pdf"  # Absolute path to the destination folder
            os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists or create it if not
            download_file_from_google_drive(file_id, destination_folder) 
           
            pdf_path = 'C:\\xampp\\htdocs\\Nacc_front_php\\Download_pdf\\'
            if not os.listdir(destination_folder):
                continue
            pdf_dwn = pdf_download(destination_folder)[0]
            
            if is_pdf_corrupted(pdf_dwn):
                print(f"This link might contain an image or the pdf is corrupted at {index + 1}")
                shutil.rmtree(destination_folder)
                continue         
            temp=True
            for column_name in df.columns:
                if column_name == link_column :
                    continue  # Skip this column
                #if column_name == Date_column:
                #skipping the date column
                # continue
                column_data = df.loc[index, column_name]
                #print(f"{column_data}")
                if pd.isna(column_data):
                  # Handle the case when column_data is NaN
                  target_word = "DATA IS NOT THERE IN EXCEL"
                elif  isinstance(column_data, float):
                    word = int(column_data)
                    target_word = str(word)
                else:
                 target_word = str(column_data).upper().replace(' ', '')
                 #print(f"{target_word}")
                text = to_txt(pdf_dwn)
                scan_text_for_word(text, target_word)
                 
            if cntt == num_row:
                print("TRUE")
                go_to_search_for(cntt,index)                
                true_count += 1  # Increment the count for each 'TRUE' occurrence
            else:
                print("False")
                pass
            cntt = 0  # Reset the count for the next iteration
            shutil.rmtree(destination_folder)
        
        print(f"{true_count}")
        print(f"System has detected number of teachers in {year_range1} : {Money_data1}") 
        print(f"System has detected number of teachers in {year_range2} : {Money_data2}") 
        print(f"System has detected number of teachers in {year_range3} : {Money_data3}") 
        print(f"System has detected number of teachers in {year_range4} :  {Money_data4}") 
        print(f"System has detected number of teachers in {year_range5} : {Money_data5}") 

        print(f"You have entered number of teachers in {year_range1} : {Lakhs7}") 
        print(f"You have entered number of teachers in {year_range2} : {Lakhs8}") 
        print(f"You have entered number of teachers in {year_range3} : {Lakhs9}") 
        print(f"You have entered number of teachers in {year_range4} :  {Lakhs10}") 
        print(f"You have entered number of teachers in {year_range5} : {Lakhs11}") 
        total_money= Money_data1 + Money_data2+Money_data3+Money_data4+Money_data5
        print(f"Number of teachers: {total_money}")  
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
        empty_set.clear()
        shutil.rmtree(r'C:\xampp\htdocs\Nacc_front_php\Downloaded_EXCEL')

    else:
        print("No column contains links.")
