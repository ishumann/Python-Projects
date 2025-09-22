from fastapi import FastAPI, Path, Query, HTTPException
import json
app = FastAPI()


def load_data():
    with open("C:\\Github\\Python-Projects\\fastapi_practice\\patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def hello_world():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "This is the about page."}

@app.get("/view")
def view():
    return load_data()


@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"), order: str = Query("asc", description="Order can be asc or desc")):
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid sort field. Must be one of {valid_fields}"
        )
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")

    data = load_data()
    sorted_data = sorted(
        data.values(), key=lambda x: x[sort_by], reverse=False if order == "desc" else True
    )
    return sorted_data
