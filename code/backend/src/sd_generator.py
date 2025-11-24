"""
Stable Diffusion image generation via MLX for Apple Silicon
"""
import io
from typing import Optional
from PIL import Image
import yaml

class StableDiffusionGenerator:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.model = None
        self.loaded = False
        print("Stable Diffusion generator initialized (model will load on first use)")

    def _load_model(self):
        """Lazy load the Stable Diffusion model"""
        if self.loaded:
            return True

        try:
            # mflux 0.11+ has classes in mflux.generate
            from mflux.generate import Flux1, Config, ModelConfig

            print("Loading FLUX model (this may take a minute on first run)...")

            # Use FLUX.1 schnell for faster generation
            self.model = Flux1(
                model_config=ModelConfig.schnell(),
                quantize=8  # 8-bit quantization for memory efficiency
            )

            self.loaded = True
            print("FLUX model loaded successfully")
            return True

        except ImportError as e:
            print(f"mflux import error: {e}")
            print("Install with: pip install mflux")
            return False
        except Exception as e:
            print(f"Error loading FLUX model: {e}")
            import traceback
            traceback.print_exc()
            return False

    def generate(
        self,
        prompt: str,
        width: int = 512,
        height: int = 512,
        num_steps: int = 4,
        seed: Optional[int] = None
    ) -> Optional[bytes]:
        """Generate an image from a text prompt"""

        if not self._load_model():
            return self._generate_placeholder(width, height, "SD model not available")

        try:
            from mflux.generate import Config

            # Generate the image
            result = self.model.generate_image(
                seed=seed or 42,
                prompt=prompt,
                config=Config(
                    num_inference_steps=num_steps,
                    height=height,
                    width=width
                )
            )

            # Convert to PNG bytes - result.image is a PIL Image
            buffer = io.BytesIO()
            if hasattr(result, 'image'):
                result.image.save(buffer, format='PNG')
            else:
                # Fallback if result is the image itself
                result.save(buffer, format='PNG')
            return buffer.getvalue()

        except Exception as e:
            print(f"Generation error: {e}")
            return self._generate_placeholder(width, height, f"Error: {str(e)[:50]}")

    def generate_logo(
        self,
        description: str,
        style: str = "modern",
        width: int = 512,
        height: int = 512
    ) -> Optional[bytes]:
        """Generate a logo from description"""

        style_prompts = {
            "modern": "modern minimalist logo design, clean lines, professional, vector style",
            "vintage": "vintage retro logo design, classic typography, badge style",
            "playful": "playful colorful logo design, friendly, rounded shapes",
            "tech": "tech startup logo, geometric shapes, futuristic, sleek",
            "organic": "organic natural logo design, flowing lines, earth tones",
            "bold": "bold impactful logo design, strong typography, high contrast"
        }

        style_addition = style_prompts.get(style, style_prompts["modern"])
        full_prompt = f"{description}, {style_addition}, white background, centered, high quality"

        return self.generate(full_prompt, width, height)

    def generate_icon(
        self,
        description: str,
        style: str = "flat",
        width: int = 256,
        height: int = 256
    ) -> Optional[bytes]:
        """Generate an icon from description"""

        style_prompts = {
            "flat": "flat design icon, solid colors, no shadows, minimalist",
            "3d": "3D rendered icon, soft shadows, glossy finish",
            "outline": "outline icon, thin lines, minimal, monochrome",
            "glyph": "glyph icon, solid fill, simple shapes",
            "duotone": "duotone icon, two colors, modern flat design"
        }

        style_addition = style_prompts.get(style, style_prompts["flat"])
        full_prompt = f"single {description} icon, {style_addition}, centered, white background, app icon style"

        return self.generate(full_prompt, width, height, num_steps=4)

    def generate_illustration(
        self,
        description: str,
        style: str = "digital",
        width: int = 768,
        height: int = 512
    ) -> Optional[bytes]:
        """Generate an illustration"""

        style_prompts = {
            "digital": "digital illustration, clean lines, vibrant colors",
            "watercolor": "watercolor painting style, soft edges, artistic",
            "vector": "vector art style, flat colors, geometric shapes",
            "sketch": "pencil sketch style, hand-drawn look, detailed",
            "isometric": "isometric illustration, 3D perspective, flat shading"
        }

        style_addition = style_prompts.get(style, style_prompts["digital"])
        full_prompt = f"{description}, {style_addition}, high quality, detailed"

        return self.generate(full_prompt, width, height, num_steps=4)

    def generate_ui_mockup(
        self,
        description: str,
        device: str = "desktop",
        width: int = 768,
        height: int = 512
    ) -> Optional[bytes]:
        """Generate a UI mockup image"""

        device_prompts = {
            "desktop": "desktop application UI, modern interface design",
            "mobile": "mobile app UI, smartphone screen, iOS/Android style",
            "tablet": "tablet app UI, iPad style interface",
            "web": "website UI design, browser mockup"
        }

        device_context = device_prompts.get(device, device_prompts["desktop"])
        full_prompt = f"{description}, {device_context}, clean modern design, professional UI/UX, high fidelity mockup"

        return self.generate(full_prompt, width, height, num_steps=4)

    def _generate_placeholder(self, width: int, height: int, message: str) -> bytes:
        """Generate a placeholder image when SD is not available"""
        from PIL import Image, ImageDraw, ImageFont

        img = Image.new('RGB', (width, height), color='#fef3c7')  # Amber background
        draw = ImageDraw.Draw(img)

        # Border
        draw.rectangle([0, 0, width-1, height-1], outline='#f59e0b', width=3)

        # Try to load fonts
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 12)
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
        except:
            font = ImageFont.load_default()
            title_font = font

        # Title
        title = "AI Image Generation Unavailable"
        bbox = draw.textbbox((0, 0), title, font=title_font)
        x = (width - (bbox[2] - bbox[0])) // 2
        draw.text((x, 20), title, fill='#92400e', font=title_font)

        # Error message
        lines = message.split('\n')
        y = 50
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            x = (width - (bbox[2] - bbox[0])) // 2
            draw.text((x, y), line, fill='#b45309', font=font)
            y += 18

        # Setup instructions
        setup_text = [
            "Setup Instructions:",
            "1. pip install mflux",
            "2. First run downloads ~4GB model",
            "3. Requires Apple Silicon Mac"
        ]
        y = height - 90
        for line in setup_text:
            bbox = draw.textbbox((0, 0), line, font=font)
            x = (width - (bbox[2] - bbox[0])) // 2
            draw.text((x, y), line, fill='#78350f', font=font)
            y += 16

        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        return buffer.getvalue()


# Singleton
_sd_generator = None

def get_sd_generator() -> StableDiffusionGenerator:
    global _sd_generator
    if _sd_generator is None:
        _sd_generator = StableDiffusionGenerator()
    return _sd_generator
