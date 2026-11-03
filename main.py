"""Report certificate expiries from an inventory CSV.

Usage: python3 main.py certs.csv [--now 2026-11-02] [--warn-days 30]
CSV columns: domain,expiry (ISO date).
EXPIRED if past, EXPIRING SOON within warn-days, else OK. Soonest
expiry first.
"""
import argparse, csv, sys
from datetime import date


def report(rows, now, warn_days):
    out = []
    for row in rows:
        expiry = date.fromisoformat(row["expiry"].strip())
        days = (expiry - now).days
        verdict = "EXPIRED" if days < 0 else ("EXPIRING SOON" if days <= warn_days else "OK")
        out.append((row["domain"], days, verdict))
    return sorted(out, key=lambda r: r[1])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--now", default=None)
    parser.add_argument("--warn-days", type=int, default=30)
    args = parser.parse_args(argv)
    now = date.fromisoformat(args.now) if args.now else date.today()
    with open(args.path, newline="", encoding="utf-8") as f:
        for domain, days, verdict in report(list(csv.DictReader(f)), now, args.warn_days):
            print(f"{domain}: {verdict} ({days} days)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
