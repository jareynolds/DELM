"""
Image generation service for UI mockups - renders real components
"""
import base64
import io
import asyncio
from typing import Optional, Dict, Any
from PIL import Image, ImageDraw, ImageFont
import yaml

class ImageGenerator:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.playwright = None
        self.browser = None
        print("Image generator initialized")

    async def _get_browser(self):
        """Get or create playwright browser"""
        if self.browser is None:
            try:
                from playwright.async_api import async_playwright
                self.playwright = await async_playwright().start()
                self.browser = await self.playwright.chromium.launch()
                print("Playwright browser launched")
            except Exception as e:
                print(f"Playwright not available: {e}")
                print("Run: playwright install chromium")
                return None
        return self.browser

    async def html_to_png(
        self,
        html_content: str,
        width: int = 800,
        height: int = 600,
        full_page: bool = False
    ) -> bytes:
        """Convert HTML/CSS to PNG image using playwright"""
        browser = await self._get_browser()

        if browser is None:
            return self._generate_error_image(width, height, "Playwright not installed\nRun: playwright install chromium")

        try:
            page = await browser.new_page(viewport={'width': width, 'height': height})

            # Full HTML document with Tailwind CSS
            full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            padding: 16px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f9fafb;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .component-wrapper {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}
    </style>
</head>
<body>
    <div class="component-wrapper">
        {html_content}
    </div>
