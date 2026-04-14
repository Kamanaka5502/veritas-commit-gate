
def run_demo():
    print("[1] SYSTEM PROPOSES")
    print("Prescription recommendation generated\n")

    print("[2] PHYSICIAN SIGN-OFF")
    print("Approved by physician\n")

    print("[3] COMMIT ATTEMPT")
    print("→ this is the moment it tries to become real\n")

    print("[4] VERITAS DECISION")
    print("If admissible:")
    print("→ EXECUTE")
    print("If not admissible:")
    print("→ REFUSE\n")

    print("[5] RECEIPT")
    print("reason: example_reason")
    print("state_hash: abc123")
    print("request_hash: def456")
    print("policy_integrity_hash: ghi789")
    print("replay_token: xyz000\n")

    print("[6] REPLAY")
    print("Re-evaluating...")
    print("Result: EXECUTE")
    print("Match: TRUE")
