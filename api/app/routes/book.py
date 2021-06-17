from fastapi import APIRouter, Depends, HTTPException, Path, status

from api.app.background_task import BackgroundTask
from api.app.schemas import DefaultResponse
from api.app.schemas.book import BookOutputSchema, BookSchema
from api.app.services.fake_api import FakeAPI
from api.app.crud.book import BookDAO

router = APIRouter()


@router.get("/", response_model=DefaultResponse)
async def run_queue(
    fake_api: FakeAPI = Depends(),
    background_task: BackgroundTask = Depends(),
):
    job = background_task.run_in_queue(fake_api.get_books)
    return {"data": {"job_id": job.id, "status": job.get_status()}}


@router.get("/job_status/{job_id}", response_model=DefaultResponse)
async def get_job_status(
    job_id: str = Path(...),
    background_task: BackgroundTask = Depends(),
):
    job = background_task.get_job_by_id(job_id)
    if job:
        return {"data": {"status": job.get_status()}}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")


@router.get("/result/{job_id}", response_model=BookOutputSchema)
async def get_books_from_queue(
    job_id: str = Path(...),
    background_task: BackgroundTask = Depends(),
    book_dao: BookDAO = Depends()
):
    job = background_task.get_job_by_id(job_id)
    if job:
        if job.result:
            books = [BookSchema(**book) for book in job.result]
            book_dao.create_all(books)
            book_dao.commit()
            return {"data": books, "count": len(job.result)}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
