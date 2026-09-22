from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    errors = []

    for error in exc.errors():

        location = error["loc"]

        field = location[-1]

        error_in = location[0]

        value = error.get("input")

        message = error["msg"]

        errors.append({
            "field": str(field),
            "error_in": str(error_in),
            "message": message,
            "input": value,
            "reason": (
                f"'{field}' field me error hai: "
                f"{message}"
            )
        })

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Validation error",
            "total_errors": len(errors),
            "errors": errors
        }
    )