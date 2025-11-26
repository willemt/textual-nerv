"""Example app demonstrating the NERV theme."""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    Log,
    ProgressBar,
    Rule,
    Sparkline,
    Static,
)

from textual_nerv import nerv


class NervDemo(App):
    """Demo application for the NERV theme."""

    TITLE = "NERV SYSTEM"
    SUB_TITLE = "MAGI-01"

    CSS = """
    Screen {
        layout: grid;
        grid-size: 2;
        grid-gutter: 1;
        padding: 1;
    }

    .panel {
        border: solid $primary;
        padding: 1;
    }

    .panel-title {
        text-style: bold;
        color: $secondary;
        margin-bottom: 1;
    }

    #control-panel Horizontal {
        height: auto;
        margin-top: 1;
    }

    #control-panel Button {
        margin-right: 1;
    }

    #status-column {
        row-span: 2;
    }

    #status-column > Container {
        margin-bottom: 1;
    }

    #status-panel {
        height: 1fr;
    }

    DataTable {
        height: 100%;
    }

    #sync-panel {
        hatch: cross $primary 30%;
    }

    .metric-row {
        height: auto;
        margin-bottom: 1;
    }

    .metric-label {
        width: 20;
    }

    .metric-value {
        width: 8;
        text-align: right;
        color: $secondary;
    }

    ProgressBar {
        width: 1fr;
        padding-left: 1;
    }

    Sparkline {
        height: 3;
        margin: 1 0;
    }

    Log {
        height: 100%;
        border: solid $primary-darken-1;
        background: $surface;
    }

    #alerts-panel {
        height: auto;
    }

    #alerts-panel Static {
        height: auto;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("t", "toggle_theme", "Toggle Theme"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        # Control Panel
        yield Container(
            Static("CONTROL INTERFACE", classes="panel-title"),
            Input(placeholder="Enter command sequence..."),
            Horizontal(
                Button("Execute", variant="primary"),
                Button("Abort", variant="error"),
                Button("Reset", variant="default"),
            ),
            Rule(),
            Static("OPERATION LOG", classes="panel-title"),
            Log(id="op-log"),
            id="control-panel",
            classes="panel",
        )

        # Status Column (Status + Alerts stacked)
        yield Vertical(
            Container(
                Static("SYSTEM STATUS", classes="panel-title"),
                DataTable(),
                id="status-panel",
                classes="panel",
            ),
            Container(
                Static("SYSTEM ALERTS", classes="panel-title"),
                Static("[#00ff00]● MAGI CONSENSUS: UNANIMOUS[/]"),
                Static("[#00ff00]● SYNC RATIO: NOMINAL[/]"),
                Static("[#ffaa00]● AT FIELD: ACTIVE - 120% OUTPUT[/]"),
                Static("[#ff6600]● LCL PRESSURE: ELEVATED[/]"),
                Static("[#ff0000]● PATTERN BLUE: CONFIRMED[/]"),
                Static("[#ff0000]● ALERT LEVEL: FIRST[/]"),
                id="alerts-panel",
                classes="panel",
            ),
            id="status-column",
        )

        # Sync Metrics Panel with cross-hatch
        yield Container(
            Static("SYNC METRICS", classes="panel-title"),
            Horizontal(
                Static("PILOT-00", classes="metric-label"),
                Static("72.4%", classes="metric-value"),
                ProgressBar(total=100, show_eta=False),
                classes="metric-row",
            ),
            Horizontal(
                Static("PILOT-01", classes="metric-label"),
                Static("98.2%", classes="metric-value"),
                ProgressBar(total=100, show_eta=False),
                classes="metric-row",
            ),
            Horizontal(
                Static("PILOT-02", classes="metric-label"),
                Static("84.7%", classes="metric-value"),
                ProgressBar(total=100, show_eta=False),
                classes="metric-row",
            ),
            Static("HARMONICS", classes="panel-title"),
            Sparkline([], id="harmonics"),
            id="sync-panel",
            classes="panel",
        )

        yield Footer()

    def on_mount(self) -> None:
        self.register_theme(nerv)
        self.theme = "nerv"

        # Populate DataTable
        table = self.query_one(DataTable)
        table.add_columns("SYSTEM", "STATUS", "LOAD", "TEMP")
        table.add_rows([
            ("MAGI-01 MELCHIOR", "ONLINE", "42%", "34°C"),
            ("MAGI-02 BALTHASAR", "ONLINE", "38%", "32°C"),
            ("MAGI-03 CASPER", "ONLINE", "45%", "35°C"),
            ("UMBILICAL BRIDGE", "ACTIVE", "67%", "28°C"),
            ("AT FIELD GEN", "STANDBY", "12%", "22°C"),
            ("ENTRY PLUG SYS", "READY", "8%", "24°C"),
            ("LCL PLANT", "CYCLING", "55%", "37°C"),
            ("POSITRON RIFLE", "CHARGING", "78%", "89°C"),
        ])

        # Set progress bars
        bars = self.query(ProgressBar)
        for bar, value in zip(bars, [72.4, 98.2, 84.7]):
            bar.progress = value

        # Populate sparkline with harmonic data
        import math
        harmonics = self.query_one("#harmonics", Sparkline)
        harmonics.data = [abs(math.sin(x * 0.3) * 50 + math.cos(x * 0.7) * 30) for x in range(40)]

        # Add log entries
        log = self.query_one("#op-log", Log)
        log.write_line("[12:01:03] MAGI system initialized")
        log.write_line("[12:01:05] Pilot neural link established")
        log.write_line("[12:01:08] Entry plug inserted")
        log.write_line("[12:01:12] LCL ionization complete")
        log.write_line("[12:01:15] A10 nerve connection nominal")
        log.write_line("[12:01:18] Sync test commencing...")
        log.write_line("[12:01:22] Borderline cleared")
        log.write_line("[12:01:25] EVA Unit-01 activated")

    def action_toggle_theme(self) -> None:
        self.theme = "textual-dark" if self.theme == "nerv" else "nerv"


if __name__ == "__main__":
    app = NervDemo()
    app.run()
