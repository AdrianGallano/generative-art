import numpy as np
import PIL.Image
import PIL.ImageDraw
import random
from django.conf import settings
from pathlib import Path
import os


class Pattern:
    @staticmethod
    def generate_circles(num_circles, pm1, pm2, pm3, pm4, pm5):
        """Generates coordinates and radii for a given number of circles.

        Args:
            num_circles: The number of circles to generate.

        Returns:
            A tuple containing:
                centers: A NumPy array of shape (num_circles, 2) containing the center
                    coordinates of each circle.
                radii: A NumPy array of shape (num_circles,) containing the radius of
                    each circle.
        """
        theta = np.linspace(0, 2 * np.pi, num_circles)
        x = np.cos(pm1 * theta) * (1 - 0.75 * np.cos(pm3 * theta) ** 2)
        y = np.sin(pm2 * theta) * (1 - 0.75 * np.cos(pm4 * theta) ** 2)
        radius = 1 / 200 + 1 / 10 * np.sin(pm5 * theta) ** 6

        return np.stack([x, y], axis=1), radius

    @staticmethod
    def draw_circles(centers, radii, image_size, max_cycle):
        image = PIL.Image.new("RGBA", image_size, (0, 0, 0, 0))
        draw = PIL.ImageDraw.Draw(image)

        scaled_centers = (centers + 1) * (np.array(image_size) / 2)

        cycle = max_cycle
        for center, radius in zip(scaled_centers, radii):
            if cycle == max_cycle:
                cycle = 0
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            draw.ellipse(
                [
                    (center[0] - radius, center[1] - radius),
                    (center[0] + radius, center[1] + radius),
                ],
                outline=color,
                fill=color + (255,),
                width=10,
            )
            cycle += 1

        return image

    @staticmethod
    def create(
        user_id=None,
        title="untitled",
        image_size=(500, 500),
        num_circles=2000000,
        max_color_cycle=1000,
        parameters = [14, 14, 20, 24, 54]
    ):
        pm1, pm2, pm3, pm4, pm5 = parameters
        centers, radii = Pattern.generate_circles(num_circles, pm1, pm2, pm3, pm4, pm5)
        image = Pattern.draw_circles(centers, radii, image_size, max_color_cycle)

        if user_id is not None:
            title = str(user_id) + "_" + title

        relative_image_path = os.path.join("images", f"{title}.png")
        image_path = os.path.join(settings.MEDIA_ROOT, "images", f"{title}.png")

        # Save the image
        image.save(image_path)

        return relative_image_path
