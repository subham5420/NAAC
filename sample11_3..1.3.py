import sys
import fitz
# Get the user input from the command line argument
from PIL import Image
import easyocr
import win32com.client
import PyPDF3
import os
import requests
import datetime
import pandas as pd
from urllib.parse import parse_qs, urlparse
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
from urllib.parse import urlparse, parse_qs
from docx import Document
from temp import get_confirm_token, save_response_content

"""
user_input = sys.argv[1]
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

"""
def extract_file_id_from_link(link):
    """Extracts the file ID from a Google Drive shareable link."""
    match = re.search(r'/file/d/([a-zA-Z0-9_-]+)', str(link))
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Google Drive shareable link")

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
def pdf_download(pdf_path):
    filenames = []
    for filename in os.listdir(pdf_path):
        if filename.endswith(".pdf"):
            filenames.append(os.path.join(pdf_path, filename))
    return filenames
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
def image_download(image_path):
    filenames = []
    for filename in os.listdir(image_path):
        if filename.endswith(( ".jpeg")):
            filenames.append(os.path.join(image_path, filename))
    return filenames
def word_in_img(img_dwn):
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(img_dwn)
    return''.join([detection[1].upper().replace(' ', '') for detection in result])


def download_doc_from_google_drive(drive_link, pdf_output_path):
    query = urlparse(drive_link).query
    parsed_query = parse_qs(query)
    file_id = parsed_query.get('id', [None])[0]

    if file_id is None:
        # Try extracting from the path
        path_parts = urlparse(drive_link).path.split('/')
        file_id = path_parts[3] if len(path_parts) > 3 else None

    if file_id is None:
        raise ValueError("No 'id' parameter found in the Google Drive link.")

    # Download URL for the file
    download_url = f"https://docs.google.com/uc?id={file_id}"

    # Send a GET request to download the file
    response = requests.get(download_url)
    
    # Save the downloaded file to the specified path
    doc_output_path = os.path.join(pdf_output_path, 'download.doc')
    with open(doc_output_path, 'wb') as f:
        f.write(response.content)

    #return doc_output_path
def doc_to_text(doc_file_path):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(doc_file_path)
    text = doc.Content.Text
    doc.Close()
    word.Quit()
    return text
def doc_ok(doc_path):
    try:
        # Try to open the file as a DOCX document
        with open(doc_path, 'rb') as file:
            doc = Document(file)
        # If no exception is raised, the file can be opened as a DOCX document
        return True
    except Exception as e:
        # If an exception is raised, the file cannot be opened as a DOCX document
        return False
def is_it_doc(shareable_link):
       doc_output_path = 'Download_doc'
       os.makedirs(doc_output_path, exist_ok=True)
       download_doc_from_google_drive(shareable_link,doc_output_path)
       doc_path = 'C:\\xampp\\htdocs\\Nacc_front_php\\Download_doc\\download.doc'
       if doc_ok(doc_path):
           return True
       else:
           return False
def to_txt(pdf_path):
    image_output_path = 'images/'
    # Create the images directory if it doesn't exist
    os.makedirs(image_output_path, exist_ok=True)
    # Open the PDF file
    pdf_file = fitz.open(pdf_path)
    text = ""

    # Iterate through each page of the PDF
    for page_num in range(pdf_file.page_count):
        # Get the page
        page = pdf_file.load_page(page_num)
        
        # Convert the page to an image
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save the image
        img_path = f'{image_output_path}page_{page_num + 1}.png'
        img.save(img_path)

        # Replace 'en' with the language code of the text in your image
        reader = easyocr.Reader(['en'], gpu=True)

        # Perform OCR on the image
        result = reader.readtext(img_path)

        # Append the extracted text to the text variable
        text += ''.join([detection[1].upper().replace(' ', '') for detection in result])

    # Close the PDF file
    pdf_file.close()

    return text
    
def scan_text_for_word(txt, target_word):
    
    if str(target_word) in txt:
        print(f"Found '{target_word}' in the text.")
        return True
    else:
        print(f"'{target_word}' not found in the text.")
        return False
global cntt
cntt = 0
def exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
def contains_folder_in_google_drive(shareable_link):
    if 'https://drive.google.com/drive/folders/' in shareable_link :
     return True
    else :
     return False
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
def check_link_in_set(shareable_link, empty_set):
    if shareable_link in empty_set:
        return True
    else:
        empty_set.add(shareable_link)
        return False
