# Calculator Workflow Notes

This file documents the custom workflow added to `Calculator.html` so it is easy to restore or understand later.

## What was added

### Results behavior
- When you enter the `Results` page, the calculator runs `analyze()` automatically.
- If you leave `Results` and come back later, it recalculates again.
- A dedicated `Analyze Again` button is available on the `Results` page to rerun the analysis manually.

### PDF / print
- `Print` and `Export PDF` use the same rendered report HTML.
- The PDF export is generated from the same report markup used for printing, so both outputs match visually.

### Shareable link
- The share link stores the current deal inputs in the URL hash.
- Opening the link restores the inputs and recalculates the results.

### CSV export / import
- `Export CSV` writes a full deal snapshot to CSV.
- The CSV contains:
  - User-entered input values
  - Repair rows
  - Calculated result values
- Importing a CSV restores only the input fields and repair rows.
- Calculated values are not imported directly; they are recalculated after the data is loaded.

### CSV shortcut
- The CSV file picker is hidden from the screen.
- Use this keyboard shortcut to load a CSV:
  - `Ctrl + Shift + L` on Windows/Linux
  - `Cmd + Shift + L` on Mac

## Notes

- The hidden CSV file input is still part of the page, but it is not shown in the UI.
- The shortcut opens the file picker directly.
- The import flow is designed for quick testing of the calculator with saved data snapshots.

