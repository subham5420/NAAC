from flask import Flask,render_template,request,redirect,url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/3.1')
def criteria3_1():
    return render_template('3.1.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get all form data for Criteria 3.1.2
    user_input_312 = request.form['312list']
    year_range1_312 = request.form['312year_range1']
    lakhs1_312 = request.form['312Lakhs1']
    year_range2_312 = request.form['312year_range2']
    lakhs2_312 = request.form['312Lakhs2']
    year_range3_312 = request.form['312year_range3']
    lakhs3_312 = request.form['312Lakhs3']
    year_range4_312 = request.form['312year_range4']
    lakhs4_312 = request.form['312Lakhs4']
    year_range5_312 = request.form['312year_range5']
    lakhs5_312 = request.form['312Lakhs5']
    
    # Execute the Python script with form data
    command = f"python full_total_copy.py {user_input_312} {year_range1_312} {year_range2_312} {year_range3_312} {year_range4_312} {year_range5_312} {lakhs1_312} {lakhs2_312} {lakhs3_312} {lakhs4_312} {lakhs5_312}"
    output_312 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_312}")

    # Get all form data for Criteria 3.1.3
    user_input_313 = request.form['313list']
    year_range1_313 = request.form['313year_range1']
    lakhs1_313 = request.form['313number1']
    year_range2_313 = request.form['313year_range2']
    lakhs2_313 = request.form['313number2']
    year_range3_313 = request.form['313year_range3']
    lakhs3_313 = request.form['313number3']
    year_range4_313 = request.form['313year_range4']
    lakhs4_313 = request.form['313number4']
    year_range5_313 = request.form['313year_range5']
    lakhs5_313 = request.form['313number5']
    
    # Execute the Python script with form data
    command = f"python sample11_3.1.3.py {user_input_313} {year_range1_313} {year_range2_313} {year_range3_313} {year_range4_313} {year_range5_313} {lakhs1_313} {lakhs2_313} {lakhs3_313} {lakhs4_313} {lakhs5_313}"
    output_313 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_313}")

    # Get all form data for Criteria 3.2.1
    user_input_321 = request.form['321list']
    year_range1_321 = request.form['321year_range1']
    lakhs1_321 = request.form['321number1']
    year_range2_321 = request.form['321year_range2']
    lakhs2_321 = request.form['321number2']
    year_range3_321 = request.form['321year_range3']
    lakhs3_321 = request.form['321number3']
    year_range4_321 = request.form['321year_range4']
    lakhs4_321 = request.form['321number4']
    year_range5_321 = request.form['321year_range5']
    lakhs5_321 = request.form['321number5']
    
    # Execute the Python script with form data
    command = f"python full_total_copy.py {user_input_321} {year_range1_321} {year_range2_321} {year_range3_321} {year_range4_321} {year_range5_321} {lakhs1_321} {lakhs2_321} {lakhs3_321} {lakhs4_321} {lakhs5_321}"
    output_321 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_321}")

    # Get all form data for Criteria 3.2.2
    user_input_322 = request.form['322list']
    year_range1_322 = request.form['322year_range1']
    lakhs1_322 = request.form['322number1']
    year_range2_322 = request.form['322year_range2']
    lakhs2_322 = request.form['322number2']
    year_range3_322 = request.form['322year_range3']
    lakhs3_322 = request.form['322number3']
    year_range4_322 = request.form['322year_range4']
    lakhs4_322 = request.form['322number4']
    year_range5_322 = request.form['322year_range5']
    lakhs5_322 = request.form['322number5']
    
    # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_322} {year_range1_322} {year_range2_322} {year_range3_322} {year_range4_322} {year_range5_322} {lakhs1_322} {lakhs2_322} {lakhs3_322} {lakhs4_322} {lakhs5_322}"
    output_322 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_322}")

    # Get all form data for Criteria 3.2.4
    user_input_324 = request.form['324list']
    year_range1_324 = request.form['324year_range1']
    lakhs1_324 = request.form['324number1']
    year_range2_324 = request.form['324year_range2']
    lakhs2_324 = request.form['324number2']
    year_range3_324 = request.form['324year_range3']
    lakhs3_324 = request.form['324number3']
    year_range4_324 = request.form['324year_range4']
    lakhs4_324 = request.form['324number4']
    year_range5_324 = request.form['324year_range5']
    lakhs5_324 = request.form['324number5']
    
    # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_324} {year_range1_324} {year_range2_324} {year_range3_324} {year_range4_324} {year_range5_324} {lakhs1_324} {lakhs2_324} {lakhs3_324} {lakhs4_324} {lakhs5_324}"
    output_312 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_324}")

    # Get all form data for Criteria 3.3.2
    user_input_332 = request.form['332list']
    year_range1_332 = request.form['332year_range1']
    lakhs1_332 = request.form['332number1']
    year_range2_332 = request.form['332year_range2']
    lakhs2_332 = request.form['332number2']
    year_range3_332 = request.form['332year_range3']
    lakhs3_332 = request.form['332number3']
    year_range4_332 = request.form['332year_range4']
    lakhs4_332 = request.form['332number4']
    year_range5_332 = request.form['332year_range5']
    lakhs5_332 = request.form['332number5']
    
    # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_332} {year_range1_332} {year_range2_332} {year_range3_332} {year_range4_332} {year_range5_332} {lakhs1_332} {lakhs2_332} {lakhs3_332} {lakhs4_332} {lakhs5_332}"
    output_332 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_332}")

    # Get all form data for Criteria 3.4.3
    user_input_343 = request.form['343list']
    year_range1_343 = request.form['343year_range1']
    lakhs1_343 = request.form['343number1']
    year_range2_343 = request.form['343year_range2']
    lakhs2_343 = request.form['343number2']
    year_range3_343 = request.form['343year_range3']
    lakhs3_343 = request.form['343number3']
    year_range4_343 = request.form['343year_range4']
    lakhs4_343 = request.form['343number4']
    year_range5_343 = request.form['343year_range5']
    lakhs5_343 = request.form['343number5']
    
     # Execute the Python script with form data
    command = f"python 3.4.3.py {user_input_343} {year_range1_343} {year_range2_343} {year_range3_343} {year_range4_343} {year_range5_343} {lakhs1_343} {lakhs2_343} {lakhs3_343} {lakhs4_343} {lakhs5_343}"
    output_343 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_343}")
    

    # Get all form data for Criteria 3.4.4
    user_input_344 = request.form['344list']
    year_range1_344 = request.form['344year_range1']
    lakhs1_344 = request.form['344number1']
    year_range2_344 = request.form['344year_range2']
    lakhs2_344 = request.form['344number2']
    year_range3_344 = request.form['344year_range3']
    lakhs3_344 = request.form['344number3']
    year_range4_344 = request.form['344year_range4']
    lakhs4_344 = request.form['344number4']
    year_range5_344 = request.form['344year_range5']
    lakhs5_344 = request.form['344number5']
    
     # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_344} {year_range1_344} {year_range2_344} {year_range3_344} {year_range4_344} {year_range5_344} {lakhs1_344} {lakhs2_344} {lakhs3_344} {lakhs4_344} {lakhs5_344}"
    output_344 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_344}")

    # Get all form data for Criteria 3.5.1
    user_input_351 = request.form['351list']
    year_range1_351 = request.form['351year_range1']
    lakhs1_351 = request.form['351number1']
    year_range2_351 = request.form['351year_range2']
    lakhs2_351 = request.form['351number2']
    year_range3_351 = request.form['351year_range3']
    lakhs3_351 = request.form['351number3']
    year_range4_351 = request.form['351year_range4']
    lakhs4_351 = request.form['351number4']
    year_range5_351 = request.form['351year_range5']
    lakhs5_351 = request.form['351number5']
    
     # Execute the Python script with form data
    command = f"python full_total_copy.py {user_input_351} {year_range1_351} {year_range2_351} {year_range3_351} {year_range4_351} {year_range5_351} {lakhs1_351} {lakhs2_351} {lakhs3_351} {lakhs4_351} {lakhs5_351}"
    output_351 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_351}")

    # Get all form data for Criteria 3.5.2
    user_input_352 = request.form['352list']
    year_range1_352 = request.form['352year_range1']
    lakhs1_352 = request.form['352number1']
    year_range2_352 = request.form['352year_range2']
    lakhs2_352 = request.form['352number2']
    year_range3_352 = request.form['352year_range3']
    lakhs3_352 = request.form['352number3']
    year_range4_352 = request.form['352year_range4']
    lakhs4_352 = request.form['352number4']
    year_range5_352 = request.form['352year_range5']
    lakhs5_352 = request.form['352number5']
    
     # Execute the Python script with form data
    command = f"python full_total_copy.py {user_input_352} {year_range1_352} {year_range2_352} {year_range3_352} {year_range4_352} {year_range5_352} {lakhs1_352} {lakhs2_352} {lakhs3_352} {lakhs4_352} {lakhs5_352}"
    output_352 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_352}")

    # Get all form data for Criteria 3.6.2
    user_input_362 = request.form['362list']
    year_range1_362 = request.form['362year_range1']
    lakhs1_362 = request.form['362number1']
    year_range2_362 = request.form['362year_range2']
    lakhs2_362 = request.form['362number2']
    year_range3_362 = request.form['362year_range3']
    lakhs3_362 = request.form['362number3']
    year_range4_362 = request.form['362year_range4']
    lakhs4_362 = request.form['362number4']
    year_range5_362 = request.form['362year_range5']
    lakhs5_362 = request.form['362number5']
    
     # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_362} {year_range1_362} {year_range2_362} {year_range3_362} {year_range4_362} {year_range5_362} {lakhs1_362} {lakhs2_362} {lakhs3_362} {lakhs4_362} {lakhs5_362}"
    output_362 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_362}")

    # Get all form data for Criteria 3.6.3
    user_input_363 = request.form['363list']
    year_range1_363 = request.form['363year_range1']
    lakhs1_363 = request.form['363number1']
    year_range2_363 = request.form['363year_range2']
    lakhs2_363 = request.form['363number2']
    year_range3_363 = request.form['363year_range3']
    lakhs3_363 = request.form['363number3']
    year_range4_363 = request.form['363year_range4']
    lakhs4_363 = request.form['363number4']
    year_range5_363 = request.form['363year_range5']
    lakhs5_363 = request.form['363number5']
    
     # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_363} {year_range1_363} {year_range2_363} {year_range3_363} {year_range4_363} {year_range5_363} {lakhs1_363} {lakhs2_363} {lakhs3_363} {lakhs4_363} {lakhs5_363}"
    output_363 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_363}")

    # Get all form data for Criteria 3.6.4
    user_input_364 = request.form['364list']
    year_range1_364 = request.form['364year_range1']
    lakhs1_364 = request.form['364number1']
    year_range2_364 = request.form['364year_range2']
    lakhs2_364 = request.form['364number2']
    year_range3_364 = request.form['364year_range3']
    lakhs3_364 = request.form['364number3']
    year_range4_364 = request.form['364year_range4']
    lakhs4_364 = request.form['364number4']
    year_range5_364 = request.form['364year_range5']
    lakhs5_364 = request.form['364number5']
    
     # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_364} {year_range1_364} {year_range2_364} {year_range3_364} {year_range4_364} {year_range5_364} {lakhs1_364} {lakhs2_364} {lakhs3_364} {lakhs4_364} {lakhs5_364}"
    output_364 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_364}")

    # Get all form data for Criteria 3.7.1
    user_input_371 = request.form['371list']
    year_range1_371 = request.form['371year_range1']
    lakhs1_371 = request.form['371number1']
    year_range2_371 = request.form['371year_range2']
    lakhs2_371 = request.form['371number2']
    year_range3_371 = request.form['371year_range3']
    lakhs3_371 = request.form['371number3']
    year_range4_371 = request.form['371year_range4']
    lakhs4_371 = request.form['371number4']
    year_range5_371 = request.form['371year_range5']
    lakhs5_371 = request.form['371number5']
    
     # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_371} {year_range1_371} {year_range2_371} {year_range3_371} {year_range4_371} {year_range5_371} {lakhs1_371} {lakhs2_371} {lakhs3_371} {lakhs4_371} {lakhs5_371}"
    output_371 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_371}")

    # Get all form data for Criteria 3.7.2
    user_input_372 = request.form['372list']
    year_range1_372 = request.form['372year_range1']
    lakhs1_372 = request.form['372number1']
    year_range2_372 = request.form['372year_range2']
    lakhs2_372 = request.form['372number2']
    year_range3_372 = request.form['372year_range3']
    lakhs3_372 = request.form['372number3']
    year_range4_372 = request.form['372year_range4']
    lakhs4_372 = request.form['372number4']
    year_range5_372 = request.form['372year_range5']
    lakhs5_372 = request.form['372number5']
    
     # Execute the Python script with form data
    command = f"python 3.1.3.py {user_input_372} {year_range1_372} {year_range2_372} {year_range3_372} {year_range4_372} {year_range5_372} {lakhs1_372} {lakhs2_372} {lakhs3_372} {lakhs4_372} {lakhs5_372}"
    output_372 = subprocess.check_output(command, shell=True, text=True)
        
    # Display the output
    print(f"no of true occurs: {output_372}")

    # Render the results template with all the outputs
    return render_template('results.html',
                           output_312=output_312,
                           output_313=output_313,
                           output_321=output_321,
                           output_322=output_322,
                           output_324=output_324,
                           output_332=output_332,
                           output_343=output_343,
                           output_344=output_344,
                           output_351=output_351,
                           output_352=output_352,
                           output_362=output_362,
                           output_363=output_363,
                           output_364=output_364,
                           output_371=output_371,
                           output_372=output_372)


if __name__ == '__main__':
    app.run(debug=True)
