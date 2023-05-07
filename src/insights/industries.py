from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path) as file:
        content = csv.DictReader(file)
        list = [data for data in content]

        list_industries_types = [industry['industry']
                                 for industry in list]

    list_industries_unic_types = [industrie
                                  for industrie
                                  in list_industries_types
                                  if industrie != '']

    return set(list_industries_unic_types)

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job['industry'] == industry]

    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
