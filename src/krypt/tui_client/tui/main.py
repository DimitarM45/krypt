import asyncio
import base64
from typing import Optional
import aiohttp

from pathlib import Path

from argparse import ArgumentParser, Namespace

from pwdlib import PasswordHash
from rich.text import Text
from rich.prompt import Prompt
from rich.console import Console

from terminaltexteffects.effects.effect_decrypt import Decrypt

from krypt.services.abstract_crypto_service import AbstractCryptoService
from krypt.services.crypto_service import CryptoService
from krypt.services.models.crypto_key_pair import CryptoKeyPair


async def handle_login() -> Optional[str]:
    username: str = Prompt.ask(
        "[yellow bold underline]username[/yellow bold underline]"
    )
    password: str = Prompt.ask(
        "[yellow bold underline]password[/yellow bold underline]", password=True
    )

    async with aiohttp.ClientSession() as session:
        async with session.post(
            AUTH_SERVER_URL + "/token",
            data={"username": username, "password": password},
        ) as response:
            if response.status == 201:
                return (await response.json())["access_token"]
            else:
                return None


async def handle_register() -> bool:
    first_name: str = Prompt.ask(
        "[yellow bold underline]first name[/yellow bold underline]"
    )
    last_name: str = Prompt.ask(
        "[yellow bold underline]last name[/yellow bold underline]"
    )
    username: str = Prompt.ask(
        "[yellow bold underline]username[/yellow bold underline]"
    )
    email: str = Prompt.ask("[yellow bold underline]email[/yellow bold underline]")
    password: str = Prompt.ask(
        "[yellow bold underline]password[/yellow bold underline]", password=True
    )

    crypto_service: AbstractCryptoService = CryptoService(PasswordHash.recommended())

    key_pair: CryptoKeyPair = crypto_service.generate_key_pair()

    async with aiohttp.ClientSession() as session:
        async with session.post(
            AUTH_SERVER_URL + "/register",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "password": password,
                "public_message_key": base64.b64encode(key_pair.public_key).decode(),
            },
        ) as response:
            if response.status == 201:
                rich_console.print("[green bold]Success![/green bold]")

                return True
            else:
                rich_console.print(
                    "[red bold]A user with the same email/username already exists![/red bold]"
                )

                return False


def render_startup_animation(text: str) -> None:
    tui_startup_effect = Decrypt(text)
    tui_startup_effect.effect_config.typing_speed = 1000000
    tui_startup_effect.terminal_config.canvas_width = 0
    tui_startup_effect.terminal_config.canvas_height = 0

    with tui_startup_effect.terminal_output() as terminal:
        for frame in tui_startup_effect:
            terminal.print(frame)


async def run_auth_flow() -> Optional[str]:
    arg_parser: ArgumentParser = ArgumentParser()

    arg_parser.add_argument(
        "-na",
        "--no-animation",
        action="store_true",
        help="Prevent startup logo animation.",
    )

    args: Namespace = arg_parser.parse_args()

    krypt_startup_text = "krypt"

    krypt_startup_logo_path = Path("startup_logo.txt")

    if Path.exists(krypt_startup_logo_path):
        krypt_startup_text = Path.read_text(krypt_startup_logo_path)

    if not args.no_animation:
        render_startup_animation(krypt_startup_text)
    else:
        no_logo_text: Text = Text(krypt_startup_text, style="yellow")

        rich_console.print(no_logo_text)

    startup_action: str = Prompt.ask(
        "[bold underline purple](l)ogin[/bold underline purple] or [bold underline yellow](r)egister[/bold underline yellow]",
        default="l",
        choices=["l", "r", "login", "register"],
        show_choices=False,
        show_default=False,
    )

    if startup_action == "l" or startup_action == "login":
        return await handle_login()
    elif startup_action == "r" or startup_action == "register":
        if not await handle_register():
            return None

        rich_console.print("[green bold]Login:[/green bold]")

        return await handle_login()


async def run_websocket_client():
    pass


async def run_tui_app():
    pass


async def main():
    access_token: Optional[str] = await run_auth_flow()

    if not access_token:
        rich_console.print("[red bold]AUTHENTICATION FAILED[/red bold]")

        return

    

if __name__ == "__main__":
    AUTH_SERVER_URL = "http://localhost:8000/auth"
    rich_console: Console = Console()

    asyncio.run(main())
