__author__ = 'Jacob'

import sys
import os

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(this_file))))
sys.path.insert(0, directory)

from ODM2 import serviceBase
import ODM2.SamplingFeatures.model as m
import ODM2.Core.model as  m_core


class readSamplingFeatures(serviceBase):
    """Queries to tables contained in the SamplingFeature """

    """
    Site
    """

    def getAllSites(self):
        """Select all on Sites

        :return Site Objects:
            :type list:
        """
        return self._session.query(m.Site).all()

    def getSiteBySFId(self, siteId):
        """Select by siteId

        :param siteId:
            :type Integer:
        :return Return matching Site Object filtered by siteId:
            :type Site:
        """
        try:
            return self._session.query(m.Site).filter_by(SamplingFeatureID=siteId).one()
        except:
            return None


    def getSiteBySFCode(self, siteCode):
        """Select by siteCode

        :param siteCode:
            :type String:
        :return Return matching Samplingfeature Object filtered by siteCode:
            :type Samplingfeature:
        """

        sf= self._session.query(m_core.Samplingfeature).filter_by(SamplingFeatureCode = siteCode).one()
        return self._session.query(m.Site).filter_by(SamplingFeatureID = sf.SamplingFeatureID).one()