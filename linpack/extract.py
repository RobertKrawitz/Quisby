import csv

from pricing import cloud_pricing
from config.config import cloud_type, region


def extract_linpack_summary_data(path, system_name):
    """
    Make shift function to handle linpack summary data 
    till a resolution is reached
    """

    results = []

    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=':')

        for row in csv_reader:
            gflops = row['MB/sec']

    if gflops:
        get_cloud_pricing = getattr(
            cloud_pricing, 'get_%s_pricing' % cloud_type.lower())
        price_per_hour = get_cloud_pricing(system_name, region)

        results.append(system_name)
        results.append(gflops)
        results.append(1)
        results.append(price_per_hour)
        results.append(float(gflops)/float(price_per_hour))

        return [results]
