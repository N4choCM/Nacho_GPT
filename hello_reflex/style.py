# Common styles for questions and answers.
shadow = "rgba(255, 255, 255, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    bg="#a34c2c ",
    margin_left="0",  # Resetting margin-left
    color="#fff",
    float="right"  # Float the element to the right
)

answer_style = message_style | dict(
    bg="#8c88be ", margin_right=chat_margin, color="#fff"
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow, margin_bottom="3em"
)
button_style = dict(bg="#3498db", box_shadow=shadow, margin_bottom="3em")

nacho_gpt_heading = dict(color="#fff", font_size="2em", margin_y="1em")
custom_margin_container = dict(margin_y="1em", height = "90vh", )
custom_margin_footer = dict(flex="1", text_align="center")