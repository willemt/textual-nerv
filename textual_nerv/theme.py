"""NERV theme for Textual applications.

Inspired by Evangelion's NERV computer systems.
A military/technical aesthetic with orange and black colors.
"""

from textual.theme import Theme

nerv = Theme(
    name="nerv",
    primary="#ff6600",  # Bright orange - borders, highlights, headers
    secondary="#ffaa00",  # Light orange - secondary elements, status text
    accent="#ff3300",  # Red-orange accent - focused elements, alerts
    foreground="#ff4400",  # Lighter orange - main body text
    background="#000000",  # Black background - main surface
    success="#00ff00",  # Green - success states
    warning="#ffaa00",  # Yellow/orange - warnings
    error="#ff0000",  # Red - errors and fail states
    dark=True,
    variables={
        # Surface colors
        "surface": "#000000",
        "surface-lighten-1": "#0a0500",  # Slightly raised surfaces
        "surface-lighten-2": "#1a0a00",  # Panels, headers, footers
        # Text colors
        "text": "#ffdfdf",
        "text-muted": "#cc7744",  # Muted orange for less important text
        "text-disabled": "#663300",
        # Primary variations
        "primary-darken-1": "#cc5200",
        "primary-lighten-1": "#ffaa00",
        # Panel and container styling
        "panel-background": "#1a0a00",
        "panel-border": "#ff6600",
        # Footer styling
        "footer-background": "#1a0a00",
        "footer-foreground": "#ff6600",
        "footer-key-foreground": "#ffaa00",
        # Input and focus
        "input-background": "#0a0500",
        "input-border": "#cc5200",
        "input-border-focus": "#ff6600",
        # Button styling
        "button-background": "#0a0500",
        "button-border": "#cc5200",
        "button-border-hover": "#ff6600",
        # Scrollbar
        "scrollbar-background": "#0a0500",
        "scrollbar-color": "#cc5200",
        "scrollbar-color-hover": "#ff6600",
        # DataTable styling
        "datatable-background": "#0a0500",
        "datatable-header-background": "#1a0a00",
        "datatable-cursor-background": "#cc5200",
        "datatable-cursor-background-focus": "#ff6600",
        # Block cursor - NERV style
        "block-cursor-text-style": "bold",
        "block-cursor-foreground": "#000000",
        "block-cursor-background": "#ff6600",
    },
)
