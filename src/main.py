from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from copy_static import setup_docs, copy_static
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys


#public changed to docs

def main():


    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]


    setup_docs("docs")
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html","docs", basepath)


main()
