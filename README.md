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


# Pre Processing paragraphs
Add custom parsers to alter text behaviour in paragrpah nodes

```python
from markdown import Markdown

def f(s: str) -> str:
  return s.upper()

def f2(s: str) -> str:
  return s.upper().replace('LOWERCASE', 'UPPERCASE')

# .md will be added for you if you do not add it yourself
md = Markdown("README") 
md.add(f)

md.heading("Results", 2)
md.paragraph("i am in not in lowercase")
md.add(f2)
md.paragraph("i am in lowercase")

md.markdown('a+')
```

## Results
I AM IN NOT IN LOWERCASE
I AM IN UPPERCASE
