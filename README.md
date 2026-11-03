# ssl-cert-inventory-reporter

Check a certificate inventory CSV for expiries: expired, expiring soon or OK, soonest first — the inventory counterpart to a live TLS check.

## How to run

```sh
python3 main.py certs.csv --warn-days 30
```

## Example output

```
old.example.com: EXPIRED (-1 days)
shop.example.com: EXPIRING SOON (18 days)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
