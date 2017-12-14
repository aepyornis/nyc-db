from .transform import with_geo, with_bbl, to_csv, extract_csvs_from_zip
from .dof_parser import parse_dof_file


def pluto_16v2(dataset):
    return with_geo(to_csv(extract_csvs_from_zip(dataset.files[0].dest)))


def hpd_complaints(dataset):
    return with_bbl(to_csv(dataset.files[0].dest))


def dob_complaints(dataset):
    return to_csv(dataset.files[0].dest)


def hpd_violations(dataset):
    return to_csv(dataset.files[0].dest)


def hpd_registrations(dataset):
    return to_csv(dataset.files[0].dest)


def hpd_contacts(dataset):
    return to_csv(dataset.files[1].dest)


def dof_sales(dataset):
    for f in dataset.files:
        for row in with_bbl(parse_dof_file(f.dest)):
            yield row


def dobjobs(dataset):
    return with_bbl(to_csv(dataset.files[0].dest))


def rentstab(dataset):
    return to_csv(dataset.files[0].dest)


def acris(dataset, table_name):
    dest_file = next(filter(lambda f: table_name in f.dest, dataset.files))
    return to_csv(dest_file.dest)
