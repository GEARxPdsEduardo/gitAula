from fastapi import FastAPI

# Importando as rotas de autenticação
from modules.auth_module.routes import router as auth_router

def create_app():
    app = FastAPI()
    configure_routing(app)
    return app

def configure_routing(app: FastAPI):
    app.include_router(auth_router, prefix="/auth", tags=["auth"])

app = create_app()

@app.get("/")
def read_root():
    return {"Hello": "World"}