if __name__ == "__main__":
    global img_not_corrup_cnt,oddword,arghatemp
    global doccnt
    doccnt=0
    img_not_corrup_cnt = 0  
    oddword = 0
    arghatemp = True
    output_folder = 'Downloaded_EXCEL'
    sheet_url = "https://docs.google.com/spreadsheets/d/1Lj5u3KQ9iEWf7TxR4x7i0Z143YADecnZ/edit#gid=1388000206"
    
    download_google_sheets_as_excel(sheet_url, output_folder)

    directory_path = r'C:\xampp\htdocs\Nacc_front_php\Downloaded_EXCEL'
    new_excel_name = 'sss.xlsx'
    rename_excel_in_directory(directory_path, new_excel_name)

    excel_path = r'C:\xampp\htdocs\Nacc_front_php\Downloaded_EXCEL\sss.xlsx'
    df = pd.read_excel(excel_path)
    column_names = df.columns.tolist()
    num_row = df.shape[0]  # Use shape[0] to get the number of rows
    link_column = None
    for col in df.columns:
        if any(df[col].apply(lambda x: isinstance(x, str) and x.startswith('http'))):
            link_column = col
            break
    empty_set = set()
    Money_data1 = Money_data2 = Money_data3 = Money_data4 = Money_data5 = 0

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
        doc_output_path = 'Download_doc'
        if not "https://docs.google.com/document/" in   shareable_link :
         file_id = extract_file_id_from_link(shareable_link)
        destination_folder = "Download_pdf"  # Absolute path to the destination folder
        destination_img_folder = "Download_img"
        image_output_path ="images"
        os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists or create it if not
        os.makedirs(destination_img_folder, exist_ok=True)
        os.makedirs(doc_output_path,exist_ok=True)
        os.makedirs(image_output_path,exist_ok=True) 
        download_file_from_google_drive(file_id, destination_folder)
        download_img_file_from_google_drive(file_id, destination_img_folder)
           
        pdf_path = 'C:\\xampp\\htdocs\\Nacc_front_php\\Download_pdf\\'
        if not os.listdir(destination_folder):
            continue
        pdf_dwn = pdf_download(destination_folder)[0]
        img_path = 'C:\\xampp\\htdocs\\Nacc_front_php\\Download_img\\'  
        img_dwn = image_download(destination_img_folder)[0]
        if is_pdf_corrupted(pdf_dwn):
            if is_img_corrupted(img_dwn) :
               if is_it_doc(shareable_link):
                 doc_file_path = r'C:\xampp\htdocs\Nacc_front_php\downloaded_file.doc'
                 doc_text = doc_to_text(doc_file_path)
                 doccnt=doccnt+1
                 
               else:
                  print(f"This link is not working at {index+1}")
                  shutil.rmtree(destination_folder)
                  shutil.rmtree(destination_img_folder)
                  shutil.rmtree(doc_output_path)
                  continue
            else:
                 
                detected_text = word_in_img(img_dwn)
                print(f"{detected_text}")
                img_not_corrup_cnt = 0 
                img_not_corrup_cnt = img_not_corrup_cnt+1  #image is not corrupted      
        else:
            text = to_txt(pdf_dwn)
            print(f"{text}")
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
                 target_word = str(column_data).upper()
                 #print(f"{target_word}")
                parts = re.split(r'\s+', target_word)
                 
                if img_not_corrup_cnt > 0:
                   
                   #print(f"{detected_text}")
                   for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
                       if part == "":
                        continue 
                    elif part.startswith("PROF."):
                       part = part.removesuffix("PROF.")
                       if part == "":
                        continue
                       
                    if part.endswith("ed"):
                        part = part.removesuffix("ed")
                    elif part.endswith("s"):
                        part = part.removesuffix("s") 
                    elif part.endswith("es"):
                        part = part.removesuffix("es")
                    elif part.endswith("ion"):
                        part = part.removesuffix("ion")                 
                    if scan_text_for_word(detected_text, part):
                        if "BEST" in part:
                         oddword=oddword+1
                        elif "PAPER" in part:
                         oddword = oddword+1
                        if oddword == 2:
                            print("best paper found")
                            break
                        print(f"found {part}")
                    else :
                        print(f"not found1:{part}")
                        arghatemp = False
                elif doccnt > 0 :
                 for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
                       if part == "":
                        continue
                    elif part.startswith("PROF."):
                       part = part.removesuffix("PROF.")
                       if part == "":
                        continue
                       
                    if part.endswith("ed"):
                        part = part.removesuffix("ed")
                    elif part.endswith("s"):
                        part = part.removesuffix("s") 
                    elif part.endswith("es"):
                        part = part.removesuffix("es")
                    elif part.endswith("ion"):
                        part = part.removesuffix("ion")   
                    if scan_text_for_word(doc_text, part):
                        if "BEST" in part:
                         oddword=oddword+1
                        elif "PAPER" in part:
                         oddword = oddword+1
                        if oddword == 2:
                            print("best paper found")
                            break
                        print(f"found {part}")
                    else :
                        print(f"not founddoc:{part}")
                        arghatemp = False           
                else:                  
                   for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
                       if part == "":
                        continue
                    elif part.startswith("PROF."):
                       part = part.removesuffix("PROF.")
                       if part == "":
                        continue
                    if part.endswith("ed"):
                        part = part.removesuffix("ed")
                    elif part.endswith("s"):
                        part = part.removesuffix("s") 
                    elif part.endswith("es"):
                        part = part.removesuffix("es")
                    elif part.endswith("ion"):
                        part = part.removesuffix("ion")
                    if scan_text_for_word(text,part):
                        if "BEST" in part:
                         oddword=oddword+1
                        elif "PAPER" in part:
                         oddword = oddword+1
                        if oddword == 2:
                            print("best paper found")
                            break
                        print(f"found {part}")
                    else :
                        print(f"not found:{part}")
                        arghatemp = False
        oddword = 0
                  
        #detected_text='' 
        shutil.rmtree(destination_img_folder)
        shutil.rmtree(doc_output_path)
        shutil.rmtree(image_output_path)
        img_not_corrup_cnt = 0 
        shutil.rmtree(destination_folder)   
        print(f"{arghatemp}")
        arghatemp = True
   
   