# Your portrait

Upload your chosen photograph here as `mingsongyan.jpg`.
No real portrait is currently included.

In `docs/index.html`, replace the entire `portrait-placeholder` div with:

```html
<img class="portrait" src="images/mingsongyan.jpg"
     alt="Portrait of Mingsong Yan" width="180">
```

Keep `.profile-row` and the adjacent `.profile` div in place.
For a PNG or another filename, use that exact filename in the src attribute.
The image keeps its natural proportions; it is not cropped into a circle.
If you later use the optional jemdoc build, also update
`jemdoc-source/profile.html` so regeneration keeps the photo.
