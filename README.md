# Interview Dashboard

A local Streamlit app for reviewing interview candidates from an Excel workbook. Search by name, review application responses, record interview status and notes, and download an updated copy.

## Technologies

Python, Streamlit, pandas and openpyxl.

## Run locally

```sh
git clone https://github.com/tanish1112/interview-dashboard.git
cd interview-dashboard
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On Windows PowerShell, activate the environment with `.\.venv\Scripts\Activate.ps1`. Open [localhost:8501](http://localhost:8501).

## Workbook format

Upload an `.xlsx` file with the following column headers. Use one row per candidate and unique, non-empty names.

| Required column | Contents |
| --- | --- |
| `Name` | Candidate name |
| `Vertical(s) Preferences (Any 3)` | Team or area preferences |
| `Why do you wish to join us?` | Application motivation |
| `Mention your past experiences.` | Experience summary |

The app adds `Interview Done` and `Notes` if they are missing. Choose a candidate, edit the fields, then download `updated_interview_list.xlsx` before switching candidates. Use the latest download as the input for the next round of edits because the app reloads the uploaded workbook on interaction.
