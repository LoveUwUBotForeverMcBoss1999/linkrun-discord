from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_discord():
    return redirect("https://discord.gg/78ZeMES4xC")

if __name__ == '__main__':
    app.run()
