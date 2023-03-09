from api.v1.controllers import heave_calculation, request_count

router = {
    "/v1/api/": heave_calculation,
    "/health/": request_count,
}
