from flask import Flask
   
app = Flask(__name__)
  
@app.route("/",methods=["GET"])
def root():
    return "Welcome to my ITIL exam"

@app.route("/modules",methods=["GET"])
def root():
    return "1] Fundamentals of Networkings
            2] Consepts of Operating Systems and Administration
            3] ITIL and DevOps
            4] Networks Deffense and Countermessures
            5] Public Key Infrastructure
            6] Complaince Audit
            7] Cyber Forensics
            8] Apptitude
            9] Project"

@app.route("/me",methods=["GET"])
  6 def root():
  7     return "Name : Arpit Madhukarrao Ikhankar (Patil)
                PRN : 230344223022
                Phone  Number : 8788357822"
pp.run(host="0.0.0.0",port=4000, debug=True)
