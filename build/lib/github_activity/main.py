import requests as req
import json, argparse
from rich import print as rich_print
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


class GitHubManager:
    def __init__(self, user_name: str):
        url_api_github = f"https://api.github.com/users/{user_name}/events"
        self.user_name = user_name
        self.url = url_api_github
        self.request_status = 0

    def get_user_info(self):
        try:
            res = req.get(self.url)
            self.request_status = res.status_code
            data = res.json()
            # print(json.dumps(data, indent=4))
            self.beutifyData(data)
        except ValueError as e:
            print(f"We have a error...{e}")

    def beutifyData(self, data) -> None:
        self.setPrints(data)

    def setPrints(self, latest_events) -> None:
        if self.request_status == 200:

            user_title = Text(f"Latest events for {self.user_name}", style="bold red")

            # table structure
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Event Type", style="dim", width=15)
            table.add_column("Description", style="bold")

            # map events    #
            for event in latest_events:
                match event["type"]:
                    case "IssueCommentEvent":
                        description = f":speech_balloon: Commented on issue [bold]{event['payload']['issue']['number']}[/bold]"
                    case "PushEvent":
                        description = (
                            f":rocket: Pushed to [bold]{event['repo']['name']}[/bold]"
                        )
                    case "IssuesEvent":
                        description = f":bug: Created issue [bold]{event['payload']['issue']['number']}[/bold]"
                    case "WatchEvent":
                        description = (
                            f":star: Starred [bold]{event['repo']['name']}[/bold]"
                        )
                    case "PullRequestEvent":
                        description = f":sparkles: Created pull request [bold]{event['payload']['pull_request']['number']}[/bold]"
                    case "PullRequestReviewEvent":
                        description = f":eyes: Reviewed pull request [bold]{event['payload']['pull_request']['number']}[/bold]"
                    case "PullRequestReviewCommentEvent":
                        description = f":speech_balloon: Commented on pull request [bold]{event['payload']['pull_request']['number']}[/bold]"
                    case "CreateEvent":
                        description = f":new: Created {event['payload']['ref_type']} [bold]{event['payload']['ref']}[/bold]"
                    case _:
                        description = f":grey_question: {event['type']}"

                # Add data to table
                table.add_row(event["type"], description)

            # display table
            rich_print(Panel(table, title=user_title, expand=False))
        else:
            # Print error message in case of request failure
            error_message = Text(
                f"Error fetching events for {self.user_name}: {self.request_status}",
                style="bold red",
            )
            rich_print(Panel(error_message, expand=False))


def arg_setup():
    # setup to recibe arguments
    parser = argparse.ArgumentParser(description="Welcome to github activity CLI")

    parser.add_argument("userName", type=str, help="UserName of the user")
    arg = parser.parse_args()
    return arg.userName


def main():
    print("entro")
    core = GitHubManager(arg_setup())
    core.get_user_info()


if __name__ == "__main__":
    main()
