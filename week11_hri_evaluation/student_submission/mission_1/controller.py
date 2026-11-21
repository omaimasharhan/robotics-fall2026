"""Complete decide() using the transition requirements in the Lab 10 guide."""


def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]

    if kind == "CANCEL" and phase in ("EXECUTING", "WAIT_READY"):
        return "cancel"  # TODO Mission 1. Cancel before processing active work.

    if kind in ("REQUEST", "CORRECT"):
         if kind == "REQUEST" and phase in ("IDLE", "CLARIFY", "CONFIRM", "RECOVERY", "CANCELLED"):
                   return "select" if target in ("red", "blue") else "clarify"
         if kind == "CORRECT" and target in ("red", "blue"):
                   return "select"  # TODO Mission 1. Clarify an unnamed target and guard when a request may replace it.

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    if phase == "WAIT_READY" and kind == "READY":
         return "release"  # TODO Tutorial. Require the READY event too.

    if kind == "TIMEOUT" and phase ==  "WAIT_READY":
        return "timeout"  # TODO Mission 1. Enter recovery from a waiting state.

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    return "hold"
