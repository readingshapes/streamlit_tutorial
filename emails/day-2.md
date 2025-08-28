**Subject**: Day 2: Set Up Your Streamlit App Locally 🛠

Welcome to Day 2 of **Learn to Build Data Apps with Streamlit**!

Today’s goal is to get the demo app running on your computer. This is the only setup-heavy day—after this, we’ll focus on building and customizing your app.

Let's break it into two parts: "One-Time Setup" and "Steps You'll Repeat".

## ✅ One-Time Setup

These steps only need to be done once:

**1. Fork the course repo**

The course repo can be found **[here](https://github.com/arilamstein/streamlit_tutorial)**. Forking creates your own copy of the tutorial. You’ll need this later when you deploy your app, so don’t skip it! 

👉 [How to fork a repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

**2. Clone your fork**

Now clone your fork of the repo. If you don't know how to do this, read the instructions here:

👉 [How to clone a repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

**3. Install `uv`**

uv is a fast Python package manager. You’ll use it to install everything you need. 

👉 [Install instructions](https://docs.astral.sh/uv/#installation)

**4. Create your virtual environment**

Inside your project folder, type:

`uv sync`

That’s it for uv—you won’t need to use it again during this course.

## 🔁 Steps You’ll Repeat

**Activate your virtual environment**

In your project directory, run:

`source .venv/bin/activate`

You'll need to do this each time you open a new terminal.

**Run the demo app**

Once your virtual environment is active, type:

`streamlit run streamlit_app.py`

This launches the app in your browser. If everything's working, you'll see something like this:

<p align="center">
  <img src="../screenshot-demo-app.png" alt="Demo App Screenshot" width="50%">
</p>

## 🧠 Tips

  * If you get stuck, reply to this email—I’m happy to help.
  * You can preview the final app [here](https://arilamstein-tutorial.streamlit.app/) to see where we’re headed.
  * Tomorrow, we’ll start customizing the app and adding new charts.

You’ve got this. One step at a time.

Ari

PS Finished early? You can peek ahead to tomorrow's lesson [here](https://github.com/arilamstein/streamlit_tutorial/blob/main/emails/day-3.md).