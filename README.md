# Keyvault-Cert-Downloader

Yet another Azure keyvault cert downloader.

## Usage

At the moment, this will:

1. Read all of the certificate bundles from a configured instance of Azure Key Vault
2. Convert them to PEM encoding
3. Output them to a configured location on disk

The tool satisfies a very specific need we have @faithlife. More functionality and flexibility coming soon (maybe)!

### Example config

```yaml
keyvaults:
  my-vault:
output:
  dir: /tmp/crt
  ext: .pem
```

## Development

### Venv Setup

Use Python 3.8:

```bash
/usr/local/opt/python@3.8/bin/python3 -m venv .venv
```

### Bootstrap

```bash
source .venv/bin/activate
pip install -r requirements.txt
```
