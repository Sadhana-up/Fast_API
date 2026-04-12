from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Middleware and CORS Demo")


app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"http://localhost",
		"http://localhost:3000",
		"http://127.0.0.1:3000",
	],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
	start_time = perf_counter()
	response = await call_next(request)
	process_time = perf_counter() - start_time

	response.headers["X-Process-Time"] = f"{process_time:.6f}"
	response.headers["X-Request-Path"] = request.url.path
	return response


@app.get("/")
async def root():
	return {"message": "Middleware and CORS are configured"}


@app.get("/health")
async def health():
	return {"status": "ok"}
