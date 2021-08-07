from config import config
from keyvault import Keyvault
from output import Output
from hook import Hook

vault = Keyvault(list(config['keyvaults'].keys())[0])
local_storage = Output(config['output']['dir'])

local_storage.sync(vault.secrets)

if config['hook']:
  hook = Hook(config['hook']['action'], config['hook']['service'])
  hook.run()