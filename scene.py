from manim import *
import os

class CreateCircle(Scene):
    def construct(self):

        raza=float(os.environ.get("MANIM_RAZA",2.0))
        culoare_str = os.environ.get("MANIM_CULOARE","PINK")

        culori = {
            "BLUE": BLUE,
            "RED": RED,
            "GREEN": GREEN,
            "YELLOW": YELLOW,
            "PINK": PINK
        }
        culoare_aleasa = culori.get(culoare_str, BLUE)

        circle = Circle(radius=raza,color=culoare_aleasa)  # Create a circle
        circle.set_fill(culoare_aleasa, opacity=0.5)  # Set the color and transparency

        text=Text(f"Raza: {raza}",font_size=24).next_to(circle,UP)

        self.play(Create(circle),Write(text))  # Show the circle on screen
        self.wait(1)