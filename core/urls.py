from api.v1.controllers import heave_calculation, request_count, index, reset_counter

router = {
    "/": index,
    "/v1/api/": heave_calculation,
    "/health/": request_count,
    "/reset_counter/": reset_counter,
}
