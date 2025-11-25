<h1>Synthetic Data Generation using Python</h1>
<p>A curated collection of synthetic datasets created for learning, experimentation, and concept exploration across healthcare analytics, time-series modelling, signal processing, and text classification. This repository provides a safe environment to practice workflows such as EDA, statistical modelling, Fourier analysis, and basic machine learning without relying on sensitive real-world data.</p>

<h2>📘 Module Descriptions</h2>

<h3>1. healthcare.py</h3>
Generates a clinical-trial-style dataset for 200 patients containing variables such as:
age, blood_pressure, cholesterol, treatment_group, recovery_time, survival_time, and event_observed.
Enables exploration of:
<ul>
<li>Hypothesis testing
<li>Correlation and regression analysis
<li>Survival analysis techniques
</ul>

<h3>2. cardio.py</h3>
Creates a cardiovascular dataset combining demographic, clinical, and lifestyle indicators.
Each entry includes a computed:
<ul>
<li>Risk score
<li>Heart disease probability
</ul>
Suitable for:
<ul>
<li>EDA
<li>Risk stratification
<li>Feature engineering practice
</ul>

<h3>3. health_time_series.py</h3>
Produces 365-day time-series for:
<ul>
<li>Glucose
<li>Systolic blood pressure
<li>Cholesterol
</ul>
Designed for hands-on experimentation with:
<ul>
<li>Time-series decomposition
<li>ARIMA and forecasting models
<li>Trend and seasonality analysis
</ul>

<h3>4. signal_synthetic.py</h3>
Generates a composite signal with 5 Hz and 20 Hz components.
Allows exploration of:
<ul>
<li>Fourier Transform
<li>Frequency-domain analysis
<li>Signal denoising and filtering
</ul>

<h3>5. earthquake.py</h3>
Simulates vibration data from a 10-story building during an earthquake.
Useful for studying:
<ul>
<li>Structural dynamics
<li>Natural frequencies & resonance
<li>Structural health monitoring concepts
</ul>

<h3>6. EEG.py</h3>
Synthesizes EEG-like signals inspired by common brainwave frequency bands.
Supports learning around:
<ul>
<li>EEG signal characteristics
<li>Frequency band extraction
<li>Neurological signal interpretation
</ul>

<h3>7. Email.py</h3>
Provides a labelled mix of synthetic spam and non-spam emails.
Ideal for building and testing:
<ul>
<li>Text preprocessing pipelines
<li>Classical ML models (e.g., MLPClassifier)
<li>Baseline spam classification workflows
</ul>

<h2>📎 Notes & Intended Use</h2>
<ol>
<li>These datasets are purely synthetic.
<li>They are designed for learning, experimentation, and prototyping.
<li>They should not be used for real-world clinical or production modelling.
<li>The focus is on understanding analytical workflows and modelling concepts across diverse data types.
</ol>

<h2>🚀 Getting Started</h2>
<h4>Clone the repository</h4>
git clone https://github.com/shivambhatnagar66/Synthetic_Data_generation.git
<h4>Install required libraries</h4>
pip install numpy pandas matplotlib scipy scikit-learn
<h4>Run any module</h4>
python healthcare.py

<h4>🤝 Contributions</h4>
Suggestions and contributions are welcome. Feel free to open an issue or submit a pull request.