-----
***A hands-on guide to help decision makers understand technology for modern data-driven services. It is designed for non-technical audiences with support from a trainer to prepare user devices.***

## What is a "Feature Store"? (And Why Should You Care?)

**Estimated Time:** 35-50 minutes (20 mins for setup, 20 mins for the experiment)

Imagine you're rolling out a new NHS app. This app looks at a patient's data (age, BMI, blood pressure) and gives them a real-time diabetes risk score.

You have two teams:

1.  **Your Data Scientists:** They study *months* of historical data from *all* patients to build a "risk-spotting brain" (a machine learning model).
2.  **Your App Developers:** They build the phone app that a GP or patient uses. It needs to get a risk score for *one* patient, right *now*.

Here's the million-pound question: How do you guarantee that the way the app calculates a patient's "BMI" *in real-time* is **exactly** the same way the scientists calculated "BMI" when they were training the "brain"?

If they are different (even slightly), the risk score could be wrong. This is a common and dangerous problem.

A **Feature Store** solves this.

Think of it as a **Central Kitchen** for your hospital's data.

  * The kitchen prepares all the "data ingredients" (like BMI, Age, Glucose) according to a single, standard recipe.
  * It stores *all* historical ingredients in a giant **"Offline Freezer"** (the Offline Store) for your data scientists to study and find new patterns.
  * It keeps a small, fresh batch of the *latest* ingredients on a **"Online Hot Counter"** (the Online Store) for the app to grab instantly.

This tutorial lets you run a mini-hospital system on your own computer. You'll act as a GP, a data engineer, and a data scientist to see *why* this "central kitchen" approach is so important.

-----

## Before We Begin: Your Tools 🛠️

**Time:** \~5 minutes (reading)

In this tutorial, you'll be installing the demo software yourself. Don't worry, it's just a few copy-and-paste steps\! The goal is for you to get a hands-on feel for how these systems are pieced together.

To make things easy, a helper has already prepared the computer you're using with all the basic building blocks. We'll be using a few key tools:

1.  **The Command Line (or "Terminal"):** This is the black text-based window you'll open (usually by searching for "Terminal" or "Command Prompt"). Think of it as the computer's "engine room." While your normal desktop (with icons and a mouse) is the friendly "front-of-house," the command line is where you give direct, powerful text commands to the computer's core. We'll give you the exact commands to copy and paste.

2.  **GitHub:** This is where the project's blueprints (the code) are stored. Think of it as a "Google Docs for code." It's a website that lets teams all over the world store, share, and collaborate on their software projects. Our first command will copy the project from GitHub onto your computer.

3.  **Python:** This is the programming language used to build the demo. Python is incredibly popular because its "grammar" (or syntax) is famously readable and clean, almost like writing in English. This makes it a top choice for everyone from app developers to data scientists.

4.  **`pip` (Pip Installs Packages):** This is Python's "app store." It's a tool that automatically finds and installs the specific "toolkits" (or packages) our project needs, like the `Flask` web server and the `Feast` feature store.

With that, let's get building\!

-----

## Part 1: Setting Up Your Mini-Hospital 🏥

**Time:** \~10-15 minutes

First, we need to get the "hospital software" (the demo project) running on your computer. This involves opening your computer's "Terminal" or "Command Prompt."

Don't worry about what these commands mean. They are just the one-time setup steps to install the project.

### Step 1. Get the Project Files

You'll need to download the project's folder from its storage site, GitHub.

1.  Open your Terminal (or Command Prompt).
2.  Copy and paste the following command to download the code, then press Enter:
    ```bash
    git clone https://github.com/regulate-tech/nhstech.git
    ```
3.  Now, move into the correct project folder by pasting this command and pressing Enter:
    ```bash
    cd nhstech/demo-feature-store
    ```

### Step 2. Create a "Clean Room" for the Project

This next command creates a separate, clean toolbox just for this project, so it doesn't interfere with any other software on your computer.

```bash
python -m venv .venv
```

### Step 3. Activate the "Clean Room"

Now, you "step into" that clean room.

  * **On Windows:**
    ```bash
    .venv\Scripts\activate
    ```
  * **On macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

You'll know it worked because you'll see `(.venv)` appear next to your terminal prompt.

### Step 4. Install the Tools

With your clean room active, you can install the "tools" this project needs (the web server, the 'AI brain' maker, etc.).

```bash
pip install feast pandas faker scikit-learn flask joblib
```

### Step 5. Generate Your First Patients

