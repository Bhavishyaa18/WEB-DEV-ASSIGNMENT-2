from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "secret123"

events_data = [
    {
        "id": 1,
        "name": "Music Fest",
        "date": "10 April",
        "venue": "Delhi",
        "image": "images/music.jpg"
    },
    {
        "id": 2,
        "name": "Tech Conference",
        "date": "15 April",
        "venue": "Noida",
        "image": "images/tech.jpg"
    },
    {
        "id": 3,
        "name": "Art Expo",
        "date": "20 April",
        "venue": "Gurgaon",
        "image": "images/art.jpg"
    },
    {
        "id": 4,
        "name": "Startup Meetup",
        "date": "25 April",
        "venue": "Delhi",
        "image": "images/startup.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html', events=events_data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        flash(f"Thank you {name}, registration successful!")
        return redirect('/events')

    return render_template('register.html', events=events_data)

@app.route('/admin')
def admin():
    return render_template('admin.html', events=events_data)

@app.route('/admin/add', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    venue = request.form['venue']
    image = request.form['image']

    new_event = {
        "id": len(events_data)+1,
        "name": name,
        "date": date,
        "venue": venue,
        "image": image
    }

    events_data.append(new_event)
    return redirect('/admin')

@app.route('/admin/delete/<int:id>')
def delete_event(id):
    global events_data
    events_data = [e for e in events_data if e['id'] != id]
    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)