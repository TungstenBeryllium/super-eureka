import unittest

from block_to_html import markdown_to_html_node


class TestBlockToHTML(unittest.TestCase):

    def test_h6_heading(self):
        md = "###### Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h6>Heading</h6></div>")

    def test_ordered_list(self):
        md = """
1. YUI
2. AZUSA
3. MUGI
4. AZUKETTO
5. K-ON
6. **MUGI** AND `MUGI`
7. _RITSU_

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol>"
            "<li>YUI</li>"
            "<li>AZUSA</li>"
            "<li>MUGI</li>"
            "<li>AZUKETTO</li>"
            "<li>K-ON</li>"
            "<li><b>MUGI</b> AND <code>MUGI</code></li>"
            "<li><i>RITSU</i></li>"
            "</ol></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p>"
            "</div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>"
            "This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- YUI
- AZUSA
- MUGI
- AZUKETTO
- K-ON
- **MUGI** AND `MUGI`

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul>"
            "<li>YUI</li>"
            "<li>AZUSA</li>"
            "<li>MUGI</li>"
            "<li>AZUKETTO</li>"
            "<li>K-ON</li>"
            "<li><b>MUGI</b> AND <code>MUGI</code></li>"
            "</ul></div>",
        )

    def test_quote(self):
            md = """
> YUI
> AZUSA
> MUGI
> AZUKETTO
> K-ON
> **MUGI** AND `MUGI`
> _RITSU_
> Fuwa

"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><blockquote>"
                "YUI AZUSA MUGI AZUKETTO K-ON "
                "<b>MUGI</b> AND <code>MUGI</code> "
                "<i>RITSU</i> Fuwa"
                "</blockquote></div>",
            )



if __name__ == "__main__":
    unittest.main(verbosity=2)
