from typing import Union, List, Dict
import csv


def get_max_salary(path: str) -> int:
    with open(path) as file:
        content = csv.DictReader(file)
        list = [data for data in content]

        salaries = [salary['max_salary']
                    for salary
                    in list]

    list_digit = [int(salary)
                  for salary
                  in salaries
                  if salary.isdigit()]
    return max(list_digit)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    with open(path) as file:
        content = csv.DictReader(file)
        list = [data for data in content]

        salaries = [salary['min_salary']
                    for salary
                    in list]

    list_digit = [int(salary)
                  for salary
                  in salaries
                  if salary.isdigit()]
    return min(list_digit)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = abs(int(job['min_salary']))
        max_salary = abs(int(job['max_salary']))
        if max_salary < min_salary or not str(abs(int(salary))).isdecimal():
            raise ValueError()

        return min_salary <= int(salary) <= max_salary

    except (KeyError, ValueError, TypeError):
        raise ValueError()
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    return [job for job in jobs if is_salary_range_matched(job, salary)]


def is_salary_range_matched(job, salary):
    try:
        return matches_salary_range(job, salary)
    except ValueError:
        return False
#    return [job for job in jobs if matches_salary_range(job, salary)]

    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
