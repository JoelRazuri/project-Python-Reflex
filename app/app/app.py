"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx




class State(rx.State):
    """The app state."""

    pass

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="rigth"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "Why is Reflex?",
            "A way to build wewb apps in pure Python",
        ),
        (
            "What can I make with it?",
            "Anything form a simple website yo a complex web app!",
        )
    ]
    return rx.box(
        *[
            qa(question, answer) for question, answer in qa_pairs
        ]
    ) 

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question"),
        rx.button("Ask")
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar())


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
