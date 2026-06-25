# ink-landscape-canvas Specification

## Purpose
TBD - created by archiving change redesign-index-ink-wash. Update Purpose after archive.
## Requirements
### Requirement: Landscape generation
The system SHALL generate mountain landscape shapes using layered noise-based terrain curves.

#### Scenario: Mountains render in layers
- **WHEN** the Canvas initializes
- **THEN** it SHALL draw 3–5 mountain layers with decreasing opacity from foreground to background

#### Scenario: Mountain shapes appear organic
- **WHEN** a mountain layer is drawn
- **THEN** its contour SHALL use bezier curves with Perlin-noise vertex offsets for irregular, hand-painted appearance

#### Scenario: Ink wash texture
- **WHEN** a mountain layer is rendered
- **THEN** it SHALL use `globalCompositeOperation: 'multiply'` and radial gradients to simulate ink bleeding on rice paper

### Requirement: Mist particle system
The system SHALL render slow-moving mist particles that drift across mountain layers.

#### Scenario: Mist particles float
- **WHEN** the animation loop runs
- **THEN** 20–60 particles SHALL move horizontally at random speeds between 0.1–0.5 px/frame and fade in/out with sine-wave opacity

#### Scenario: Mist respects layer depth
- **WHEN** particles are rendered
- **THEN** particles behind mountain layers SHALL draw with lower opacity than those in front

### Requirement: Ink splash accent
The system SHALL periodically render ink-splash accents at random positions for organic texture.

#### Scenario: Random ink drops
- **WHEN** the animation timer reaches a random interval (3–8 seconds)
- **THEN** the system SHALL draw an expanding radial ink blotch that fades out over 2–4 seconds

### Requirement: Performance adaptation
The system SHALL degrade gracefully on low-power devices.

#### Scenario: Reduced quality on mobile
- **WHEN** `window.innerWidth < 768`
- **THEN** the system SHALL reduce mountain layers to 3 and particle count to 20

#### Scenario: No animation for reduced motion
- **WHEN** the user has `prefers-reduced-motion: reduce`
- **THEN** the system SHALL render a static frame and skip the animation loop

