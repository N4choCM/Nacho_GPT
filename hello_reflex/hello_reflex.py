import reflex as rx
from hello_reflex import style
from hello_reflex.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question),
            style=style.question_style,  # Apply styling to the question box
            text_align="right",  # Align the text within the question box to the right
        ),
        rx.box(
            rx.text(answer),
            style=style.answer_style,
            text_align="left",  # Align the text within the answer box to the left
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            id="question",
            placeholder="Ask a question",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        rx.box(
            rx.heading("Nacho-GPT 💬", size="2xl"),
            style=style.nacho_gpt_heading,
            text_align="center",
        ),
        chat(),
        action_bar(),
        rx.box(
            rx.text("Made with ❤️ by Nacho Campos Dev"),
            rx.text("Powered by OpenAI's GPT-3"),
            rx.html("<br/>"),
            style=style.custom_margin_footer,
            text_align="center",
        ),
        style=style.custom_margin_container,
    )


app = rx.App()
app.add_page(index)
app.compile()
