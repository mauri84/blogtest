from flask.ext.wtf import Form
from wtforms import TextField, validators, PasswordField, TextAreaField, SubmitField, HiddenField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Person, Article, Category

strip_filter = lambda x: x.strip() if x else None

def category_choice():
    return Category.query.all()

class ArticleCreateForm(Form):
    title = TextField('Title', [validators.Required("Please enter Title.")], filters=[strip_filter])
    body = TextAreaField('Body', [validators.Required("Please enter body.")], filters=[strip_filter])
    url = TextField('URL ://', filters=[strip_filter])
    category = QuerySelectField('Category', query_factory=category_choice )
    person_name = HiddenField()
    arch_local = HiddenField()

class ArticleUpdateForm(ArticleCreateForm):
    id = HiddenField()

class SignupForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name", [validators.Required("Please enter your last name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])

    def __init__(self, *args, **kargs):
        Form.__init__(self, *args, **kargs)

    def validate(self):
        if not Form.validate(self):
            return False

        person = Person.query.filter_by(email=self.email.data.lower()).first()
        if person:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True

class SigninForm(Form):
    email = TextField("Email", [validators.Required("Please enter your email.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kargs):
        Form.__init__(self, *args, **kargs)

    def validate(self):
        if not Form.validate(self):
            return False

        person = Person.query.filter_by(email=self.email.data.lower()).first()
        if person and person.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid Password")
            return False 

class CategoryCreateForm(Form):
    name = TextField('Name', [validators.Required(), validators.length(min=1, max=240)])
    description = TextAreaField('Description', [validators.Required()])

class PersonUpdateForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name", [validators.Required("Please enter your last name.")])
    password = PasswordField("Password", [validators.Required("Please enter a password.")])

