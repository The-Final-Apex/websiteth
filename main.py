from flask import Flask, render_template, request, redirect, url_for

import smtplib
from email.mime.text import MIMEText

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    company_overview = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut risus in augue luctus venenatis. Sed tincidunt, magna a ultricies accumsan,
    
mienim tempor lorem, ut efficitur sem magna vel tellus. Cras posuere libero rhoncus, aliquam eros fringilla, rutrum mi. Fusce at placerat urna, vel aliquet magna. Nullam ac ullamcorper augue, a suscipit tellus. Donec euismod, nisl eget ultricies tincidunt, nunc justo efficitur enim, a aliquam magna eros quis nisl.

"""
    return render_template('about.html', company_overview=company_overview)


@app.route('/products')
def products():
    products = [
        {
            'name': 'Product 1',
            'description': 'Description of Product 1',
            'price': 9.99,
            'image': 'product1.jpg'
        },
        {
            'name': 'Product 2',
            'description': 'Description of Product 2',
            'price': 14.99,
            'image': 'product2.jpg'
        },
        {
            'name': 'Product 3',
            'description': 'Description of Product 3',
            'price': 19.99,
            'image': 'product3.jpg'
        }
    ]
    return render_template('products.html', products=products)



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Configure email settings
        sender = email
        recipient = 'Python_is_cool@outlook.com'
        subject = 'New Message from Contact Form'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        # Send the email
        try:
            with smtplib.SMTP('outlook') as smtp:
                smtp.send_message(msg)
            return render_template('contact.html', message='Message sent successfully!')
        except Exception as e:
            return render_template('contact.html', message='Error sending message. Please try again later.')

    return render_template('contact.html')

@app.route('/careers')
def careers():
    company_culture = "At our company, we value innovation, teamwork, and a positive work-life balance. We are always looking for talented individuals to join our growing team."
    job_openings = [
        {
            'title': 'Software Engineer',
            'description': 'We are seeking a skilled software engineer to join our development team.',
            'requirements': ['Bachelor\'s degree in Computer Science or related field', 'Proficient in Python, JavaScript, and SQL', '3+ years of experience in software development']
        },
        {
            'title': 'Marketing Coordinator',
            'description': 'We are looking for a creative and organized marketing coordinator to help us promote our products.',
            'requirements': ['Bachelor\'s degree in Marketing or Communications', '2+ years of experience in digital marketing', 'Strong writing and communication skills']
        },
        {
            'title': 'Customer Service Representative',
            'description': 'We are hiring a friendly and knowledgeable customer service representative to assist our clients.',
            'requirements': ['High school diploma or equivalent', '1+ year of customer service experience', 'Excellent problem-solving and communication skills']
        }
    ]
    return render_template('careers.html', company_culture=company_culture, job_openings=job_openings)


if __name__ == '__main__':
    app.run(debug=True)

