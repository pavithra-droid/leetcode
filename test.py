from datetime import date, timedelta
 
 
class Employment:
    def __init__(self, start_date: date, end_date: date | None):
        """
        Parameters
        ----------
        start_date
            The date the employment started.
        end_date
            The date the employment ended (set to None if the employment is still active).
        """
        self.start_date = start_date
        self.end_date = end_date
 
 
class EmploymentHistory:
    def __init__(self, employments: list[Employment]):
        self.employments = employments
 
    @property
    def is_empty(self) -> bool:
        """Return True if the employment history is empty, False otherwise."""
        if not self.employments:
            return True
        return False
 
    @property
    def current(self) -> list[Employment]:
        """Return a list of ongoing employments."""
        ...
        ongoing_employments = []
        for employment in self.employments:
            if not employment.end_date:
                ongoing_employments.append(employment)
 
    @property
    def earliest(self) -> Employment:
        """Returns the employment started the earliest."""
        ...
        if not self.employments:
            raise ValueError("Employment list is empty")
        data = sorted(self.employments, key=lambda x:x.start_date)
        return data[0]
        

    @property
    def total_time_employed(self) -> timedelta:
        """
        Returns the total amount of time spent employed.
        If working multiple jobs concurrently, they should not be double counted.
        """
        if not self.employments:
            return timedelta()

        data = sorted(self.employments, key=lambda x:x.start_date)
        total = timedelta()
        last_seen_end_date = None

        for employment in data:
            start_date = employment.start_date
            end_date = employment.end_date if employment.end_date else date.today()

            if last_seen_end_date is None:
                effective_start_date = start_date
            else:
                effective_start_date = max(start_date, last_seen_end_date)

            if end_date > effective_start_date:
                total += end_date - effective_start_date
            if last_seen_end_date is None or end_date > last_seen_end_date:
                last_seen_end_date = end_date
        return total

employments = [    
    Employment(start_date=date(2020, 1, 1), end_date=date(2020, 12, 30)),    
    Employment(start_date=date(2020, 7, 1), end_date=date(2020, 12, 31)),    
    Employment(start_date=date(2020, 8, 1), end_date=date(2020, 12, 31)),    
    Employment(start_date=date(2020, 9, 1), end_date=date(2020, 12, 31)),    
    Employment(start_date=date(2020, 10, 1), end_date=date(2020, 12, 31)),
    ]

employment_hist = EmploymentHistory(employments=employments)
print(employment_hist.total_time_employed)
 
# A quick summary of the behaviour of timedelta:
# d1 = date(2021, 4, 23)
# d2 = date(2023, 5, 21)
#
# td1 = d2-d1
# td2 = td1 + timedelta(days=5)
# assert td1 == timedelta(days=758)
# assert td2 == timedelta(days=763)
 