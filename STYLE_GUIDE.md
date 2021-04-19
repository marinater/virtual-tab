# Repository Style Guide

## Python Code

- All code in pull requests will be automatically formatted using a Github Action written by Peter Evans [in this blog post](https://peterevans.dev/posts/github-actions-how-to-automate-code-formatting-in-pull-requests/).
- It is recommended, that you format code locally using Black as well, though not required.

## Naming Scheme

### Files and Folders

- In general, files and folders should be all lowercase and use underscores to separate words.

### Python Variable Naming

- All constant variables should be in all capitals
- All other variables should use lower camel case. Ex: `fooBar = 'Foo Bar'`
- All classes should use upper camel case. Ex: `FooBar = 'Foo Bar'`
- Class fields should be prefixed with an underscore if they are not intended for public use

