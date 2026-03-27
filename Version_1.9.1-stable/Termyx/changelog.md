# Version 1.9.1
## is here with the following updates:

## App Improvements

- The Timer now uses the Windows `SystemExclamation` sound on completion.
- The Pomodoro Timer now uses simple beeps for standard work and break transitions.
- The final Pomodoro completion alert now uses a separate Windows `SystemExclamation` sound to better distinguish it from normal cycle changes.
- Timer and Pomodoro sound behavior now feels more intentional and easier to recognize during use.

## Scripting Improvements

- Sound logic in `timer.py` and `pom_tmr.py` has been cleaned up into dedicated helper functions.
- Windows-specific sound handling now uses `winsound` when available.
- Cross-platform fallback behavior has been preserved for non-Windows platforms by falling back to the terminal bell.

## Bug Fixes

- The Pomodoro Timer no longer relies entirely on `\a`, which was not playing reliably in some terminal environments.
- The Timer completion alert is now more reliable on Windows terminals.
- The Pomodoro completion alert is now distinct from regular session-transition beeps.
