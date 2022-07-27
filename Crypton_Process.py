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


cryptons=[]

g1=CryptonObj("lolminer","lolminer","1.52a","lolMiner_v1.52a_Lin64.tar.gz")
print(f"A: {g1.Arhiv}")
print(f"AE: {g1.Arhiv_Extract}")
print(f"S: {g1.Path_Sh}")
#cryptons.append(g1)

class Crypton(object):
	"""docstring for Crypton"""
	def __init__(self):
		super(Crypton, self).__init__()
		pass
	def SelectCrypton(self):
		dict_crypt={
		  "lol_miner": CryptonObj("lolminer","lolminer","1.52a","lolMiner_v1.52a_Lin64.tar.gz"),
		  "b_miner": "",
		  "srb_miner": "",
		  "nb_miner": "",
		  "teamred_miner": "",
		  "t_rex_miner":""
		}
		return dict_crypt