</body>
</html>"""

            await page.set_content(full_html)
            await page.wait_for_timeout(1000)  # Wait for Tailwind to load and render

            screenshot = await page.screenshot(type='png', full_page=full_page)
            await page.close()

            return screenshot
        except Exception as e:
            print(f"Screenshot error: {e}")
            return self._generate_error_image(width, height, f"Render error:\n{str(e)[:100]}")

    def _generate_error_image(self, width: int, height: int, message: str) -> bytes:
        """Generate an error placeholder image"""
        img = Image.new('RGB', (width, height), color='#fee2e2')
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, width-1, height-1], outline='#ef4444', width=2)

        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
        except:
            font = ImageFont.load_default()

        # Draw multiline text
        y = 20
        for line in message.split('\n'):
            draw.text((20, y), line, fill='#991b1b', font=font)
            y += 20

        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        return buffer.getvalue()

    async def generate_component_mockup(
        self,
        component_type: str,
        props: Dict[str, Any],
        width: int = 400,
        height: int = 300
    ) -> bytes:
        """Generate a real component mockup using HTML/Tailwind"""

        html = self._generate_component_html(component_type, props)
        return await self.html_to_png(html, width, height)

    def _generate_component_html(self, component_type: str, props: Dict[str, Any]) -> str:
        """Generate HTML for a component type"""

        if component_type == 'button':
            text = props.get('text', 'Button')
            color = props.get('color', '#3b82f6')
            variant = props.get('variant', 'primary')

            if variant == 'outline':
                return f'''
                <button class="px-6 py-3 border-2 border-blue-500 text-blue-500 font-semibold rounded-lg
                    hover:bg-blue-50 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                    {text}
                </button>'''
            elif variant == 'secondary':
                return f'''
                <button class="px-6 py-3 bg-gray-200 text-gray-800 font-semibold rounded-lg
                    hover:bg-gray-300 transition-colors focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2">
                    {text}
                </button>'''
            else:  # primary
                return f'''
                <button style="background-color: {color}" class="px-6 py-3 text-white font-semibold rounded-lg
                    hover:opacity-90 transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 shadow-md">
                    {text}
                </button>'''

        elif component_type == 'card':
            title = props.get('title', 'Card Title')
            content = props.get('content', 'Card content goes here.')
            image = props.get('image', '')

            image_html = f'<img src="{image}" class="w-full h-48 object-cover" />' if image else '''
                <div class="w-full h-48 bg-gradient-to-br from-blue-400 to-purple-500"></div>'''

            return f'''
            <div class="w-80 bg-white rounded-xl shadow-lg overflow-hidden border border-gray-200">
                {image_html}
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">{title}</h3>
                    <p class="text-gray-600 mb-4">{content}</p>
                    <button class="w-full px-4 py-2 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition-colors">
                        Learn More
                    </button>
                </div>
            </div>'''

        elif component_type == 'input':
            label = props.get('label', 'Label')
            placeholder = props.get('placeholder', 'Enter text...')
            input_type = props.get('type', 'text')
            error = props.get('error', '')

            error_html = f'<p class="mt-1 text-sm text-red-500">{error}</p>' if error else ''
            border_class = 'border-red-500 focus:ring-red-500' if error else 'border-gray-300 focus:ring-blue-500'

            return f'''
            <div class="w-80">
                <label class="block text-sm font-medium text-gray-700 mb-1">{label}</label>
                <input type="{input_type}" placeholder="{placeholder}"
                    class="w-full px-4 py-2 border {border_class} rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-colors" />
                {error_html}
            </div>'''

        elif component_type == 'navbar':
            logo = props.get('logo', 'Logo')
            items = props.get('items', ['Home', 'About', 'Contact'])

            nav_items = ''.join([
                f'<a href="#" class="text-gray-300 hover:text-white transition-colors">{item}</a>'
                for item in items
            ])

            return f'''
            <nav class="w-full bg-gray-900 px-6 py-4 flex items-center justify-between">
                <div class="text-xl font-bold text-white">{logo}</div>
                <div class="flex items-center space-x-6">
                    {nav_items}
                </div>
            </nav>'''

        elif component_type == 'alert':
            message = props.get('message', 'This is an alert message')
            alert_type = props.get('type', 'info')

            colors = {
                'info': 'bg-blue-50 border-blue-500 text-blue-700',
                'success': 'bg-green-50 border-green-500 text-green-700',
                'warning': 'bg-yellow-50 border-yellow-500 text-yellow-700',
                'error': 'bg-red-50 border-red-500 text-red-700'
            }

            icons = {
                'info': '''<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>''',
                'success': '''<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>''',
                'warning': '''<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>''',
                'error': '''<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path></svg>'''
            }

            return f'''
            <div class="w-96 p-4 border-l-4 {colors.get(alert_type, colors['info'])} rounded-r-lg flex items-start space-x-3">
                {icons.get(alert_type, icons['info'])}
                <p class="text-sm font-medium">{message}</p>
            </div>'''

        elif component_type == 'badge':
            text = props.get('text', 'Badge')
            badge_type = props.get('type', 'default')

            colors = {
                'default': 'bg-gray-100 text-gray-800',
                'primary': 'bg-blue-100 text-blue-800',
                'success': 'bg-green-100 text-green-800',
                'warning': 'bg-yellow-100 text-yellow-800',
                'error': 'bg-red-100 text-red-800'
            }

            return f'''
            <span class="px-3 py-1 text-sm font-medium rounded-full {colors.get(badge_type, colors['default'])}">
                {text}
            </span>'''

        elif component_type == 'avatar':
            name = props.get('name', 'John Doe')
            src = props.get('src', '')
            size = props.get('size', 'md')

            sizes = {'sm': 'w-8 h-8 text-sm', 'md': 'w-12 h-12 text-lg', 'lg': 'w-16 h-16 text-xl'}
            size_class = sizes.get(size, sizes['md'])

            if src:
                return f'''
                <img src="{src}" alt="{name}" class="{size_class} rounded-full object-cover border-2 border-white shadow-md" />'''
            else:
                initials = ''.join([n[0].upper() for n in name.split()[:2]])
                return f'''
                <div class="{size_class} rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white font-bold shadow-md">
                    {initials}
                </div>'''

        elif component_type == 'toggle':
            checked = props.get('checked', False)
            label = props.get('label', 'Toggle')

            bg_class = 'bg-blue-500' if checked else 'bg-gray-300'
            translate = 'translate-x-5' if checked else 'translate-x-0'

            return f'''
            <label class="flex items-center space-x-3 cursor-pointer">
                <div class="relative">
                    <div class="w-10 h-6 {bg_class} rounded-full transition-colors"></div>
                    <div class="absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow transform {translate} transition-transform"></div>
                </div>
                <span class="text-gray-700 font-medium">{label}</span>
            </label>'''

        elif component_type == 'progress':
            value = props.get('value', 60)
            label = props.get('label', '')

            label_html = f'<div class="flex justify-between mb-1"><span class="text-sm font-medium text-gray-700">{label}</span><span class="text-sm text-gray-500">{value}%</span></div>' if label else ''

            return f'''
            <div class="w-64">
                {label_html}
                <div class="w-full bg-gray-200 rounded-full h-2.5">
                    <div class="bg-blue-500 h-2.5 rounded-full transition-all" style="width: {value}%"></div>
                </div>
            </div>'''

        else:
            # Generic component
            return f'''
            <div class="p-6 bg-white rounded-lg shadow-md border border-gray-200">
                <p class="text-gray-600">{component_type} component</p>
            </div>'''

    async def generate_from_code(
        self,
        code: str,
        width: int = 800,
        height: int = 600
    ) -> bytes:
        """Generate image from React/HTML code by rendering it"""
        html = self._code_to_html(code)
        return await self.html_to_png(html, width, height)

    def _code_to_html(self, code: str) -> str:
        """Convert React/JSX code to renderable HTML"""
        import re

        # Try to find JSX content in return statement
        jsx_match = re.search(r'return\s*\(\s*([\s\S]*?)\s*\)\s*;?\s*}', code)
        if jsx_match:
            jsx = jsx_match.group(1)
        else:
            # Check if it's already HTML
            if '<' in code and '>' in code:
                jsx = code
            else:
                jsx = f'<pre class="p-4 bg-gray-100 rounded text-sm overflow-auto"><code>{code[:1000]}</code></pre>'

        # Convert JSX to HTML
        html = jsx
        html = re.sub(r'className=', 'class=', html)
        html = re.sub(r'\{/\*.*?\*/\}', '', html, flags=re.DOTALL)  # Remove JSX comments

        # Handle simple JS expressions (convert {variable} to placeholder)
        html = re.sub(r'\{([^{}]+)\}', r'[\1]', html)

        return html

    def to_base64(self, image_bytes: bytes) -> str:
        """Convert image bytes to base64 string"""
        return base64.b64encode(image_bytes).decode('utf-8')

    def to_data_url(self, image_bytes: bytes) -> str:
        """Convert image bytes to data URL"""
        b64 = self.to_base64(image_bytes)
        return f"data:image/png;base64,{b64}"

    async def close(self):
        """Clean up resources"""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()


# Singleton instance
_image_generator = None

def get_image_generator() -> ImageGenerator:
    global _image_generator
    if _image_generator is None:
        _image_generator = ImageGenerator()
    return _image_generator
