from config import config
from keyvault import Keyvault
from output import Output

vault = Keyvault(list(config['keyvaults'].keys())[0])
local_storage = Output(config['output']['dir'])

local_storage.sync(vault.secrets)
