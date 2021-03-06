""" create csv tables from clodfelter.yaml """
import csv
import re

import yaml

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def rename(x, k, j):
    if k in x:
        x[j] = x[k]
        del x[k]

def battles(data, filename):
    with open(filename, 'w') as f:
        fieldnames = ('name', 'theater', 'start_date', 'end_date', 'page')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for theater, battles in data.items():
            for battle in battles:
                row = battle.copy()
                fields = ('name', 'p', 'start', 'end')
                row = dict_subset(row, fields)
                rename(row, 'p', 'page')
                rename(row, 'start', 'start_date')
                rename(row, 'end', 'start_date')
                if 'end_date' not in row:
                    row['end_date'] = row['start_date']
                row['theater'] = theater
                writer.writerow(row)

def forces(data, filename):
    fields = set()
    # for theater, battles in data.items():
    #     for battle in battles:
    #         for combatant in ('union', 'confed'):
    #             for k in battle[combatant].keys():
    #                 fields.add(k)
    # for x in fields:
    #     print("'%s'" % x + ',')
    fields = ('cavalry',
    'divisions',
    'casualties',
    'killed_missing',
    'guns',
    'killed',
    'warships and transports',
    'warships',
    'killed_wounded',
    'captured',
    'gunboats captured',
    'small arms lost',
    'steamers',
    'wounded',
    'brigades',
    'ironclads captured',
    'crewmen',
    'warships damaged',
    'cavalry divisions',
    'ironclads',
    'missing',
    'gunboats',
    'warships sunk',
    'guns lost',
    'strength',
    'corps',
    'companies',
    'forts captured',
    'note',
    'guns captured',
    'captured_missing',
    'cavalry corps',
    'sloops',
    'wounded_missing',
    'wooden warships',
    'iroclads sunk',
    'gunboats sunk',
    'infantry',
    'frigates',
    'small arms captured'
    )
    with open(filename, 'w') as f:
        fieldnames = ['battle', 'belligerent'] + list(fields)
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for theater, battles in data.items():
            for battle in battles:
                for combatant in ('union', 'confed'):
                    row = battle[combatant].copy()
                    row['battle'] = battle['name']
                    row['belligerent'] = combatant
                    rename(row, 'w', 'wounded')
                    rename(row, 'wm', 'wounded_missing')
                    rename(row, 'p', 'captured')
                    rename(row, 's', 'strength')
                    rename(row, 'c', 'casualties')
                    rename(row, 'cm', 'captured_missing')
                    rename(row, 'm', 'missing')
                    rename(row, 'k', 'killed')
                    rename(row, 'km', 'killed_missing')
                    rename(row, 'kw', 'killed_wounded')
                    writer.writerow(row)

def cwsac_links(data, filename):
    with open(filename, 'w') as f:
        fieldnames = ('battle', 'cwsac', 'relation')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for theater, battles in data.items():
            for battle in battles:
                if 'links' in battle:
                    links = battle['links']
                    for x in links:
                        if re.match("[A-Z]{2}[0-9]{3}", x[0]):
                            if len(x) == 1:
                                row = {'cwsac': x[0], 'relation': '='}
                            else:
                                row = {'cwsac': x[0], 'relation': x[1]}
                            row['battle'] = battle['name']
                            writer.writerow(row)
                else:
                    print(battle)

def dbpedia_links(data, filename):
    with open(filename, 'w') as f:
        fieldnames = ('battle', 'dbpedia', 'relation')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for theater, battles in data.items():
            for battle in battles:
                if 'links' in battle:
                    links = battle['links']
                    for x in links:
                        if re.search("wikipedia.org", x[0]):
                            x[0] = re.sub(r'https?://en\.wikipedia\.org/wiki', 
                                          r'http://dbpedia.org/resource', x[0])
                            if len(x) == 1:
                                row = {'dbpedia': x[0], 'relation': '='}
                            else:
                                row = {'dbpedia': x[0], 'relation': x[1]}
                            row['battle'] = battle['name']
                            writer.writerow(row)
                else:
                    print(battle)
                

SRC = 'clodfelter.yaml'
    
with open(SRC, 'r') as f:
    data = yaml.load(f)

battles(data, 'clodfelter_battles.csv')
forces(data, 'clodfelter_forces.csv')
cwsac_links(data, 'clodfelter_to_cwsac.csv')
dbpedia_links(data, 'clodfelter_to_dbpedia.csv')
