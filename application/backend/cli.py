import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", app_dir="app")
