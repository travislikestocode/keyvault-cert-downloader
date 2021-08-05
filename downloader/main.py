from config import config
from keyvault import Keyvault
from output import Output

vault = Keyvault(list(config['keyvaults'].keys())[0])
cert_dir = Output(config['cert_dir'])
secrets = map(lambda s: vault.get_secret(s.name), vault.secret_list)

cert_dir.sync(secrets)
