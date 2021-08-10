import yaml
from .args import args

config = yaml.load(args.config_file, Loader=yaml.FullLoader)

if len(config['keyvaults'].keys()) > 1:
    raise RuntimeError('Only one Key Vault supported in MVP')
