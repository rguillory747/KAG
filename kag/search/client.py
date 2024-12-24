# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

from kag.common.base.client import Client
from kag.common.rest import Configuration, ApiClient

from kag.search import rest, TextSearchRequest, VectorSearchRequest, IdxRecord


def idx_record_to_dict(record: IdxRecord):
    return {"score": record.score, "node": record.fields}


class SearchClient(Client):
    """ """

    def __init__(self, host_addr: str = None, project_id: int = None):
        super().__init__(host_addr, project_id)
        self._rest_client: rest.SearchApi = rest.SearchApi(
            api_client=ApiClient(configuration=Configuration(host=host_addr))
        )

    def search_text(self, query_string, label_constraints=None, topk=10, params=None):
        req = TextSearchRequest(
            self._project_id, query_string, label_constraints, topk, params
        )
        records = self._rest_client.search_text_post(text_search_request=req)
        return [idx_record_to_dict(record) for record in records]

    def search_vector(
        self, label, property_key, query_vector, topk=10, ef_search=None, params=None
    ):
        req = VectorSearchRequest(
            self._project_id, label, property_key, query_vector, ef_search, topk, params
        )
        records = self._rest_client.search_vector_post(vector_search_request=req)
        return [idx_record_to_dict(record) for record in records]


if __name__ == "__main__":
    sc = SearchClient("http://127.0.0.1:8887", 4)
    a = sc.search_text("Depressive_or_psychotic_symptoms")
    print(a)

    b = sc.search_vector(
        "Entity",
        "name",
        [
            -0.011183402,
            0.048467062,
            0.034121536,
            -0.012637187,
            -0.0063864742,
            -0.018192118,
            -0.005130675,
            0.0001195873,
            -0.050548747,
            0.0039880113,
            -0.00019851669,
            -0.021597484,
            0.072632715,
            -0.015092217,
            0.06702121,
            0.004932689,
            -0.021484349,
            -0.0026530172,
            0.016630854,
            0.018146865,
            0.018237373,
            -0.014526542,
            0.020669777,
            0.0030574752,
            -0.019221647,
            0.0034647614,
            0.033148576,
            0.061771747,
            -0.03303544,
            -0.016314076,
            0.025297001,
            0.015963357,
            0.009311016,
            -0.0052918927,
            -0.022242354,
            0.015578698,
            0.011652912,
            -0.013349937,
            0.030546468,
            0.057246342,
            -0.009090402,
            -0.018565465,
            -0.0309085,
            -0.04023083,
            0.03461933,
            -0.016913692,
            0.060640395,
            -0.012625873,
            0.043715388,
            -0.024731325,
            0.009678705,
            0.1618284,
            0.011992317,
            0.010945817,
            -0.022038711,
            -0.023894126,
            -0.0048025837,
            -0.01371197,
            -0.047697745,
            -0.005190071,
            -0.05122756,
            -0.0063864742,
            0.054576356,
            -0.060957175,
            0.010363172,
            -0.031247905,
            -0.011058953,
            -0.023758363,
            -0.030636976,
            -0.051996876,
            -0.023215316,
            0.0064260717,
            -0.032243494,
            -0.035275515,
            -0.0061488906,
            0.0029556535,
            0.006584461,
            0.042787682,
            -0.036836777,
            0.01242223,
            -0.007042658,
            0.04009507,
            -0.0143568395,
            -0.0052324967,
            -0.0010097305,
            -0.023894126,
            -0.010555502,
            -0.018655973,
            0.038058635,
            -0.054576356,
            -0.06602562,
            -0.005246639,
            -0.0036882032,
            -0.034822974,
            0.018622031,
            0.02393938,
            -0.022445997,
            -0.0119583765,
            0.0062789964,
            0.015080905,
            -0.07552897,
            0.0048110685,
            0.035252888,
            0.0027322117,
            0.10019241,
            0.020352999,
            0.028012242,
            0.014243705,
            0.003965384,
            0.0031508117,
            -0.030999009,
            0.037787113,
            -0.007297212,
            0.008162695,
            -0.00044122676,
            -0.017603816,
            -0.004002153,
            -0.025093358,
            -0.03016181,
            -0.0061262636,
            0.0011143804,
            -0.005190071,
            0.024595562,
            0.0139043,
            0.008575638,
            -0.0051023914,
            0.018124238,
            -0.008784938,
            0.01738886,
            0.03439306,
            -0.054123815,
            0.048602823,
            -0.08019014,
            0.018610718,
            -0.012886084,
            0.026269963,
            -0.03355586,
            -0.007263271,
            0.010397113,
            -0.05407856,
            0.033171203,
            -0.026496232,
            -0.037108302,
            -0.048467062,
            -0.016438525,
            0.014741499,
            -0.0015414653,
            0.058015663,
            -0.008151381,
            -0.013474386,
            -0.039122105,
            0.07534795,
            0.026043693,
            -0.0065901177,
            0.0059452476,
            0.039733034,
            -0.019889144,
            0.040660743,
            0.00012612792,
            0.010838339,
            -0.040615488,
            -0.027356058,
            0.0033063723,
            -0.046430632,
            0.020601895,
            -0.030863246,
            -0.040570233,
            0.04742622,
            -0.005068451,
            -0.0865257,
            0.028894696,
            -0.016596913,
            -0.02477658,
            0.04136218,
            -0.021280706,
            -0.029369863,
            0.0030631318,
            0.032854423,
            0.025568524,
            0.016461153,
            -0.03620322,
            -0.051861115,
            -0.014933828,
            -0.0053512887,
            0.00020894632,
            -0.015273234,
            -0.021427782,
            -0.012546679,
            -0.01413057,
            -0.024867088,
            -0.032243494,
            -0.010572472,
            -0.026269963,
            -0.022525191,
            0.019108513,
            0.017400173,
            0.006923866,
            0.00007247715,
            -0.0016263166,
            0.032990184,
            0.0041407435,
            0.036768895,
            0.013915613,
            0.032944933,
            0.0150469635,
            0.009593854,
            0.034506194,
            0.0056284694,
            0.06616139,
            0.03409891,
            -0.008536041,
            -0.025206493,
            0.0108213695,
            0.006233742,
            -0.03545653,
            0.035094496,
            -0.010040737,
            0.07960183,
            -0.016585601,
            0.042448275,
            -0.0056058425,
            -0.040887013,
            0.010159529,
            0.04968892,
            -0.04756198,
            -0.046611648,
            -0.07955658,
            0.023984633,
            -0.0057048355,
            -0.053082973,
            -0.035049245,
            0.0584682,
            0.008077844,
            0.043805897,
            -0.11268253,
            -0.03636161,
            -0.007410347,
            -0.0051844143,
            -0.011375731,
            0.026405724,
            0.0578799,
            0.037606094,
            0.020816851,
            -0.020058848,
            -0.021597484,
            0.08172877,
            0.03925787,
            -0.00016272004,
            -0.03029757,
            -0.029980792,
            -0.04733571,
            -0.04152057,
            -0.011579374,
            0.008943327,
            -0.036044832,
            -0.005399371,
            0.041407432,
            -0.03998193,
            0.06054989,
            0.045502923,
            0.02597581,
            -0.0061206073,
            0.042923443,
            -0.007772379,
            -0.03371425,
            0.009639108,
            0.026564114,
            -0.022445997,
            -0.023826245,
            0.06150022,
            -0.042312514,
            0.021529604,
            0.053309243,
            0.00052537094,
            -0.057382107,
            0.03332959,
            0.03656525,
            -0.014311586,
            0.061817,
            0.016212255,
            -0.032628153,
            0.01829394,
            -0.013892986,
            0.023396332,
            0.0780632,
            0.015431623,
            -0.019889144,
            -0.0046130824,
            -0.08014488,
            0.014775439,
            0.006165861,
            -0.067383245,
            -0.015205353,
            -0.044258438,
            0.3663766,
            -0.008886759,
            0.013349937,
            0.034121536,
            0.07380932,
            0.10245512,
            0.033306964,
            -0.057291597,
            -0.012094138,
            0.016596913,
            0.022276293,
            0.044824112,
            -0.067202225,
            0.05810617,
            -0.033306964,
            -0.060414124,
            -0.0078968275,
            0.019425292,
            0.06236005,
            -0.004941174,
            0.019119825,
            -0.060730904,
            -0.04029871,
            -0.04652114,
            -0.044778857,
            -0.0013851975,
            0.005037339,
            0.022389429,
            0.024686072,
            0.0023970492,
            -0.06394394,
            -0.018916182,
            -0.06398919,
            -0.023645228,
            -0.03461933,
            0.025025476,
            -0.032605525,
            0.0009072018,
            0.02681301,
            0.026473606,
            0.017569875,
            0.04235777,
            0.03636161,
            -0.05005095,
            0.010923191,
            -0.03265078,
            -0.0086718025,
            0.014945142,
            0.017400173,
            -0.037900247,
            -0.04258404,
            0.047018934,
            -0.026315216,
            -0.07996386,
            -0.007336809,
            -0.037809737,
            -0.027310805,
            0.017728265,
            0.031881463,
            -0.018237373,
            0.011415328,
            0.009876691,
            -0.019447917,
            -0.014741499,
            0.026699875,
            0.025319628,
            -0.0006328493,
            0.0016150031,
            -0.045050383,
            0.0023121978,
            -0.07783692,
            0.025319628,
            0.051770605,
            0.018112924,
            -0.030931126,
            -0.028691053,
            0.02742394,
            -0.015895477,
            0.008179666,
            0.027514448,
            0.011664225,
            0.0066636554,
            0.061817,
            -0.046928424,
            0.038398042,
            -0.05240416,
            0.013564894,
            0.06394394,
            -0.009186568,
            -0.03167782,
            0.00077921775,
            -0.008009963,
            0.05014146,
            -0.05552669,
            -0.019436603,
            0.011211685,
            -0.08810959,
            -0.0390316,
            0.03068223,
            -0.03278654,
            -0.007274585,
            -0.05765363,
            0.02681301,
            -0.063129365,
            0.027695464,
            0.011217342,
            -0.0151261585,
            -0.030704856,
            0.04801452,
            -0.00025844292,
            -0.07684134,
            0.019481858,
            -0.007201047,
            0.044756234,
            0.008043903,
            -0.03771923,
            0.024233531,
            -0.0018893556,
            -0.01461705,
            -0.0039455853,
            -0.012286468,
            0.00030175244,
            -0.01803373,
            -0.04742622,
            0.029505625,
            -0.00141136,
            0.026473606,
            0.06294835,
            0.04294607,
            -0.00675982,
            0.09955886,
            0.010204783,
            -0.034868225,
            0.043443866,
            0.032854423,
            0.008383309,
            0.03545653,
            0.03385001,
            -0.0012734766,
            0.01810161,
            0.012625873,
            0.04097752,
            -0.009627794,
            -0.03172307,
            0.055798214,
            -0.017830087,
            -0.036248475,
            0.0139043,
            0.03197197,
            -0.007240644,
            0.010827025,
            0.018078983,
            0.03226612,
            0.042674545,
            -0.006601431,
            0.02235549,
            -0.02207265,
            -0.0020986556,
            -0.000473046,
            -0.06973645,
            -0.01806767,
            -0.07009849,
            -0.01935741,
            0.042900816,
            -0.0105385315,
            0.00011941053,
            -0.021156257,
            -0.01810161,
            0.014662305,
            -0.0021962344,
            0.016076492,
            0.022672268,
            0.007093569,
            -0.015476877,
            -0.0032582898,
            0.055164658,
            0.05036773,
            -0.039710406,
            0.024052516,
            -0.024731325,
            -0.033872638,
            -0.014175824,
            0.013474386,
            -0.01965156,
            -0.014911202,
            -0.055436183,
            -0.024889715,
            0.032922305,
            0.0075800493,
            0.006918209,
            0.00077002554,
            -0.022445997,
            -0.078923024,
            -0.019843891,
            -0.055798214,
            0.06598037,
            0.016540347,
            -0.027175043,
            0.0038098234,
            -0.045570806,
            0.018146865,
            -0.0064600124,
            0.0567938,
            -0.021699306,
            -0.015861535,
            -0.05819668,
            -0.013530954,
            0.06226954,
            0.043013953,
            -0.021665365,
            -0.047516726,
            -0.020047534,
            -0.0015980328,
            0.061002426,
            0.0012579205,
            0.029053085,
            -0.01461705,
            -0.0130557865,
            -0.042516157,
            0.035411276,
            0.09539549,
            -0.03029757,
            0.035637546,
            -0.018146865,
            0.055571944,
            -0.024233531,
            0.008722713,
            -0.0018002618,
            0.050096206,
            0.0073198387,
            -0.001998248,
            -0.027242923,
            0.020805538,
            -0.0052975495,
            0.027831227,
            0.027446566,
            0.023147434,
            -0.019662874,
            -0.03242451,
            -0.04543504,
            0.014832007,
            -0.041837346,
            0.0089546405,
            -0.0054559386,
            0.053173482,
            -0.0069634635,
            -0.017852712,
            -0.011845241,
            -0.020126728,
            -0.043534372,
            -0.027740719,
            0.004106803,
            -0.041475315,
            0.01583891,
            0.045344535,
            -0.0021396668,
            -0.0069747767,
            -0.04566131,
            0.07186339,
            0.030659603,
            -0.01603124,
            -0.028781561,
            -0.0348456,
            0.055888724,
            -0.0020675433,
            -0.027582329,
            -0.017535934,
            0.007619647,
            -0.025274374,
            -0.016076492,
            -0.012014944,
            -0.009514659,
            0.01887093,
            0.025591152,
            0.015352428,
            -0.018836988,
            0.04577445,
            -0.0031790955,
            -0.044281065,
            0.004760158,
            -0.023351077,
            0.020375626,
            0.024957595,
            -0.012229901,
            0.0065052663,
            0.011460582,
            0.0087509975,
            -0.04710944,
            0.0032158643,
            0.012478798,
            -0.02355472,
            -0.010866623,
            -0.051091794,
            -0.03977829,
            0.005023197,
            -0.039959304,
            -0.021755872,
            0.0483313,
            0.06249581,
            -0.00003367536,
            -0.0027039282,
            -0.016404584,
            0.006239399,
            -0.0155334445,
            -0.013372565,
            0.023170061,
            -0.006782447,
            -0.016234882,
            -0.015363742,
            -0.011256939,
            -0.0020788568,
            -0.010006797,
            0.019538425,
            -0.026405724,
            0.023848873,
            -0.04733571,
            -0.030116554,
            -0.0038777043,
            0.039371002,
            0.02584005,
            0.026835637,
            0.054802626,
            -0.029369863,
            -0.004533888,
            -0.014741499,
            -0.041565824,
            0.008089157,
            -0.03550178,
            0.032447137,
            0.016008612,
            -0.020386938,
            0.008960297,
            0.024663445,
            0.05023197,
            -0.031021634,
            -0.010793085,
            -0.0024946283,
            -0.01780746,
            0.027310805,
            0.050865527,
            0.0078742,
            0.0011355932,
            -0.02961876,
            -0.022830656,
            -0.008202292,
            0.007432974,
            -0.007268928,
            -0.07602677,
            -0.015567385,
            -0.04910062,
            -0.024980223,
            -0.009876691,
            -0.016189627,
            0.041090656,
            0.016404584,
            -0.032356627,
            0.023577347,
            -0.0186786,
            0.053309243,
            0.02200477,
            -0.0068899253,
            0.024143023,
            0.026383096,
            0.006748507,
            -0.015646579,
            -0.018508896,
            0.02207265,
            0.031655192,
            -0.008321084,
            -0.0070256875,
            -0.0060640397,
            -0.07317576,
            0.022943791,
            -0.045095637,
            0.037108302,
            0.013530954,
            -0.054666862,
            -0.054983642,
            -0.0038692192,
            -0.002036431,
            -0.012761636,
            0.023962006,
            0.020239864,
            0.039506763,
            0.030342825,
            -0.047245204,
            -0.019187707,
            -0.052901957,
            0.032152984,
            -0.08838111,
            -0.048919603,
            -0.08883365,
            -0.0133386245,
            0.016314076,
            -0.0034195073,
            -0.03464196,
            -0.014741499,
            0.0072180172,
            0.01284083,
            -0.034958735,
            -0.021122316,
            0.057698883,
            -0.014933828,
            0.07765591,
            0.003131013,
            0.018904869,
            0.018022416,
            -0.0060923235,
            -0.0052070413,
            -0.041859973,
            -0.028215885,
            -0.037176184,
            0.025319628,
            0.012625873,
            0.0026077633,
            -0.045344535,
            -0.00400781,
            -0.020149356,
            0.027061908,
            0.035999577,
            0.0059565613,
            -0.0019402663,
            -0.037085675,
            0.046475884,
            0.011562403,
            0.028826814,
            -0.0086718025,
            -0.016925005,
            -0.028306393,
            -0.036022205,
            -0.007676214,
            0.05416907,
            -0.005586044,
            0.002853832,
            0.0011942821,
            -0.02461819,
            -0.029867657,
            0.018927496,
            -0.055662453,
            -0.009118686,
            0.006256369,
            -0.019764695,
            0.0011773118,
            0.06607088,
            -0.03642949,
            0.029188847,
            -0.10752357,
            0.019187707,
            0.021687992,
            -0.027921734,
            0.017309666,
            -0.021993456,
            0.0015895477,
            -0.03658788,
            -0.03303544,
            -0.023192689,
            0.014277645,
            -0.012026258,
            0.053354498,
            -0.0013738839,
            0.041407432,
            -0.047018934,
            0.028804189,
            -0.010029424,
            -0.00004401661,
            0.009769212,
            -0.0004963801,
            -0.018689914,
            -0.0011886252,
            0.027491821,
            -0.009254448,
            -0.03468721,
            0.0139495535,
            -0.026315216,
        ],
    )
    print(b)
