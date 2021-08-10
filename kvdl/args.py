import argparse
from os import path
from pathlib import Path

parser = argparse.ArgumentParser(
  description='Deploy Azure Key Vault Certificates'
)

parser.add_argument(
  '-c', '--config-file',
  nargs='?',
  type=argparse.FileType('r'),
  default=path.join(
    Path.home(),
    '.keyvault-cert-downloader/config.yaml'
  )
)

args = parser.parse_args()
