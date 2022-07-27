import os, sys, json, time, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))


class CryptonObj(object):
	"""docstring for CryptonObj"""
	Arhiv=""
	Arhiv_Extract=""
	Path_Sh=""
	def __init__(self, sh: str, folder: str, arhiv: str, folder_path="/content/Crypton"):
		super(CryptonObj, self).__init__()
		self.Arhiv = f"{folder_path}/{folder}/{arhiv}"
		self.Arhiv_Extract=f"{folder_path}/{folder}"
		self.Path_Sh=f"{folder_path}/{folder}/{sh}"


#cryptons=[]

# g1=CryptonObj("lolminer","lolminer","lolMiner_v1.52a_Lin64.tar.gz")
# print(f"A: {g1.Arhiv}")
# print(f"AE: {g1.Arhiv_Extract}")
# print(f"S: {g1.Path_Sh}")
#cryptons.append(g1)

class Crypton(object):
	"""docstring for Crypton"""
	def __init__(self):
		super(Crypton, self).__init__()
		pass
	def GetDictCrypton(self):
		"""Получить Словари"""
		dict_crypt={
		  "lol_miner": CryptonObj("lolMiner","lolminer","lolMiner_v1.52a_Lin64.tar.gz"),
		  "b_miner": CryptonObj("bminer","bminer","bminer-v16.4.11-2849b5c-amd64.tar.gz"),
		  "srb_miner": CryptonObj("srbminer","srbminer","SRBMiner-Multi-1-0-2-Linux.tar.gz"),
		  "nb_miner": CryptonObj("nbminer","nbminer","NBMiner_42.2_Linux.tar.gz"),
		  "teamred_miner": CryptonObj("teamredminer","teamredminer","teamredminer-v0.10.2-linux.tar.gz"),
		  "t_rex_miner": CryptonObj("t-rex","t_rex","t-rex-0.26.4-linux.tar.gz"),
		  "g_miner": CryptonObj("miner","gminer","gminer_3_03_linux64.tar.gz")
		}
		return dict_crypt
	def GetExtractAll(self, dictes: {}):
		"""Распаковка"""
		arhives=[]
		for li in dictes.keys():
			arhives.append(f'-xzvf "{dictes[li].Arhiv}" -C "{dictes[li].Arhiv_Extract}"')
		return arhives

g=Crypton()
mass=g.GetDictCrypton()

g.GetExtractAll(mass)