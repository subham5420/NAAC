if img_not_corrup_cnt > 0:
                   
                   #print(f"{detected_text}")
                   for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
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
                elif doccnt > 0 :
                 for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
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
                                   
                else:                  
                   for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
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
                 #print(f"{target_word}")
                if img_not_corrup_cnt > 0:
                   
                   #print(f"{detected_text}")
                   for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
                       if part == "":
                        continue                  
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
                 elif doccnt > 0 :
                  for part in parts :
                    if part.startswith("DR."):
                       part = part.removesuffix("DR.")
                       if part == "":
                        continue
                       
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
                                   
                 else:                  
                   for part in parts :
                     if part.startswith("DR."):
                       part = part.removesuffix("DR.")
                       if part == "":
                        continue
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
                 
            if cntt == num_row:
                print("TRUE")
                go_to_search_for(cntt,index)                
                true_count += 1  # Increment the count for each 'TRUE' occurrence
            else:
                print("False")
                pass
            cntt = 0
            img_not_corrup_cnt = 0
            oddword = 0  
            shutil.rmtree(destination_folder)
            shutil.rmtree(destination_img_folder)
            shutil.rmtree(doc_output_path)
            shutil.rmtree(image_output_path)
            
            