""" Convert Civil War Soldiers and Sailors XML file to csv tables """
from lxml import etree as ET
import re
import csv

namespaces = {
'd' : "http://schemas.microsoft.com/ado/2007/08/dataservices",
'm' :"http://schemas.microsoft.com/ado/2007/08/dataservices/metadata",
'': "http://www.w3.org/2005/Atom"
}

def xmlns(x):
    xsplit = x.split(':')
    if len(xsplit) == 1:
        xsplit = ['', xsplit[0]]
    return "{%s}%s" % (namespaces[xsplit[0]], xsplit[1])


def battle_csv(root, dst):
    fields = (
    'BattlefieldCode',
    'BattleName',
    'BattleType',
    'CampaignCode',
    #'CampaignDates',
    #'CampaignName',
    'Comment',
    'EndDate',
    'ID',
    'Result',
    'ShortSummary',
    'ShortSummarySource',
    'State',
    'Summary',
    'SummarySource',
    'TheaterCode',
    # 'TheaterName',
    'TotalCasualties'
    )
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            battle = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in fields:
                battle[fld] = properties.find(xmlns('d:%s' % fld)).text
            writer.writerow(battle)
            
def theaters_csv(root, dst):
    theaters = {}
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, ('TheaterCode', 'TheaterName'))
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            theater_code = properties.find(xmlns('d:TheaterCode')).text
            theater_name = properties.find(xmlns('d:TheaterName')).text
            if theater_code:
                theaters[theater_code] = theater_name
        theaters_rows = [{'TheaterCode': k, 'TheaterName': v} for k, v in theaters.items()]
        writer.writerows(theaters_rows)
        
def campaigns_csv(root, dst):
    campaigns = {}
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, ('CampaignCode', 'CampaignName', 'CampaignDates', 'TheaterCode'))
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            campaign_code = properties.find(xmlns('d:CampaignCode')).text
            campaign_name = properties.find(xmlns('d:CampaignName')).text
            campaign_dates = properties.find(xmlns('d:CampaignDates')).text
            theater_code = properties.find(xmlns('d:TheaterCode')).text
            if campaign_code and campaign_code.strip() != '' and campaign_code not in campaigns:
                campaigns[campaign_code] = {'CampaignCode': campaign_code,
                                            'CampaignName': campaign_name,
                                            'CampaignDates': campaign_dates,
                                            'TheaterCode': theater_code}
        for k, v in campaigns.items():
            writer.writerow(v) 

def guid_clean(x):
    return x.lower().replace("{", "").replace("}", "")
           
def commander_csv(root, dst):
    fields = ('BattlefieldCode', 'combatant', 'commander_number', 'commander', 'rank')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for entry in root.findall('.//%s' % xmlns('entry')):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            battlecode = properties.find(xmlns("d:BattlefieldCode")).text
            enemy = properties.find(xmlns("d:EnemyName")).text
            for i, ordinal in enumerate(("First", "Second", "Third")):
                if properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text is not None:
                    if re.search("\\S", properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text):
                        writer.writerow({'BattlefieldCode' : battlecode,
                                         'combatant' : enemy,
                                         'commander_number' : i + 1,
                                         'commander' : guid_clean(properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text),
                                         'rank' : properties.find(xmlns("d:%sEnemyCommanderRank" % ordinal)).text
                                         })
                if properties.find(xmlns("d:%sUSCommander" % ordinal)).text is not None:
                    if re.search("\\S", properties.find(xmlns("d:%sUSCommander" % ordinal)).text):
                        writer.writerow({'BattlefieldCode' : battlecode,
                                         'combatant' : "US",
                                         'commander_number' : i + 1,  
                                         'commander' : guid_clean(properties.find(xmlns("d:%sUSCommander" % ordinal)).text),
                                         'rank' : properties.find(xmlns("d:%sUSCommanderRank" % ordinal)).text
                                         })
                                        
def forces_csv(root, dst):
    fields = ('BattlefieldCode', 'combatant', 'TroopsEngaged', "Casualties")
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for entry in root.findall('.//%s' % xmlns('entry')):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            battlecode = properties.find(xmlns("d:BattlefieldCode")).text
            enemy = properties.find(xmlns("d:EnemyName")).text
            writer.writerow({'BattlefieldCode' : battlecode,
                             'combatant' : enemy,
                             'TroopsEngaged': properties.find(xmlns("d:EnemyTroopsEngaged")).text,
                             'Casualties': properties.find(xmlns("d:EnemyCasualties")).text,
                           })
            writer.writerow({'BattlefieldCode' : battlecode,
                            'combatant' : "US",
                             'TroopsEngaged': properties.find(xmlns("d:USTroopsEngaged")).text,
                             'Casualties': properties.find(xmlns("d:USCasualties")).text,
                          })
                          
def people_csv(root, dst):
    fields = ("PersonID", "ID", "LastName", "FirstName", "MiddleName", "MiddleInitial", "Keywords", "Rank", "Bio", "BioSource", "NarrativeLink1", "NarrativeLink2")
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            row = {}        
            for fld in fields:
                row[fld] = properties.find(xmlns('d:%s' % fld)).text
            writer.writerow(row)   
            
def battleunitslink_csv(root, dst):
    fields = (
    'BattlefieldCode',
    'Comment',
    'Source',
    'UnitCode'
    )
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):            
            row = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in fields:
                row[fld] = properties.find(xmlns('d:%s' % fld)).text
            row['BattlefieldCode'] = row['BattlefieldCode'].upper()
            writer.writerow(row)
            
def units_csv(root, dst):
    fields = (
    'ID',
    'UnitCode',
    'UnitName',
    )
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):           
            row = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in fields:
                row[fld] = properties.find(xmlns('d:%s' % fld)).text
            writer.writerow(row) 

def main():
    
    parser = ET.XMLParser(encoding = 'cp1252')

    with open('battle.xml', 'rb') as f:
        battles = ET.fromstring(f.read(), parser)    
    commander_csv(battles, "cwss_commanders.csv")
    battle_csv(battles, 'cwss_battles.csv')
    forces_csv(battles, 'cwss_forces.csv')
    theaters_csv(battles, 'cwss_theaters.csv')
    campaigns_csv(battles, 'cwss_campaigns.csv')

    with open('persons.xml', 'rb') as f:
            persons = ET.fromstring(f.read(), parser)  
    people_csv(persons, 'cwss_persons.csv')

    with open('battleunitlink.xml', 'rb') as f:
            battleunitlinks = ET.fromstring(f.read(), parser)  
    battleunitslink_csv(battleunitlinks, 'cwss_battleunitlinks.csv')

    with open('units.xml', 'rb') as f:
            battleunitlinks = ET.fromstring(f.read(), parser)  
    units_csv(battleunitlinks, 'cwss_units.csv')

if __name__ == "__main__":
    main()
