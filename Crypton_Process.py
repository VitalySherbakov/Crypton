import os, sys, json, time, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))


class CryptonObj(object):
	"""docstring for CryptonObj"""
	Arhiv=""
	Arhiv_Extract=""
	Path_Sh=""
	def __init__(self, sh: str, folder: str, folder2: str, arhiv: str, folder_path="/content/Crypton"):
		super(CryptonObj, self).__init__()
		self.Arhiv = f"{folder_path}/{folder}/{arhiv}"
		self.Arhiv_Extract=f"{folder_path}/{folder}"
		self.Path_Sh=f"{folder_path}/{folder}/{folder2}/{sh}"


class Crypton(object):
	"""docstring for Crypton"""
	def __init__(self):
		super(Crypton, self).__init__()
		pass
	def GetDictCrypton(self):
		"""Получить Словари"""
		dict_crypt={
		  "lol_miner": CryptonObj("lolMiner","lolminer", "1.52a","lolMiner_v1.52a_Lin64.tar.gz"),
		  "b_miner": CryptonObj("bminer","bminer","1.52a","bminer-v16.4.11-2849b5c-amd64.tar.gz"),
		  "srb_miner": CryptonObj("srbminer","srbminer","1.52a","SRBMiner-Multi-1-0-2-Linux.tar.gz"),
		  "nb_miner": CryptonObj("nbminer","nbminer","1.52a","NBMiner_42.2_Linux.tar.gz"),
		  "teamred_miner": CryptonObj("teamredminer","1.52a","teamredminer","teamredminer-v0.10.2-linux.tar.gz"),
		  "t_rex_miner": CryptonObj("t-rex","t_rex","1.52a","t-rex-0.26.4-linux.tar.gz"),
		  "g_miner": CryptonObj("miner","gminer","1.52a","gminer_3_03_linux64.tar.gz")
		}
		return dict_crypt
	def GetExtractAll(self, dictes: {}):
		"""Распаковка"""
		arhives=[]
		for li in dictes.keys():
			arhives.append(f'-xzvf "{dictes[li].Arhiv}" -C "{dictes[li].Arhiv_Extract}"')
		return arhives

