from lib.keyvault import keyvault
from lib.config import config

keyvaults = {}

for kv in config.keys():
  keyvaults[kv] = keyvault(kv)

for vault in keyvaults.values():
  for secret in vault.secrets:
    s = vault.get_secret(secret.name)
    print(s.name)
    print(s.value)