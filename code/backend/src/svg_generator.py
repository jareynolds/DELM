"""
SVG generation for icons, symbols, and simple graphics
"""
import re
from typing import Dict, Any, List

class SVGGenerator:
    def __init__(self):
        self.icon_templates = self._load_icon_templates()

    def _load_icon_templates(self) -> Dict[str, str]:
        """Load built-in icon templates"""
        return {
            # UI Icons
            "home": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>''',
            "user": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>''',
            "settings": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>''',
            "search": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>''',
            "menu": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>''',
            "close": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>''',
            "check": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>''',
            "plus": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>''',
            "minus": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/>''',
            "arrow-right": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/>''',
            "arrow-left": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>''',
            "arrow-up": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>''',
            "arrow-down": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>''',
            "heart": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>''',
            "star": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>''',
            "mail": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>''',
            "phone": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>''',
            "camera": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/>''',
            "download": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>''',
            "upload": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/>''',
            "trash": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>''',
            "edit": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>''',
            "copy": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>''',
            "share": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/>''',
            "lock": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>''',
            "unlock": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 11V7a4 4 0 118 0m-4 8v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2z"/>''',
            "eye": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>''',
            "eye-off": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>''',
            "bell": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>''',
            "calendar": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>''',
            "clock": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>''',
            "folder": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/>''',
            "file": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>''',
            "image": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>''',
            "video": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>''',
            "music": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>''',
            "code": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>''',
            "terminal": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>''',
            "database": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"/>''',
            "cloud": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"/>''',
            "sun": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>''',
            "moon": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>''',
            "refresh": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>''',
            "filter": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/>''',
            "sort": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4h13M3 8h9m-9 4h6m4 0l4-4m0 0l4 4m-4-4v12"/>''',
            "chart": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>''',
            "globe": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>''',
            "link": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/>''',
            "wifi": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.14 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0"/>''',
            "bluetooth": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 12l6-6v12l-6-6zm0 0l6 6m0-12l6 6-6 6"/>''',
            "battery": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7h14a2 2 0 012 2v6a2 2 0 01-2 2H3a2 2 0 01-2-2V9a2 2 0 012-2zm18 3v4"/>''',
            "zap": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>''',
            "gift": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"/>''',
            "shopping-cart": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>''',
            "tag": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/>''',
            "bookmark": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/>''',
            "flag": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9"/>''',
            "map": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>''',
            "navigation": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>''',
            "compass": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16.24 7.76l-2.12 6.36-6.36 2.12 2.12-6.36 6.36-2.12z"/>''',
            "layers": '''<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>''',
        }

    def generate_icon(
        self,
        name: str,
        size: int = 24,
        color: str = "currentColor",
        stroke_width: float = 2
    ) -> str:
        """Generate an SVG icon by name"""

        icon_path = self.icon_templates.get(name.lower())

        if icon_path:
            # Update stroke width in the path
            icon_path = re.sub(r'stroke-width="[^"]*"', f'stroke-width="{stroke_width}"', icon_path)

            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round">
{icon_path}
</svg>'''
        else:
            # Return a placeholder
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}">
<rect x="3" y="3" width="18" height="18" rx="2" stroke-width="{stroke_width}"/>
<text x="12" y="16" text-anchor="middle" font-size="8" fill="{color}">?</text>
</svg>'''

    def generate_symbol(
        self,
        symbol_type: str,
        size: int = 64,
        primary_color: str = "#3b82f6",
        secondary_color: str = "#60a5fa"
    ) -> str:
        """Generate decorative symbols and shapes"""

        if symbol_type == "circle":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="circleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<circle cx="50" cy="50" r="45" fill="url(#circleGrad)"/>
</svg>'''

        elif symbol_type == "hexagon":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="hexGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="50,5 95,27.5 95,72.5 50,95 5,72.5 5,27.5" fill="url(#hexGrad)"/>
</svg>'''

        elif symbol_type == "star":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="starGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="50,5 61,39 97,39 68,61 79,95 50,73 21,95 32,61 3,39 39,39" fill="url(#starGrad)"/>
</svg>'''

        elif symbol_type == "diamond":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="diamondGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="50,5 95,50 50,95 5,50" fill="url(#diamondGrad)"/>
</svg>'''

        elif symbol_type == "triangle":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="triGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="50,10 90,90 10,90" fill="url(#triGrad)"/>
</svg>'''

        elif symbol_type == "ring":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<circle cx="50" cy="50" r="40" fill="none" stroke="url(#ringGrad)" stroke-width="8"/>
</svg>'''

        elif symbol_type == "badge":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<path d="M50 5 L61 39 L97 39 L68 61 L79 95 L50 73 L21 95 L32 61 L3 39 L39 39 Z" fill="{primary_color}"/>
<circle cx="50" cy="50" r="20" fill="{secondary_color}"/>
</svg>'''

        elif symbol_type == "arrow":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="arrowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="10,40 60,40 60,20 90,50 60,80 60,60 10,60" fill="url(#arrowGrad)"/>
</svg>'''

        elif symbol_type == "chevron":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="chevGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="20,10 50,50 20,90 40,90 70,50 40,10" fill="url(#chevGrad)"/>
</svg>'''

        elif symbol_type == "divider":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="divGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:0" />
        <stop offset="50%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:0" />
    </linearGradient>
</defs>
<rect x="5" y="45" width="90" height="10" rx="5" fill="url(#divGrad)"/>
</svg>'''

        elif symbol_type == "dots":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<circle cx="25" cy="50" r="8" fill="{primary_color}"/>
<circle cx="50" cy="50" r="8" fill="{secondary_color}"/>
<circle cx="75" cy="50" r="8" fill="{primary_color}"/>
</svg>'''

        elif symbol_type == "wave":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<path d="M0,50 Q25,20 50,50 T100,50 V100 H0 Z" fill="url(#waveGrad)"/>
</svg>'''

        elif symbol_type == "shield":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<path d="M50,5 L90,20 L90,50 Q90,85 50,95 Q10,85 10,50 L10,20 Z" fill="url(#shieldGrad)"/>
</svg>'''

        elif symbol_type == "heart":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="heartGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<path d="M50,88 C20,60 5,40 5,25 C5,10 20,5 35,15 C45,22 50,30 50,30 C50,30 55,22 65,15 C80,5 95,10 95,25 C95,40 80,60 50,88 Z" fill="url(#heartGrad)"/>
</svg>'''

        elif symbol_type == "lightning":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="lightGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="60,5 25,50 45,50 40,95 75,45 55,45" fill="url(#lightGrad)"/>
</svg>'''

        elif symbol_type == "cross":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="crossGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<path d="M40,10 H60 V40 H90 V60 H60 V90 H40 V60 H10 V40 H40 Z" fill="url(#crossGrad)"/>
</svg>'''

        elif symbol_type == "octagon":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="octGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="30,5 70,5 95,30 95,70 70,95 30,95 5,70 5,30" fill="url(#octGrad)"/>
</svg>'''

        elif symbol_type == "pentagon":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="pentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="50,5 95,38 77,90 23,90 5,38" fill="url(#pentGrad)"/>
</svg>'''

        elif symbol_type == "burst":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="burstGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<polygon points="50,0 58,35 90,15 65,42 100,50 65,58 90,85 58,65 50,100 42,65 10,85 35,58 0,50 35,42 10,15 42,35" fill="url(#burstGrad)"/>
</svg>'''

        elif symbol_type == "ribbon":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="ribGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<path d="M0,35 L15,50 L0,65 L25,65 L25,35 Z" fill="{secondary_color}"/>
<rect x="20" y="35" width="60" height="30" fill="url(#ribGrad)"/>
<path d="M100,35 L85,50 L100,65 L75,65 L75,35 Z" fill="{secondary_color}"/>
</svg>'''

        elif symbol_type == "square":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<defs>
    <linearGradient id="sqGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
</defs>
<rect x="10" y="10" width="80" height="80" rx="8" fill="url(#sqGrad)"/>
</svg>'''

        else:
            # List available types
            available = ["circle", "hexagon", "star", "diamond", "triangle", "ring", "badge",
                        "arrow", "chevron", "divider", "dots", "wave", "shield", "heart",
                        "lightning", "cross", "octagon", "pentagon", "burst", "ribbon", "square"]
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<rect x="5" y="5" width="90" height="90" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
<text x="50" y="45" text-anchor="middle" font-family="sans-serif" font-size="8" fill="#6b7280">Unknown type:</text>
<text x="50" y="58" text-anchor="middle" font-family="sans-serif" font-size="7" fill="#9ca3af">{symbol_type}</text>
</svg>'''

    def generate_logo_placeholder(
        self,
        text: str,
        size: int = 128,
        bg_color: str = "#3b82f6",
        text_color: str = "#ffffff",
        shape: str = "circle"
    ) -> str:
        """Generate a simple logo placeholder with initials"""

        # Get initials
        words = text.split()
        initials = ''.join([w[0].upper() for w in words[:2]])

        if shape == "circle":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<circle cx="50" cy="50" r="45" fill="{bg_color}"/>
<text x="50" y="50" text-anchor="middle" dominant-baseline="central" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="{text_color}">{initials}</text>
</svg>'''

        elif shape == "rounded":
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<rect x="5" y="5" width="90" height="90" rx="20" fill="{bg_color}"/>
<text x="50" y="50" text-anchor="middle" dominant-baseline="central" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="{text_color}">{initials}</text>
</svg>'''

        else:  # square
            return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
<rect x="5" y="5" width="90" height="90" fill="{bg_color}"/>
<text x="50" y="50" text-anchor="middle" dominant-baseline="central" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="{text_color}">{initials}</text>
</svg>'''

    def list_available_icons(self) -> List[str]:
        """Return list of available icon names"""
        return sorted(self.icon_templates.keys())


# Singleton
_svg_generator = None

def get_svg_generator() -> SVGGenerator:
    global _svg_generator
    if _svg_generator is None:
        _svg_generator = SVGGenerator()
    return _svg_generator
