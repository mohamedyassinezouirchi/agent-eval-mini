# Demo: AI agent trace checks

A short, reproducible way to show what this repository currently does.

## Walkthrough

Run `python agent_eval.py examples/traces.jsonl` to see the result of a synthetic trace. For a negative demo, add an event with `"approved":false` and `"executed":true` before the final event; the evaluator reports a failed run. This does not run or connect to an AI model.

## Suggested content for a public demo

- Show your terminal with the command and actual output.
- Explain the developer problem in one sentence.
- Share the repository link and the specific limitation below.
- Invite practical feedback or a reproducible issue instead of asking for stars.

## Honest limitations

Synthetic agent traces only; never upload customer prompts or private execution logs.

## Validation

Run the project's tests where applicable:

```bash
python -m unittest discover -s tests -v
```

Avoid presenting a demo output as a real performance measurement unless you actually collected it.
