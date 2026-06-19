class MetricsMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        self.r2xx = 0
        self.r4xx = 0
        self.r5xx = 0
        self.total = 0
        self.since_last = 0
    
    def __call__(self, request):
        response = self.get_response(request)
        code = response.status_code
        if code >= 200 and code < 300:
            self.r2xx += 1
        if code >= 400 and code < 500:
            self.r4xx += 1
        if code >= 500 and code < 600:
            self.r5xx += 1
        self.total += 1
        self.since_last += 1
        if self.since_last >= 5:
            print("---LOGG---")
            print(f"2XX: {self.r2xx}, 4XX: {self.r4xx}, 5XX:{self.r5xx}, всего: {self.total}")
            self.since_last = 0
        return response
