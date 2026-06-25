## ADDED Requirements

### Requirement: Scroll-reactive parallax
The system SHALL adjust Canvas rendering parameters in response to page scroll position.

#### Scenario: Foreground mountains fade on scroll
- **WHEN** the page is scrolled past 50vh
- **THEN** the opacity of the foreground mountain SHALL decrease proportionally to scroll distance, reaching 0 at 100vh

#### Scenario: Ink density increases
- **WHEN** the page is scrolled past 30vh
- **THEN** the ink saturation of the background mountain layers SHALL increase by up to 30% at 80vh

#### Scenario: Scroll resets on top
- **WHEN** the page is scrolled back to the top
- **THEN** all Canvas parameters SHALL return to their initial values within 300ms

### Requirement: Hero content layer integration
The Canvas SHALL render behind brand typography as a background layer.

#### Scenario: Canvas behind text
- **WHEN** the Hero section is visible
- **THEN** the Canvas SHALL be positioned with `z-index: 0` and the text/content SHALL be above it with `z-index: 2`

#### Scenario: Divider line reacts to landscape
- **WHEN** the hero divider line is visible
- **THEN** its accent color SHALL be extended by a subtle ink spread animation drawn on the Canvas

### Requirement: Memory management
The system SHALL clean up resources when the Hero section is out of view or the component unmounts.

#### Scenario: Animation stops when hidden
- **WHEN** the Hero section scrolls out of view (past 150vh from top)
- **THEN** the animation loop SHALL pause and resume when the Hero re-enters the viewport
