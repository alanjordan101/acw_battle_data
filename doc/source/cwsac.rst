CWSAC Battle Summaries
=======================

These data are from the `CWSAC Battle Summaries
<http://www.nps.gov/hps/abpp/battles/bystate.htm>`_.  The unstructured
webpages were cleaned and converted into the structured data in these
tables.

For more information on the CWSAC data see

- http://www.nps.gov/hps/abpp/battles/tvii.htm 
- http://www.nps.gov/hps/abpp/cwsac/cws0-1.html

Notes
---------

The various Battles of Fort Wagner, Fort Morris, and the Charleston
Harbor are particularly confusing and seem to overlap.  See
:doc:`./Charleston_Harbor_Battles` for more information.

A couple notes about the set of battles in these data. 

- In an update on the status of battlefields `Civil War Sites Advisory Commission Report Update & Resurvey <http://www.nps.gov/history/hps/abpp/CWSII/CWSII.htm>`_, 
  the following changes were made.
  
  - AR018,  Battle of Bayou Meto (Reed's Bridge) on Aug 27, 1863 (part of the Advance on Little Rock campaign) was added. See 
    `Civil War Battlefields in the State of Arkansas - Arkansas Post to Devils Backbone <http://www.nps.gov/history/hps/abpp/CWSII/ArkansasBattlefieldProfiles/Arkansas%20Post%20to%20Devils%20Backbone.pdf>`_.
  - SC007. Fort Wagner II. Dates changed to 7-18. `Report Update
    <http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.
  - SC008. Fort Sumter II. Dates changed to 8-17 to 9-8. `Report
    Update
    <http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.
  - SC009. Charleston Harbor. Dates changed to Aug 22-23, 1863 and
    Sept 5-8, 1863.  This really appears to be to engagements.  The
    assault on Fort Sumter is the only engagement referenced in the
    initial CWSAC report.  `Report Update
    <http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.
    
    - Aug 22-23, 1863 Bombardment of Charleston by the Swamp Angel
    - Sept 5-8, 1863. Assault on Fort Sumter.

  - VA020A and VA020B combined into a single battle, `Source
    <http://www.nps.gov/hps/abpp/CWSII/VirginiaBattlefieldProfiles/White%20oak%20Road%20to%20Wilderness.pdf>`_.

	 Although the CWSAC identified the engagements at White Oak
	 Swamp and Glendale as part of the same offensive, it mapped the
	 battlefields individually. Upon further study, the ABPP decided to
	 combine the two engagements under one Study Area.

CWSAC II 
=================

The Civil War Battlefield Preservation Act of 2002 directed the NPS to
update their 1993 battlefield surveys. The results of the resurvey are
available `here
<http://www.nps.gov/hps/abpp/CWSII/CWSIIStateReports.htm>`_.

- Battles Glendale (VA020A) and White Oak Swamp (VA020B) were combined
  into a single battle.

    Upon review of the histories of the battles, the ABPP has combined
    White Oak Swamp (VA020a) and Glendale (VA020b) into a single
    entry: the overall count is one battlefield fewer, but both
    engagement areas are included. `Update to the Civil War Sites
    Advisory Commission Report: Commonwealth of Virigina
    <http://www.nps.gov/hps/abpp/CWSII/CWSACReportVirginiaUpdate.pdf>`_
    (p. 8).
    
- The Battle of Bayou Meto (AR018) was added. However, it does not
  appear to have been added strictly due to historical judgment of
  importance.  No military significance or casualties is given for
  this battle.  

	The CWSAC did not list Bayou Meto (Reed’s Bridge) as one of
	the principal battles of the Civil War. In 2002, however, the
	battlefield was listed in the National Register of Historic
	Places as a nationally significant historic property. Given
	the high level of significance conferred by the NRHP listing,
	the ABPP decided, as part of the fieldwork undertaken for this
	update, to assess conditions at Bayou Meto.  ` Update to the
	Civil War Sites Advisory Commission Report: State of Arkansas
	<http://www.nps.gov/hps/abpp/CWSII/CWSACReportArkansasUpdate.pdf>`_ (p. 8)

- The Battle of Athens (AL002) is redefined from the battle on January 26, 1863
  to the battle on September 23-25, 1963. Because of this I give
  the new battle the code **AL009**.  I also think that the results in the document
  are referring to the January battle because the September battle is unambiguously
  a Confederate victory.
- new variables: Acreage of the battlefield area
- revised variables: forces, principal commanders, result, battle
  dates
- Indian forces. Oklahoma battles OK001 (Round Mountain), OK002
  (Chusto-Talasah), and OK003 (Chustenahlah) classify the Creek forces
  under Opothleyahola as [US] instead of [I].  In CWSAC II, the only
  battles involving purely American Indian forces are against the
  Union and generally part of the Sioux Wars (Minnesota, North Dakota,
  Idaho).  This seems reasonable, the Creek and Seminole forces in the
  Oklahoma battles seemed to genuinely be Union allies, while the
  Sioux Indian forces fighting the Union were not allied with the
  Confederacy.

    
cwsac_campaigns
------------------

.. include:: _tables/cwsac_campaigns.rst

List of the American Civil War campaigns and theaters.

cwsac_battles
------------------

.. include:: _tables/cwsac_battles.rst

Data on the time, location, outcome, and battle-level attributes of each battle.

cwsac_forces
-----------------

.. include:: _tables/cwsac_forces.rst

Data on the casualties and force sizes of the combatants in each battles.

cwsac_to_dbepdia
--------------------

.. include:: _tables/cwsac_to_dbpedia.rst

For the most part, each CWSAC battle page corresponds to a single Wikipedia page, 
making linking the two easy.

The one exception is that CWSAC considers the Battle of Chattanooga
(http://www.nps.gov/hps/abpp/battles/tn024.htm) from Nov 23-25, 1863 a
single battle. However, in Wikipedia this corresponds to two battles
in http://en.wikipedia.org/wiki/Chattanooga_Campaign:
http://en.wikipedia.org/wiki/Battle_of_Lookout_Mountain on Nov 24, and
the http://en.wikipedia.org/wiki/Battle_of_Missionary_Ridge on Nov 25.



