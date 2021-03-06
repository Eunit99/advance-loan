from flask import Flask ,render_template,request,flash,redirect,url_for, make_response #the render twmplate will be responsible for loading the html files

# from flask_wkhtmltopdf import Wkhtmltopdf
# import  wkhtmltopdf.WKHtmlToPdf

app =Flask(__name__) 

app.debug = True


@app.route('/')
def index():#function
    return render_template("index.html")
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/practice_area')
def practice_area():
    return render_template("practice-area.html")
@app.route('/attorney')
def attorney():
    return render_template("attorney.html")

@app.route('/simple_mail', methods=['post'])
def simple_mail():
    # return request.form
    try:
        msg = Message("A website Visitor Query",
        sender=("Chweya And Advocates Website","chweyaandavocateswebsite@gmail.com"),
        recipients=["nyasingajeff@gmail.com"])
        msg.body = f"We Hope this finds You well,\n\n Mr/Mrs {request.form['name'].capitalize()}  had a query concerning {request.form['area']} , The specific Question was :- \n\n {request.form['question'].capitalize()} \n\nHis or Her Return email is  {request.form['email']} \n Regards , \n\n The Chweya And Avocates Website"           
        mail.send(msg)
        # flash('Your Query was Successfuly submitted','success')
        # return render_template("index.html")
    except Exception as e:
        return e

    return render_template("attorney.html")

@app.route('/contact_mail', methods=['post'])
def contact_mail():
    # return request.form
    env = Environment(loader=FileSystemLoader('site/templates'))
    template = env.get_template("form.html")
    template_vars = {'todays_date':dt.today().strftime('%Y-%m-%d') ,'name': request.form['name'] , 'lastname': request.form['lastname'] ,'dob':request.form['dob'] , 'bussiness_name': request.form['bussiness_name'] , 'address':request.form['bussiness_adress'] ,'city': request.form['city'] ,'state':  request.form['state'], 'zip': request.form['zip'] ,'h_telephone': request.form['h_telephone'] ,'fax': request.form['fax'] , 'email':request.form['email'] , 'employer': request.form['employer'] , 'emp_tel': request.form['empl_tel'], 'description': request.form['message'] ,'papers':request.form['papers'] , 'serving_date': request.form['papers_date'] , 'court_date': request.form['court_date'] , 'judge': request.form['judge'] , 'associated_parties': request.form['associates'], 'other_sides_name': request.form['other_sides_name'],'opposing_cousel': request.form['opposing_counsel'] , 'spouse_name':request.form['spouse'],'spouses_employer':request.form['spouse_employer'] ,'phone': request.form['spouse_phone']  ,'reffered_by':request.form['refferee']  ,'contact': request.form['prevous_contacts'] ,'other_artorney':  request.form['attorney'] }  
    html_out = template.render(template_vars)
    # return html_out
    try:
        pdfkit.from_string( html_out,'site/consultation.pdf')
    except Exception as e:
        a=e

    pdf = 'consultation.pdf'

    # return pdf
    try:
        msg = Message(f"{ request.form['name'].capitalize()}'.' '.{request.form['lastname'].capitalize()} Consultation form",
        sender=("Chweya And Advocates Website","chweyaandavocateswebsite@gmail.com"),
        # subject='Online Consultation Form ',
        recipients=["nyasingajeff@gmail.com"])
        msg.body = f" Mr or Mrs , { request.form['name'].capitalize()}, Submitted  The above data. \n Regards \n\n\n The Chweya And Advocates Website ."         
        

        with app.open_resource(pdf) as fp:
            msg.attach("consultation.pdf",'application/pdf', fp.read())
        
        
        mail.send(msg)
        # flash('Your Query was Successfuly submitted','success')
        # return render_template("index.html")
    except Exception as e:
       a=e

    return render_template("attorney.html")



    

if __name__ == "__main__":
    app.run(debug=True) 
