from flask import Flask, render_template, url_for


app = Flask(__name__)

blogData=[{
    "id":1,
    "title":"Welcome to the new blog",
    "body":"Book description: In June, 1954, eighteen-year-old Emmett Watson is driven home to Nebraska by the warden of the juvenile work farm where he has just served fifteen months for involuntary manslaughter. His mother long gone, his father recently deceased, and the family farm foreclosed upon by the bank, Emmett's intention is to pick up his eight-year-old brother, Billy, and head to California where they can start their lives anew. But when the warden drives away, Emmett discovers that two friends from the work farm have hidden themselves in the trunk of the warden's car. Together, they have hatched an altogether different plan for Emmett's future, one that will take them all on a fateful journey in the opposite direction—to the City of New York.",
    "likes":30
},{
    "id":2,
    "title":"How to be a good programmer",
    "body":"Book description: In June, 1954, eighteen-year-old Emmett Watson is driven home to Nebraska by the warden of the juvenile work farm where he has just served fifteen months for involuntary manslaughter. His mother long gone, his father recently deceased, and the family farm foreclosed upon by the bank, Emmett's intention is to pick up his eight-year-old brother, Billy, and head to California where they can start their lives anew. But when the warden drives away, Emmett discovers that two friends from the work farm have hidden themselves in the trunk of the warden's car. Together, they have hatched an altogether different plan for Emmett's future, one that will take them all on a fateful journey in the opposite direction—to the City of New York.",
    "likes":20
},{
    "id":3,
    "title":"How to delete a post",
    "body":"Book description: In June, 1954, eighteen-year-old Emmett Watson is driven home to Nebraska by the warden of the juvenile work farm where he has just served fifteen months for involuntary manslaughter. His mother long gone, his father recently deceased, and the family farm foreclosed upon by the bank, Emmett's intention is to pick up his eight-year-old brother, Billy, and head to California where they can start their lives anew. But when the warden drives away, Emmett discovers that two friends from the work farm have hidden themselves in the trunk of the warden's car. Together, they have hatched an altogether different plan for Emmett's future, one that will take them all on a fateful journey in the opposite direction—to the City of New York.",
    "likes":31
},{
    "id":4,
    "title":"This is the end of the world",
    "body":"Book description: In June, 1954, eighteen-year-old Emmett Watson is driven home to Nebraska by the warden of the juvenile work farm where he has just served fifteen months for involuntary manslaughter. His mother long gone, his father recently deceased, and the family farm foreclosed upon by the bank, Emmett's intention is to pick up his eight-year-old brother, Billy, and head to California where they can start their lives anew. But when the warden drives away, Emmett discovers that two friends from the work farm have hidden themselves in the trunk of the warden's car. Together, they have hatched an altogether different plan for Emmett's future, one that will take them all on a fateful journey in the opposite direction—to the City of New York.",
    "likes":15
}]

@app.route("/")
def home():
    return render_template('home.html', posts=blogData, title="Home")
@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/login")
def login():
    return render_template('./authentication/login.html', title="Login")

@app.route("/register")
def register():
    return render_template('./authentication/register.html', title="Register")


if __name__=='__main__':
    app.run(debug=True)