This command creates your first 500 synthetic patients and saves them to your "Offline Freezer" (a file called `patient_gp_data.parquet`) and "Online Hot Counter" (a file called `online_store.db`).

```bash
python generate_data.py
```

### Step 6. Train Your First "Risk Brain" 🧠

Now that you have data, this command tells your "data scientist" to study all 500 patients and create the first "brain" (the model) for spotting diabetes risk.

```bash
python train_model.py
```

### Step 7. Open the "GP's Computer"

You're all set\! This final command starts the simple website.

```bash
python app.py
```

Now, open your web browser (like Chrome or Edge) and go to this address: **`http://127.0.0.1:5000`**

You should see the "NHS Diabetes Risk Calculator" web page.

-----

## Part 2: The "What If" Experiment 🔬

**Time:** \~15-20 minutes

This is where you'll see the Feature Store in action. Let's run an experiment. We'll see how predictions can change for the *same patient*.

### Step 1. Get a Baseline

You're looking at the "GP View."

1.  In the "Patient ID" box, type in **10** and click **Calculate Risk**.
2.  You'll see a result, something like: **Patient 10 has a 28.5% (MEDIUM RISK) chance of diabetes.**
3.  Note down the Patient's features (their BMI, Age, etc.) and their risk score.

This score is based on two things: Patient 10's data and the "Risk Brain" (model) we trained on the *first 500 patients*.

### Step 2. Add New National Data

Now, let's simulate new data arriving in the health system from across the country.

1.  At the top of the page, click the **"Add 500 New Patients"** button.
2.  After the page reloads, click it **one more time**.

You have just added **1,000 new patients** to the "Offline Freezer" (the main database). The "Online Hot Counter" has also been updated with this new data.

### Step 3. See Patient 10 Again (The "Aha\!" Moment)

Let's check on Patient 10 again.

1.  In the "Patient ID" box, type **10** and click **Calculate Risk**.
2.  You will see the **exact same risk score** as before (e.g., **28.5% - MEDIUM RISK**).

**Why?**
This is the key insight. Their personal data hasn't changed, which is good. But more importantly, the app is still using the **old "Risk Brain"**\!

Even though our hospital system *has* 1,000 new patients' worth of data, our "Data Science" team hasn't published an updated "brain" yet. The app is separate from the model.

### Step 4. Retrain the "Risk Brain"

Now, let's play the role of the Data Scientist.

1.  Click the **"Retrain Risk Model"** button.
2.  This tells the system: "Go to the **Offline Freezer**, study *all* 1,500 patients (the original 500 + the new 1,000), and create a *new, smarter Risk Brain* based on this much larger dataset."
3.  The app will automatically load this new "brain" into memory.

### Step 5. See the Change

Let's test our patient one last time.

1.  In the "Patient ID" box, type **10** and click **Calculate Risk**.
2.  You will now see a **different risk score\!** (e.g., **30.1% - MEDIUM RISK**).

**Why?**
Patient 10's personal data is *identical*. But the "brain" (the model) has been updated. It now has a more refined, more accurate understanding of risk because it learned from 1,500 patients instead of just 500.

This is the power of a Feature Store. The app never went offline. The GP didn't have to do anything. The "Central Kitchen" (Feature Store) ensured that the *new* model was available, and the app *instantly* started using it, providing a more accurate prediction based on the latest national data.

-----

## What You've Learned 🎓

You just experienced the core principle of modern data systems (often called "MLOps"):

  * **The Problem:** In old systems, data scientists and real-time apps often use different data sources, leading to incorrect or stale predictions.
  * **The Solution:** A **Feature Store** acts as a "single source of truth" or "central kitchen."
      * The **Offline Store** ("freezer") collects all historical data for scientists to train big, new models.
      * The **Online Store** ("hot counter") provides the *latest* data for the live app to make instant predictions.
  * **The Benefit:** You can update your service's "intelligence" (the model) based on new data *without ever taking the app offline* or re-programming it. This makes your public services smarter, safer, and faster to improve.

-----

## Learn More (Drilling Down)

If you're curious, here are a few resources to explore these concepts further.

  * **What is a Feature Store?:** [A technical blog post describing what goes into a feature store" idea](https://www.tecton.ai/what-is-a-feature-store/).
  * **What is MLOps?:** [An explainer from IBM of the ideas behind managing the full lifecycle of AI models](https://www.ibm.com/think/topics/mlops).
  * **Feast (The Tool Used in this Demo):** [The official website for the open-source Feature Store technology used in this tutorial](https://feast.dev/).