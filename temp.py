import sys

# Get the user input from the command line argument
from PIL import Image
import easyocr
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
    URL = "https://drive.google.com/uc?export=download"
    destination = os.path.join(destination_folder, f"{file_id}.pdf")
    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
    
    save_response_content(response, destination)

    
def download_img_file_from_google_drive(file_id, destination_img_folder):
    """Downloads a file from Google Drive given its file ID."""
    URL_img = "https://drive.google.com/uc?export=download"
    destination = os.path.join(destination_img_folder, f"{file_id}.jpeg")
    session = requests.Session()

    response = session.get(URL_img, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL_img, params=params, stream=True)
    
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
    pdf_text = ''.join(text.upper().split())
    print(f"{pdf_text}")
    return pdf_text

def pdf_download(pdf_path):
    filenames = []
    for filename in os.listdir(pdf_path):
        if filename.endswith(".pdf"):
            filenames.append(os.path.join(pdf_path, filename))
    return filenames
def image_download(image_path):
    filenames = []
    for filename in os.listdir(image_path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
            filenames.append(os.path.join(image_path, filename))
    return filenames

def is_pdf_corrupted(file_path):
    try:
        with open(file_path, "rb") as file:
            _ = PyPDF3.PdfFileReader(file)
        return False
    except:
        return True
def is_img_corrupted(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
            print("image is verified")  # Attempt to open and verify the image
        return False  # Image is not corrupted
    except OSError:
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
def word_in_img(img_dwn,detected_text):
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(img_dwn)
    detected_text = ''.join([detection[1].upper().replace(' ', '') for detection in result])
    print(detected_text, end='')
    
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
if __name__ == "__main__":
    empty_set = set()
    global detected_text
    detected_text=''
    global img_not_corrup_cnt
    img_not_corrup_cnt = 0  
    output_folder = 'Downloaded_EXCEL'
    sheet_url = "https://docs.google.com/spreadsheets/d/1DL2MsEK1PAqitg0LNyYcg22bY32bqRoBZz7A1zavL2A/edit#gid=0"
    
    download_google_sheets_as_excel(sheet_url, output_folder)

    directory_path = r'C:\Users\HP\Desktop\sample11\Downloaded_EXCEL'
    new_excel_name = 'sss.xlsx'
    rename_excel_in_directory(directory_path, new_excel_name)

    excel_path = r'C:\Users\HP\Desktop\sample11\Downloaded_EXCEL\sss.xlsx'
    df = pd.read_excel(excel_path)
    column_names = df.columns.tolist()
    num_row = df.shape[0]  # Use shape[0] to get the number of rows
    link_column = None
    for col in df.columns:
        if any(df[col].apply(lambda x: isinstance(x, str) and x.startswith('http'))):
            link_column = col
            break

    for index, shareable_link in df.iloc[1:, df.columns.get_loc(link_column)].items():
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
        destination_img_folder = "Download_img"
        os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists or create it if not
        os.makedirs(destination_img_folder, exist_ok=True) 
        download_file_from_google_drive(file_id, destination_folder)
        download_img_file_from_google_drive(file_id, destination_img_folder)
           
        pdf_path = 'C:\\Users\\HP\\Desktop\\sample11\\Download_pdf\\'
        if not os.listdir(destination_folder):
            continue
        pdf_dwn = pdf_download(destination_folder)[0]
        img_path = 'C:\\Users\\HP\\Desktop\\sample11\\Download_img\\'  
        img_dwn = image_download(destination_img_folder)[0]
        if is_pdf_corrupted(pdf_dwn):
            if is_img_corrupted(img_dwn) :
             print(f"This link might contain an image or the pdf is corrupted at {index + 1}")
             shutil.rmtree(destination_folder)
             shutil.rmtree(destination_img_folder)
             
             continue 
            else:
                shutil.rmtree(destination_folder) 
                word_in_img(img_dwn,detected_text)
                img_not_corrup_cnt = img_not_corrup_cnt+1  #image is not corrupted      
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
                 print(f"{target_word}")
                if img_not_corrup_cnt > 0:
                   scan_text_for_word(detected_text, target_word) 
                   
                else:
                   text = to_txt(pdf_dwn)
                   scan_text_for_word(text, target_word)
        detected_text='' 
        shutil.rmtree(destination_img_folder)      
        if cntt == num_row:
            print("TRUE")
            img_not_corrup_cnt = 0
        else:
            print("False")
