import asyncio
from pathlib import Path
from argparse import ArgumentParser, Namespace
from rich.console import Console

from terminaltexteffects.effects.effect_decrypt import Decrypt


async def main():
    arg_parser: ArgumentParser = ArgumentParser()

    arg_parser.add_argument(
        "-nl", "--no-logo", action="store_true", help="Prevent startup logo animation."
    )

    args: Namespace = arg_parser.parse_args()

    krypt_startup_text = "krypt"

    krypt_startup_logo_path = Path("startup_logo.txt")

    if not args.no_logo and Path.exists(krypt_startup_logo_path):
        krypt_startup_text = Path.read_text(krypt_startup_logo_path)

    tui_startup_effect = Decrypt(krypt_startup_text)
    tui_startup_effect.effect_config.typing_speed = 10000
    tui_startup_effect.terminal_config.anchor_canvas = "nw"
    tui_startup_effect.terminal_config.canvas_width = 0
    tui_startup_effect.terminal_config.canvas_height = 0

    with tui_startup_effect.terminal_output() as terminal:
        for frame in tui_startup_effect:
            terminal.print(frame)

    console: Console = Console()

    console.input("[red]Login/Register: ")


if __name__ == "main":
    asyncio.run(main())
