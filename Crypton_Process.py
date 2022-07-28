import os, sys, json, time, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))


class CryptonObj(object):
	"""docstring for CryptonObj"""
	Arhiv=""
	Arhiv_Extract=""
	Path_Sh=""
	Info=""
	Cmd=""
	def __init__(self,cmd: str, sh: str, folder: str, folder2: str, arhiv: str,info: str, folder_path="/content/Crypton"):
		super(CryptonObj, self).__init__()
		self.Arhiv = f"{folder_path}/{folder}/{arhiv}"
		self.Arhiv_Extract=f"{folder_path}/{folder}"
		self.Cmd=cmd
		self.Info=info
		if self.IsBlank(folder2)==False:
			self.Path_Sh=f"{folder_path}/{folder}/{folder2}/{sh}"
		else:
			self.Path_Sh=f"{folder_path}/{folder}/{sh}"
	def GetRoot(self):
		"""Корень Папки"""
		return dir_path
	def IsBlank(self,mystr: str):
		"""Являеться Строка Пустой"""
		return not (mystr and mystr.strip())

class Crypton(object):
	"""docstring for Crypton"""
	def __init__(self):
		super(Crypton, self).__init__()
		pass
	def GetDictCrypton(self, filejson: str, ReadFile=1, encod="utf-8"):
		"""Получить Словари"""
		dict_crypt={
		  "lol_miner": CryptonObj("-xzvf","lolMiner","lolminer", "1.52a","lolMiner_v1.52a_Lin64.tar.gz","--algo ETHASH --pool eth.hashcity.org:7777 --user bonakva.[WORKER]"),
		  "b_miner": CryptonObj("-xf","bminer","bminer","bminer-v16.4.11-2849b5c","bminer-v16.4.11-2849b5c-amd64.tar.xz","-uri ethproxy://bonakva.[WORKER]@eth.hashcity.org:7777"),
		  "srb_miner": CryptonObj("-xf","srbminer","srbminer","SRBMiner-Multi-1-0-2","SRBMiner-Multi-1-0-2-Linux.tar.xz","Смотрите *.SH файлы"),
		  "nb_miner": CryptonObj("-xzf","nbminer","nbminer","NBMiner_Linux","NBMiner_42.2_Linux.tgz","-a ethash -o stratum+tcp://eth.hashcity.org:7777 -u bonakva.[WORKER]"),
		  "teamred_miner": CryptonObj("-xzf","teamredminer","teamredminer","teamredminer-v0.10.2-linux","teamredminer-v0.10.2-linux.tgz","-a ethash -o stratum+tcp://eth.hashcity.org:7777 -u bonakva.[WORKER] -p x"),
		  "t_rex_miner": CryptonObj("-xzvf","t-rex","t_rex","","t-rex-0.26.4-linux.tar.gz","-a ethash -o stratum+tcp://eth.hashcity.org:7777 -u bonakva.[WORKER] -p x"),
		  "g_miner": CryptonObj("-xf","miner","gminer","","gminer_3_03_linux64.tar.xz","--algo ETCHASH --pool $POOL --user $WALLET $@")
		}
		if ReadFile==1:
			dict_crypt=self.ReadSetting(filejson)
		if ReadFile==2:
			dict_crypt=self.ReadJson(filejson)
		return dict_crypt
	def ReadSetting(self, filejson: str, encod="utf-8"):
		"""Чтение Новых Данных Minor"""
		dict_crypt={}
		try:
			with open(filejson, 'r', encoding=encod) as f:
				data = json.load(f)
				dict_crypt={
				  "lol_miner": CryptonObj(data['lol_miner'][0],data['lol_miner'][1],data['lol_miner'][2], data['lol_miner'][3],data['lol_miner'][4],data['lol_miner'][5]),
				  "b_miner": CryptonObj(data['b_miner'][0],data['b_miner'][1],data['b_miner'][2], data['b_miner'][3],data['b_miner'][4],data['b_miner'][5]),
				  "srb_miner": CryptonObj(data['srb_miner'][0],data['srb_miner'][1],data['srb_miner'][2], data['srb_miner'][3],data['srb_miner'][4],data['srb_miner'][5]),
				  "nb_miner": CryptonObj(data['nb_miner'][0],data['nb_miner'][1],data['nb_miner'][2], data['nb_miner'][3],data['nb_miner'][4],data['nb_miner'][5]),
				  "teamred_miner": CryptonObj(data['teamred_miner'][0],data['teamred_miner'][1],data['teamred_miner'][2], data['teamred_miner'][3],data['teamred_miner'][4],data['teamred_miner'][5]),
				  "t_rex_miner": CryptonObj(data['t_rex_miner'][0],data['t_rex_miner'][1],data['t_rex_miner'][2], data['t_rex_miner'][3],data['t_rex_miner'][4],data['t_rex_miner'][5]),
				  "g_miner": CryptonObj(data['g_miner'][0],data['g_miner'][1],data['g_miner'][2], data['g_miner'][3],data['g_miner'][4],data['g_miner'][5])
				}
		except Exception as ex:
			print(f"ERROR JSON: {ex}!")
		return dict_crypt
	def ReadJson(self, filejson: str):
		dict_crypt={}
		data = json.load(filejson)
		dict_crypt={
				  "lol_miner": CryptonObj(data['lol_miner'][0],data['lol_miner'][1],data['lol_miner'][2], data['lol_miner'][3],data['lol_miner'][4],data['lol_miner'][5]),
				  "b_miner": CryptonObj(data['b_miner'][0],data['b_miner'][1],data['b_miner'][2], data['b_miner'][3],data['b_miner'][4],data['b_miner'][5]),
				  "srb_miner": CryptonObj(data['srb_miner'][0],data['srb_miner'][1],data['srb_miner'][2], data['srb_miner'][3],data['srb_miner'][4],data['srb_miner'][5]),
				  "nb_miner": CryptonObj(data['nb_miner'][0],data['nb_miner'][1],data['nb_miner'][2], data['nb_miner'][3],data['nb_miner'][4],data['nb_miner'][5]),
				  "teamred_miner": CryptonObj(data['teamred_miner'][0],data['teamred_miner'][1],data['teamred_miner'][2], data['teamred_miner'][3],data['teamred_miner'][4],data['teamred_miner'][5]),
				  "t_rex_miner": CryptonObj(data['t_rex_miner'][0],data['t_rex_miner'][1],data['t_rex_miner'][2], data['t_rex_miner'][3],data['t_rex_miner'][4],data['t_rex_miner'][5]),
				  "g_miner": CryptonObj(data['g_miner'][0],data['g_miner'][1],data['g_miner'][2], data['g_miner'][3],data['g_miner'][4],data['g_miner'][5])
				}
		return dict_crypt
	def GetDictName(self, dictes: {}):
		"""Имена Словарей"""
		for li in dictes.keys():
			print(f"Имя: {li} | ./*.sh {dictes[li].Info}")
	def IsBlank(self,mystr: str):
		"""Являеться Строка Пустой"""
		return not (mystr and mystr.strip())
	def GetExtractAll(self, dictes: {}):
		"""Распаковка Полностью"""
		arhives=[]
		for li in dictes.keys():
			arhives.append(f'{dictes[li].Cmd} "{dictes[li].Arhiv}" -C "{dictes[li].Arhiv_Extract}"')
		return arhives
