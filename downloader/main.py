from keyvault import Keyvault
from config import config
from files import Files

vault = Keyvault(list(config['keyvaults'].keys())[0])
cert_dir = Files(config['cert_dir'])

for secret in vault.secrets:
    s = vault.get_secret(secret.name)
    cert_filename = Files.make_filename(s.name, config['cert_ext'])

    if cert_filename not in cert_dir.file_names:
      cert_dir.output_file(cert_filename, s.value)
