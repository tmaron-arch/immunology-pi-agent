"""Core PI Agent implementation for inflammation immunology research."""

import os
from anthropic import Anthropic
from typing import Optional
import base64
from pathlib import Path


class ImmunologyPIAgent:
    """Principal Investigator agent for inflammation immunology research."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PI agent with Claude API.
        
        Args:
            api_key: Anthropic API key. If None, uses ANTHROPIC_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not provided and not found in environment"
            )
        
        self.client = Anthropic(api_key=self.api_key)
        self.conversation_history = []
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        """Load the system prompt for the PI agent."""
        prompt_path = Path(__file__).parent.parent / "prompts" / "system_prompts.md"
        if prompt_path.exists():
            with open(prompt_path, "r") as f:
                return f.read()
        return "You are an experienced Principal Investigator in inflammation immunology."

    def encode_image(self, image_path: str) -> tuple[str, str]:
        """Encode image to base64 for Claude API.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Tuple of (base64_data, media_type)
        """
        path = Path(image_path)
        
        # Determine media type
        suffix = path.suffix.lower()
        media_types = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }
        
        media_type = media_types.get(suffix, "image/jpeg")
        
        with open(path, "rb") as f:
            image_data = base64.standard_b64encode(f.read()).decode("utf-8")
        
        return image_data, media_type

    def analyze_with_image(self, prompt: str, image_path: str) -> str:
        """Analyze data with an image (flow cytometry, microscopy, etc.).
        
        Args:
            prompt: The analysis prompt/question
            image_path: Path to the image file
            
        Returns:
            PI's analysis and critique
        """
        image_data, media_type = self.encode_image(image_path)
        
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": prompt
                }
            ],
        })
        
        return self._get_response()

    def analyze_with_csv(self, prompt: str, csv_path: str) -> str:
        """Analyze experimental data from CSV file.
        
        Args:
            prompt: The analysis prompt/question
            csv_path: Path to the CSV file
            
        Returns:
            PI's analysis and critique
        """
        try:
            import pandas as pd
            df = pd.read_csv(csv_path)
            csv_content = f"CSV Data:\n{df.to_string()}\n\nData shape: {df.shape}\n"
        except Exception as e:
            csv_content = f"Error reading CSV: {str(e)}"
        
        full_prompt = f"{csv_content}\n\nQuestion: {prompt}"
        
        self.conversation_history.append({
            "role": "user",
            "content": full_prompt
        })
        
        return self._get_response()

    def ask(self, prompt: str) -> str:
        """Ask the PI agent a question in natural language.
        
        Args:
            prompt: The question or request
            
        Returns:
            PI's response
        """
        self.conversation_history.append({
            "role": "user",
            "content": prompt
        })
        
        return self._get_response()

    def _get_response(self) -> str:
        """Get response from Claude API.
        
        Returns:
            The PI agent's response
        """
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            system=self.system_prompt,
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message

    def get_conversation_history(self) -> list:
        """Get the full conversation history.
        
        Returns:
            List of conversation turns
        """
        return self.conversation_history

    def reset_conversation(self):
        """Reset the conversation history for a new analysis."""
        self.conversation_history = []
