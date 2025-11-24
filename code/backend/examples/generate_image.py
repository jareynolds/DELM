#!/usr/bin/env python3
"""
Example: Generate UI component images using the DELM API
"""

import requests
import base64
from pathlib import Path

BASE_URL = "http://127.0.0.1:3005"

def generate_mockup(component_type: str, props: dict, filename: str, width: int = 400, height: int = 300):
    """Generate a component mockup and save to file"""

    response = requests.post(
        f"{BASE_URL}/generate/mockup",
        json={
            "component_type": component_type,
            "props": props,
            "width": width,
            "height": height,
            "format": "base64"
        }
    )

    if response.status_code == 200:
        data = response.json()

        # Decode base64 and save to file
        image_bytes = base64.b64decode(data["image"])
        Path(filename).write_bytes(image_bytes)

        print(f"✓ Saved {component_type} to {filename}")
        print(f"  Size: {data['width']}x{data['height']}")

        # Return data_url for use in HTML
        return data["data_url"]
    else:
        print(f"✗ Error: {response.status_code} - {response.text}")
        return None


def generate_from_html(html_code: str, filename: str, width: int = 800, height: int = 600):
    """Render HTML/JSX code to image"""

    response = requests.post(
        f"{BASE_URL}/generate/code-to-image",
        json={
            "code": html_code,
            "width": width,
            "height": height,
            "format": "base64"
        }
    )

    if response.status_code == 200:
        data = response.json()
        image_bytes = base64.b64decode(data["image"])
        Path(filename).write_bytes(image_bytes)
        print(f"✓ Saved HTML render to {filename}")
        return data["data_url"]
    else:
        print(f"✗ Error: {response.status_code} - {response.text}")
        return None


def main():
    print("DELM Image Generation Examples\n")

    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Example 1: Button variants
    print("Generating buttons...")
    generate_mockup(
        "button",
        {"text": "Primary Button", "variant": "primary"},
        "output/button_primary.png"
    )
    generate_mockup(
        "button",
        {"text": "Secondary", "variant": "secondary"},
        "output/button_secondary.png"
    )
    generate_mockup(
        "button",
        {"text": "Outline", "variant": "outline"},
        "output/button_outline.png"
    )

    # Example 2: Card component
    print("\nGenerating card...")
    generate_mockup(
        "card",
        {
            "title": "Product Feature",
            "content": "Discover our latest innovation that will transform your workflow."
        },
        "output/card.png",
        width=400,
        height=450
    )

    # Example 3: Form input with error
    print("\nGenerating inputs...")
    generate_mockup(
        "input",
        {
            "label": "Email Address",
            "placeholder": "you@example.com",
            "type": "email"
        },
        "output/input_normal.png"
    )
    generate_mockup(
        "input",
        {
            "label": "Password",
            "placeholder": "Enter password",
            "type": "password",
            "error": "Password must be at least 8 characters"
        },
        "output/input_error.png"
    )

    # Example 4: Alert types
    print("\nGenerating alerts...")
    for alert_type in ["info", "success", "warning", "error"]:
        generate_mockup(
            "alert",
            {
                "message": f"This is a {alert_type} alert message",
                "type": alert_type
            },
            f"output/alert_{alert_type}.png",
            width=450,
            height=100
        )

    # Example 5: Navigation bar
    print("\nGenerating navbar...")
    generate_mockup(
        "navbar",
        {
            "logo": "MyApp",
            "items": ["Dashboard", "Projects", "Team", "Settings"]
        },
        "output/navbar.png",
        width=800,
        height=80
    )

    # Example 6: Avatar
    print("\nGenerating avatars...")
    generate_mockup(
        "avatar",
        {"name": "Sarah Connor", "size": "lg"},
        "output/avatar.png",
        width=200,
        height=200
    )

    # Example 7: Progress bar
    print("\nGenerating progress...")
    generate_mockup(
        "progress",
        {"value": 67, "label": "Upload Progress"},
        "output/progress.png",
        width=350,
        height=100
    )

    # Example 8: Toggle switch
    print("\nGenerating toggles...")
    generate_mockup(
        "toggle",
        {"label": "Dark Mode", "checked": True},
        "output/toggle_on.png",
        width=200,
        height=100
    )
    generate_mockup(
        "toggle",
        {"label": "Notifications", "checked": False},
        "output/toggle_off.png",
        width=200,
        height=100
    )

    # Example 9: Custom HTML render
    print("\nGenerating custom HTML...")
    custom_html = '''
    <div class="p-6 max-w-sm bg-white rounded-xl shadow-lg space-y-4">
        <div class="flex items-center space-x-4">
            <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center">
                <span class="text-white text-xl font-bold">D</span>
            </div>
            <div>
                <h3 class="text-lg font-semibold text-gray-900">DELM System</h3>
                <p class="text-sm text-gray-500">Design Experience LM</p>
            </div>
        </div>
        <p class="text-gray-600">
            Generate beautiful UI components with natural language prompts.
        </p>
        <button class="w-full py-2 px-4 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600">
            Get Started
        </button>
    </div>
    '''
    generate_from_html(custom_html, "output/custom.png", width=400, height=300)

    print(f"\n✓ All images saved to {output_dir.absolute()}")
    print("\nTo view: open output/")


if __name__ == "__main__":
    main()
