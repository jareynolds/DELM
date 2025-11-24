"""
Small Language Model interface optimized for Apple Silicon using MLX
"""
from mlx_lm import load, generate
import yaml
from typing import Optional

class DesignLLM:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        model_name = self.config['model']['name']
        print(f"Loading model: {model_name}")

        self.model, self.tokenizer = load(model_name)
        self.max_tokens = self.config['model']['max_tokens']

        print("Model loaded successfully on Apple Silicon")

    def _format_prompt(self, user_message: str, system_message: Optional[str] = None) -> str:
        """Format prompt using the model's chat template"""
        messages = []

        if system_message:
            messages.append({"role": "system", "content": system_message})

        messages.append({"role": "user", "content": user_message})

        # Use the tokenizer's chat template if available
        if hasattr(self.tokenizer, 'apply_chat_template'):
            prompt = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
        else:
            # Fallback for models without chat template
            if system_message:
                prompt = f"<|system|>\n{system_message}<|end|>\n<|user|>\n{user_message}<|end|>\n<|assistant|>\n"
            else:
                prompt = f"<|user|>\n{user_message}<|end|>\n<|assistant|>\n"

        return prompt

    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """Generate text from prompt"""

        formatted_prompt = self._format_prompt(prompt, system_prompt)

        response = generate(
            self.model,
            self.tokenizer,
            prompt=formatted_prompt,
            max_tokens=max_tokens or self.max_tokens,
            verbose=False
        )

        return response

    def generate_ui_component(
        self,
        description: str,
        context: str,
        component_type: str = "react"
    ) -> str:
        """Generate a UI component based on description and RAG context"""

        system_prompt = f"""You are an expert React developer. Generate complete, working UI components using React, TypeScript, and Tailwind CSS.

IMPORTANT: Output ONLY valid TypeScript/React code. No explanations, no markdown, just the code.

Reference these design patterns:
{context}

Requirements:
- Use TypeScript with proper interfaces
- Use Tailwind CSS for all styling
- Include all necessary imports
- Make components fully functional"""

        user_prompt = f"Create this React component: {description}\n\nOutput only the complete TypeScript code:"

        return self.generate(user_prompt, system_prompt=system_prompt)

    def generate_styles(
        self,
        description: str,
        context: str
    ) -> str:
        """Generate CSS/Tailwind styles"""

        system_prompt = f"""You are an expert UI designer. Generate CSS styles, Tailwind configurations, or design tokens.

IMPORTANT: Output ONLY valid code. No explanations, no markdown.

Reference patterns:
{context}"""

        user_prompt = f"Create these styles: {description}\n\nOutput only the code:"

        return self.generate(user_prompt, system_prompt=system_prompt)

    def generate_layout(
        self,
        description: str,
        context: str
    ) -> str:
        """Generate page layouts"""

        system_prompt = f"""You are an expert React developer. Generate page layouts using React and Tailwind CSS.

IMPORTANT: Output ONLY valid TypeScript/React code. No explanations, no markdown.

Reference patterns:
{context}"""

        user_prompt = f"Create this layout: {description}\n\nOutput only the complete TypeScript code:"

        return self.generate(user_prompt, system_prompt=system_prompt)
