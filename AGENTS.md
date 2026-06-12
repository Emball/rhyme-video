# rhyme-video

Genius-style rhyme scheme video generator for rap. Takes a song, word-level alignment data, and a manually annotated rhyme scheme, and renders a synchronized highlight video.

## Architecture

Three decoupled modules with JSON handoff files between them:

### Module 1 — `align.py` (client-side)
- Input: audio file + ground truth lyrics (plain text)
- Runs WhisperX to produce word-level timestamps
- Output: `alignment.json`

### Module 2 — `annotate.html` (browser-based GUI)
- Input: paste lyrics manually; load `alignment.json` when ready to export
- GUI lets user select character-level spans within words and assign colors from a preset pastel palette
- Includes a song manager to keep multiple songs organized
- Output: `annotation.json`

### Module 3 — `render.py` (client-side or sandbox)
- Input: `alignment.json` + `annotation.json` + audio file
- Renders Genius-style video: gray background, bold black text, scrolling lyrics, highlight spans snap on at word onset distributed evenly across annotated spans within each word
- Output: ProRes 422 HQ, 1080p, 29.97fps, same duration as audio

## Handoff Formats

### alignment.json
```json
{
  "words": [
    { "index": 0, "text": "So", "start": 0.42, "end": 0.61 },
    ...
  ]
}
```

### annotation.json
```json
{
  "spans": [
    { "word_index": 5, "char_start": 0, "char_end": 3, "color": "#FFB347" },
    ...
  ]
}
```

## Video Spec
- Resolution: 1920x1080
- FPS: 29.97
- Codec: ProRes 422 HQ
- Duration: matches audio
- Background: flat gray (#888888 approx, match Genius)
- Font: bold black, large, left-aligned
- Highlight: solid pastel rounded rectangle behind text, snaps on at calculated onset

## Reveal Mechanic
For a word with N annotated spans, divide the word's duration evenly across N spans and snap each highlight on sequentially. No fade — binary on/off at each interval boundary.

## Palette
Pastel colors only. Diverse, high contrast against gray background. Defined in annotate.html and shared with render.py via annotation.json hex values.
