# Markdown for python
Programmatically write markdown to a file

```python
from markdown import Markdown

md = Markdown("README.md")

md.heading("Level 3 Heading", 3)
md.paragraph("This is a paragraph")
md.heading("Level 4 Heading", 4)
md.paragraph("> *This* is a blockquote\n")

header = ["table", "header"]
rows = [
  ["Row one", "match length with header"],
  ["Row two", "must match"]
]

md.table(header, rows)

md.markdown('a+')
```

## Results
### Level 3 Heading
This is a paragraph
#### Level 4 Heading
> *This* is a blockquote

|table|header|
|---|---|
|Row one|match length with header|
|Row two|must match|
