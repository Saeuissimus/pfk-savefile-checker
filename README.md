# Pathfinder: Kingmaker savefile checker

This script is just an easy way to check the health of your Pathfinder: Kingmaker savefile. In my playthrough I've been running into  savefile corruption occasionally.

This script condenses my current knowledge about the subject — which, by the way, amounts to practically nothing.

## Usage

You need to install the dependencies specified in the Pipfile before running. I suggest using [pipenv](https://github.com/pypa/pipenv) like this:

```
$ pipenv install
$ pipenv run ./corrupt-save-checker.py <savefile path>
```

## FAQ

Q: It says my savefile is corrupted, am I in trouble?

A: Well, personally I've only ever seen "subsaves" for specific locations corrupt. For example, I've had Old Sycamore corrupt a couple of times in my campaign. If you never happen to revisit the affected locations, then I'd expect you to not be impacted by this problem. If you do visit one of the affected locations however, I'd expect there to be a crash back to the main menu while loading the area. Depending on where this manifests, it may be crippling to your campaign.

Q: It says it found an unknown file extension or a file with a strange mime type in my savefile. What is it?

A: It's highly probable that this is a normal, healthy file that I never saw in my own savefiles. Consider opening a pull request to add this information to the script!

## TODO

- Map known filenames to locations?
