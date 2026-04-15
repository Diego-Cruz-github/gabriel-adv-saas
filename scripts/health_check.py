#!/usr/bin/env python3
"""
health_check.py - Monitoramento do SaaS Juridico
Verifica API, webhook endpoint e tempo de resposta.
"""

import requests
import sys
from datetime import datetime


def check_api(base_url, timeout=10):
    """Verifica API principal."""
    try:
        resp = requests.get(f"{base_url}/api/health", timeout=timeout)
        elapsed = int(resp.elapsed.total_seconds() * 1000)
        status = "OK" if resp.status_code == 200 else "WARN"
        print(f"  [{status}] API: HTTP {resp.status_code} ({elapsed}ms)")
        return resp.status_code == 200
    except Exception as e:
        print(f"  [FAIL] API: {e}")
        return False


def check_webhook(base_url, timeout=10):
    """Verifica se o endpoint de webhook esta acessivel."""
    try:
        resp = requests.options(f"{base_url}/api/webhook/intake", timeout=timeout)
        accessible = resp.status_code < 500
        status = "OK" if accessible else "FAIL"
        print(f"  [{status}] Webhook endpoint: HTTP {resp.status_code}")
        return accessible
    except Exception as e:
        print(f"  [FAIL] Webhook: {e}")
        return False


def check_response_time(base_url, timeout=10):
    """Mede tempo de resposta e valida SLA (< 1 minuto)."""
    try:
        resp = requests.post(
            f"{base_url}/api/triage/test",
            json={"area": "civil", "test": True},
            timeout=timeout
        )
        elapsed_ms = int(resp.elapsed.total_seconds() * 1000)
        within_sla = elapsed_ms < 60000  # SLA: < 1 minuto
        status = "OK" if within_sla else "WARN"
        print(f"  [{status}] Triage response: {elapsed_ms}ms (SLA: < 60000ms)")
        return within_sla
    except Exception as e:
        print(f"  [FAIL] Triage: {e}")
        return False


def run_checks(base_url):
    """Executa verificacao completa."""
    print(f"\n[{datetime.utcnow().isoformat()}] Legal SaaS Health Check")
    print(f"  Target: {base_url}")
    print("-" * 50)

    results = [
        check_api(base_url),
        check_webhook(base_url),
        check_response_time(base_url),
    ]

    all_ok = all(results)
    print("-" * 50)
    print(f"  Result: {'ALL HEALTHY' if all_ok else 'ISSUES DETECTED'}")
    return all_ok


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:3000"
    ok = run_checks(url)
    sys.exit(0 if ok else 1)
