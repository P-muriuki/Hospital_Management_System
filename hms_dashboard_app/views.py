from django.shortcuts import render
# import plotly.express as px
# import pandas as pd

# # Create your views here.
# def patient_visualization(request):
#     data = {    "1": {
#         "Name(First and Last Name)": "john doe",
#         "Gender": "male",
#         "YearofBirth(DD-MM-YYYY)": "01-01-1990",
#         "Age": 34,
#         "Location": "nairobi",
#         "Previous Appointment": "30-10-2024",
#         "Next Appointment": "30-11-2024",
#         "Blood Pressure 1": 130,
#         "Blood Pressure 2": 110,
#         "Blood Pressure 3": 125,
#         "Blood Pressure 4": 140,
#         "Blood Pressure 5": 135
#     }}
#     df = pd.DataFrame(data)
    
#     fig = px.bar(df, x='Name', y='Age', color='Diagnosis')
#     graph = fig.to_html(full_html=False)

#     return render(request, 'visualizations/patient_visualization.html', {'graph': graph})
