from modules import launch_utils

index_url = launch_utils.index_url
dir_repos = launch_utils.dir_repos

run = launch_utils.run
repo_dir = launch_utils.repo_dir

list_extensions = launch_utils.list_extensions
start = launch_utils.start

def main():
    launch_utils.startup_timer.record("initial startup")

    start()

if __name__ == "__main__":
    main()
