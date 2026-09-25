# Vocab Orbit: Mission New York

An offline-capable, English-language vocabulary space game with 86 main entries from the supplied textbook pages 184–189. Practice sentences were written specifically for the game. German remains part of the translation exercises.

## Play

https://danizahnweh-oss.github.io/vocab-orbit-new-york/

Or download `index.html` and open it in a browser. No installation, account or internet connection required. Progress lasts only for the current session.

Choose a topic and mission length. Every question independently selects a random task type: German to English, English to German, or an English gap-fill sentence, each with equal probability. Consecutive tasks may have the same type. Mistake practice also uses random task types.

## Flight controls

- Left/right arrows or A/D: rotate the ship.
- Up arrow or W: thrust. Momentum carries the ship forward.
- Down arrow or S: brake.
- Space: fire. Shots must physically hit an answer asteroid.
- P: pause or resume. Switching away automatically pauses flight.
- Touchscreens: drag the virtual joystick in any direction; push further for more thrust. Release to brake. Hold Fire with the other thumb to keep shooting. The original flight buttons are also available.
- The joystick resets on release, touch cancellation, pause, resize, a hit and the next question.

The ship wraps around the screen edges. Asteroids drift and rotate within six separate regions so their labels stay readable. There is no time limit or loss of lives. Each question has six answer asteroids. A correct hit immediately advances to the next question (or opens the final results), with no waiting time. Wrong answers wait for Next. The answer-button alternative allows play without flying. Mistakes can be practised again at the end.

Each correct answer earns 100 points plus a streak bonus of 20 per consecutive additional hit, capped at 100 bonus points. Mistakes reset the streak. Reduced-motion settings disable asteroid rotation and hit particles; flight itself remains interactive.

## Edit

`vocabulary.tsv` contains the words, translations and sentences. `index.template.html` contains the application. Run `python3 build.py` after changes to regenerate the standalone `index.html`. GitHub Pages publishes the main branch.

## Validation

Browser checks cover English interface labels, all three random type selections, actual thrust and rotation, pause/resume, projectile collision scoring, mistake practice, accessible answer buttons and mobile layout. Desktop and mobile screenshots were visually inspected.

## Hard mode

Use the Hard mode button before or during a mission. When enabled, touching any asteroid returns the ship to its launch position and resets the hit streak. The current question and earned points remain. A brief visible shield prevents repeated collision penalties immediately after respawning. Collision detection follows the visible ship and asteroid outlines. Normal mode still allows flying through asteroids.
