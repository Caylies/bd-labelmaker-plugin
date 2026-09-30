# bd-labelmaker-plugin

Add extra buttons to your BallSpawnView without any code changes.

This project is a direct fork of bd-labelmaker and serves as a way to allow Plugin and bd-labelmaker to work together.

## Installation

Add the following lines to your `config/extra.toml` (create it if it doesn't exist):

```toml
[[ballsdex.packages]]
location = "git+https://github.com/Caylies/bd-labelmaker-plugin.git@1.0.0"
path = "labelmaker_app"
enabled = true

```

## Usage

To use, first add something in the Labels panel, then run `@botping reload labelmaker_app.package` (or use your prefix).

Subsequent spawns will have those buttons added.

Label responses support keywords, such as:

- `{user}` - Mentions the user who interacted with a button.
- `{collectible}` - The collectible name.
- `{collectibles}` - A plural version of `{collectible}`.
- `{ball}` - The countryball's name.
- `{rarity}` - The countryball's rarity.
- `{emoji}` - The countryball's emoji.
- `{discord}` - Your bot's Discord server invite link.

The **Despawn state** and **Caught state** sections in the panel control how the label will change after its ball despawns or is caught, respectively. It should be fairly self-explanatory.

**Caught state** also includes a section for whether the label will disable after being caught (enabled by default)

## Example

<img width="905" height="701" alt="image" src="https://github.com/user-attachments/assets/24dc4f2a-9a5a-4509-8e84-3a595aa8199f" />
