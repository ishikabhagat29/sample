from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/data/", response_class=FileResponse)
async def read_data():
    file_path = "C:\Users\ishikapradeep.bhagat\Desktop\Project\scripts\energy_parameters.csv"
    response = FileResponse(file_path, media_type="file/csv")
    response.headers["Content-Disposition"] = "attachment; filename=downloaded_file.csv"
    return response