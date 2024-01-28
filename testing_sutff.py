from pathlib import Path
import random

from amnon_graphics import AmnonApp, AmnonButton, layouts, colors, AmnonLabel, AmnonTextBox


def on_click(song: str):
    """
    example of a button adding another button in a random position.
    The new buttons will also add other buttons when clicked!! :O
    """
    # app.add_button(AmnonButton(
    #     position=layouts.Position(random.randint(0, 1400), random.randint(0, 800)),
    #     size=layouts.Size(50, 50),
    #     on_click=on_click,
    #     on_click_params=[app],
    #     text=f'asdf'
    # ))
    print(song)

def on_text_change(textbox_id: str, app: AmnonApp):
    new_text = app.get_textbox_text(textbox_id)
    app.add_label(AmnonLabel(
        position=layouts.Position(random.randint(0, 1400), random.randint(0, 800)),
        size=layouts.Size(50, 50),
        text=new_text
    ))


if __name__ == '__main__':
    app = AmnonApp(
        name='my_app',
        height=800,
        width=1400,
        background_color=colors.RGB(10, 30, 10)
    )
    label = AmnonLabel(
        position=layouts.Position(20, 20),
        size=layouts.Size(100, 20),
        text='Click it:',
        background_color=colors.RGB(200, 100, 50)
    )
    button1 = AmnonButton(
        position=layouts.Position(20, 45),
        size=layouts.Size(100, 50),
        on_click=on_click,
        on_click_params=['song1'],
        text='Press Here',
        background_color=colors.WHITE
    )
    button2 = AmnonButton(
        position=layouts.Position(20, 45),
        size=layouts.Size(100, 50),
        on_click=on_click,
        on_click_params=['song2'],
        text='Press Here',
        background_color=colors.WHITE
    )
    textbox = AmnonTextBox(
        position=layouts.Position(20, 100),
        size=layouts.Size(100, 20),
        on_change=on_text_change,
        on_change_params=[app]
    )

    app.add_button(button1)
    app.add_button(button2)
    app.add_label(label)
    app.add_textbox(textbox)
    app.set_background_image(Path(r"C:\Users\helper\Pictures\ocean.jpg"))

    app.run()
