#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file MorphologicalAnalysis.py
 @brief MorphologicalAnalysis
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import MeCab

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
morphologicalanalysis_spec = ["implementation_id", "MorphologicalAnalysis",
		 "type_name",         "MorphologicalAnalysis",
		 "description",       "MorphologicalAnalysis",
		 "version",           "1.0.0",
		 "vendor",            "hiroyasu_tsuji",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class MorphologicalAnalysis
# @brief MorphologicalAnalysis
#
#
class MorphologicalAnalysis(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_xmldata = RTC.TimedString(RTC.Time(0,0),"")
		"""
		"""
		self._xmldataIn = OpenRTM_aist.InPort("xmldata", self._d_xmldata)
		self._d_strdata = RTC.TimedString(RTC.Time(0,0),"")
		"""
		"""
		self._strdataIn = OpenRTM_aist.InPort("strdata", self._d_strdata)
		self._d_wakati = RTC.TimedStringSeq(RTC.Time(0,0),"")
		"""
		"""
		self._wakatiOut = OpenRTM_aist.OutPort("wakati", self._d_wakati)
		self._d_chasen = RTC.TimedStringSeq(RTC.Time(0,0),"")
		"""
		"""
		self._chasenOut = OpenRTM_aist.OutPort("chasen", self._d_chasen)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable

		# Set InPort buffers
		self.addInPort("xmldata",self._xmldataIn)
		self.addInPort("strdata",self._strdataIn)

		# Set OutPort buffers
		self.addOutPort("wakati",self._wakatiOut)
		self.addOutPort("chasen",self._chasenOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The deactivated action (Active state exit action)
	# former rtc_active_exit()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
                while self._xmldataIn.isNew():
                        data = self._xmldataIn.read()
                        data.data = data.data.decode('utf-8')
                        speechdata = BeautifulSoup(data.data,"lxml")
                        totaldata = []
                        
                        for data.data in speechdata.findAll('data'):
                                rank = int(data.data['rank'])
                                score = float(data.data['score'])
                                text = data.data['text']
                                xmldata = XMLSet(rank, score, text.encode("utf-8"))
                                totaldata.append(xmldata)
                                
                        totalxmldata = sorted(totaldata, key=lambda x: x[1], reverse=True)
                        print str(totalxmldata).decode('string-escape')
                        highxmldata = totalxmldata[0]
                        print (highxmldata[2])
                        
                        intextdata = highxmldata[2]

                        taggerwakati = MeCab.Tagger("-Owakati")
                        data_wakati = taggerwakati.parse(intextdata)
                        list_wakati = data_wakati.split(' ')
                        print str(list_wakati).decode('string-escape')
                        self._d_wakati.data = list_wakati
                        self._wakatiOut.write()
                
                        taggerchasen = MeCab.Tagger("-Ochasen")
                        taggerchasen.parse('')
                        node = taggerchasen.parseToNode(intextdata)
                        chasendata = []
                        while node:
                                resorg = node.feature.split(",")[6]
                                ps =node.feature.split(",")[0]
                                if ps == "名詞":
                                        chasendata.append(resorg)
                                if ps == "動詞":
                                        chasendata.append(resorg)
                                if ps == "形容詞":
                                        chasendata.append(resorg)
                                if ps == "副詞":
                                        chasendata.append(resorg)
                                if ps == "助詞":
                                        chasendata.append(resorg)
                                if ps == "接続詞":
                                        chasendata.append(resorg)
                                if ps == "助動詞":
                                        chasendata.append(resorg)
                                if ps == "連体詞":
                                        chasendata.append(resorg)
                                if ps == "感動詞":
                                        chasendata.append(resorg)
                                node = node.next
                        chasendata.append("\n")
                        
                        print str(chasendata).decode('string-escape')
                        self._d_chasen.data = chasendata
                        self._chasenOut.write()
                
                while self._strdataIn.isNew():
                        
                        intext = self._strdataIn.read()
                        intextdata = intext.data

                        taggerwakati = MeCab.Tagger("-Owakati")
                        data_wakati = taggerwakati.parse(intextdata)
                        list_wakati = data_wakati.split(' ')
                        print str(list_wakati).decode('string-escape')
                        self._d_wakati.data = list_wakati
                        self._wakatiOut.write()
                
                        taggerchasen = MeCab.Tagger("-Ochasen")
                        taggerchasen.parse('')
                        node = taggerchasen.parseToNode(intextdata)
                        chasendata = []
                        while node:
                                resorg = node.feature.split(",")[6]
                                ps =node.feature.split(",")[0]
                                if ps == "名詞":
                                        chasendata.append(resorg)
                                if ps == "動詞":
                                        chasendata.append(resorg)
                                if ps == "形容詞":
                                        chasendata.append(resorg)
                                if ps == "副詞":
                                        chasendata.append(resorg)
                                if ps == "助詞":
                                        chasendata.append(resorg)
                                if ps == "接続詞":
                                        chasendata.append(resorg)
                                if ps == "助動詞":
                                        chasendata.append(resorg)
                                if ps == "連体詞":
                                        chasendata.append(resorg)
                                if ps == "感動詞":
                                        chasendata.append(resorg)
                                node = node.next
                        chasendata.append("\n")
                        
                        print str(chasendata).decode('string-escape')
                        self._d_chasen.data = chasendata
                        self._chasenOut.write()
	                
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def MorphologicalAnalysisInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=morphologicalanalysis_spec)
    manager.registerFactory(profile,
                            MorphologicalAnalysis,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MorphologicalAnalysisInit(manager)

    # Create a component
    comp = manager.createComponent("MorphologicalAnalysis")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

