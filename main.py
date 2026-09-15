#!/usr/bin/env python3
"""Interactive CLI for the Immunology PI Agent."""

import os
import sys
from pathlib import Path
from agent.pi_agent import ImmunologyPIAgent
from dotenv import load_dotenv


def print_banner():
    """Print the agent banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║          IMMUNOLOGY PI AGENT - Inflammation Focus            ║
    ║                                                              ║
    ║  Analysis | Hypothesis Validation | Design Critique          ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_help():
    """Print help information."""
    help_text = """
    Commands:
    ---------
    analyze <filepath>     : Analyze a CSV file or image
    ask <question>         : Ask a question about your research
    new                    : Start a new conversation (reset history)
    history                : Show conversation history
    help                   : Show this help message
    exit / quit            : Exit the agent
    
    Examples:
    ---------
    > analyze ./data/cytokines.csv
    > analyze ./figures/flow_cytometry.png
    > ask Does my data support a Th17 response?
    > ask What controls am I missing?
    """
    print(help_text)


def handle_analyze_command(agent: ImmunologyPIAgent, filepath: str) -> None:
    """Handle the analyze command.
    
    Args:
        agent: The PI agent instance
        filepath: Path to the file to analyze
    """
    path = Path(filepath)
    
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        return
    
    # Determine file type and prompt
    if path.suffix.lower() == ".csv":
        prompt = input("What would you like me to analyze in this data? > ")
        print(f"\n📊 Analyzing CSV data...\n")
        response = agent.analyze_with_csv(prompt, filepath)
    
    elif path.suffix.lower() in [".png", ".jpg", ".jpeg", ".gif", ".webp"]:
        prompt = input("What would you like me to analyze in this image? > ")
        print(f"\n🖼️  Analyzing image...\n")
        response = agent.analyze_with_image(prompt, filepath)
    
    else:
        print(f"❌ Unsupported file type: {path.suffix}")
        print("   Supported: .csv, .png, .jpg, .jpeg, .gif, .webp")
        return
    
    print(response)
    print("\n" + "="*70 + "\n")


def main():
    """Main interactive loop for the PI agent."""
    load_dotenv()
    
    try:
        agent = ImmunologyPIAgent()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nPlease set the ANTHROPIC_API_KEY environment variable:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    print_banner()
    print("Type 'help' for commands or start asking questions.\n")
    
    while True:
        try:
            user_input = input("You > ").strip()
            
            if not user_input:
                continue
            
            # Parse commands
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye!")
                break
            
            elif user_input.lower() == "help":
                print_help()
            
            elif user_input.lower() == "new":
                agent.reset_conversation()
                print("✅ Conversation history cleared.\n")
            
            elif user_input.lower() == "history":
                history = agent.get_conversation_history()
                if not history:
                    print("No conversation history yet.\n")
                else:
                    print("\nConversation History:")
                    print("="*70)
                    for i, msg in enumerate(history, 1):
                        role = msg["role"].upper()
                        content = msg["content"]
                        if isinstance(content, str):
                            content = content[:200] + "..." if len(content) > 200 else content
                        print(f"{i}. {role}: {content}")
                    print("\n")
            
            elif user_input.lower().startswith("analyze "):
                filepath = user_input[8:].strip()
                handle_analyze_command(agent, filepath)
            
            elif user_input.lower().startswith("ask "):
                question = user_input[4:].strip()
                print(f"\n🤔 Thinking...\n")
                response = agent.ask(question)
                print(f"PI Agent > {response}")
                print("\n" + "="*70 + "\n")
            
            else:
                # Default: treat as a question
                print(f"\n🤔 Thinking...\n")
                response = agent.ask(user_input)
                print(f"PI Agent > {response}")
                print("\n" + "="*70 + "\n")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()
