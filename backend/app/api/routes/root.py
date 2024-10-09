from fastapi import APIRouter, Body

router = APIRouter()


@router.post("/")
def root(arg: str = Body(embed=True)):
    return {"message": f"It root page. Your message {arg}"}


@router.get("/")
def root_get():
    return {"message": "It root page."}
