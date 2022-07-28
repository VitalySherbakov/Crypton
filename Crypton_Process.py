import os, sys, json, time, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))


class CryptonObj(object):
	"""docstring for CryptonObj"""
	Arhiv=""
	Arhiv_Extract=""
	Path_Sh=""
	Cmd=""
	def __init__(self,cmd: str, sh: str, folder: str, folder2: str, arhiv: str, folder_path="/content/Crypton"):
		super(CryptonObj, self).__init__()
		self.Arhiv = f"{folder_path}/{folder}/{arhiv}"
		self.Arhiv_Extract=f"{folder_path}/{folder}"
		self.Path_Sh=f"{folder_path}/{folder}/{folder2}/{sh}"
		self.Cmd=cmd

class Crypton(object):
	"""docstring for Crypton"""
	def __init__(self):
		super(Crypton, self).__init__()
		pass
	def GetDictCrypton(self):
		"""Получить Словари"""
		dict_crypt={
		  "lol_miner": CryptonObj("-xzvf","lolMiner","lolminer", "1.52a","lolMiner_v1.52a_Lin64.tar.gz"),
		  "b_miner": CryptonObj("-xf","bminer","bminer","1.52a","bminer-v16.4.11-2849b5c-amd64.tar.xz"),
		  "srb_miner": CryptonObj("-xf","srbminer","srbminer","1.52a","SRBMiner-Multi-1-0-2-Linux.tar.xz"),
		  "nb_miner": CryptonObj("-xzf","nbminer","nbminer","1.52a","NBMiner_42.2_Linux.tgz"),
		  "teamred_miner": CryptonObj("-xzf","teamredminer","teamredminer","1.52a","teamredminer-v0.10.2-linux.tgz"),
		  "t_rex_miner": CryptonObj("-xzvf","t-rex","t_rex","1.52a","t-rex-0.26.4-linux.tar.gz"),
		  "g_miner": CryptonObj("-xf","miner","gminer","1.52a","gminer_3_03_linux64.tar.xz")
		}
		return dict_crypt
	def GetDictName(self):
		"""Имина Словарей"""
		for li in dictes.keys():
			print(f"Имя: {li}")
	def GetExtractAll(self, dictes: {}):
		"""Распаковка Полностью"""
		arhives=[]
		for li in dictes.keys():
			arhives.append(f'{dictes[li].Cmd} "{dictes[li].Arhiv}" -C "{dictes[li].Arhiv_Extract}"')
		return arhives
