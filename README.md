# GithubTd

Program for automatically collecting GitHub trending projects

## Usage

### collect
Use ```collect()``` to collect Github trending
```python
class GithubTd:
    
    def __init__(self):
        ...
    
    def collect(self, language, since='daily'):
        # language: python | java | Go ...
        # since: daily | weekly | monthly
        ...

gt = GithubTd()
gt.collect('Go', 'daily')
```
After the program runs, it will generate a Go_GithubTrending.json file
```json lines
{
  "ollama": {
        "desc": "Get up and running with Llama 3.3, Mistral, Gemma 2, and other large language models.",
        "info": {
            "language": "go",
            "stars_num": "102,214",
            "forks_num": "8,152",
            "today_stars_num": "335 stars today"
        }
    },
    "terraformer": {
        "desc": "CLI tool to generate terraform files from existing infrastructure (reverse Terraform). Infrastructure to Code",
        "info": {
            "language": "go",
            "stars_num": "12,815",
            "forks_num": "1,664",
            "today_stars_num": "17 stars today"
        }
    },
    "...": {"...":  "..."},
}
```

### batch_collect
Use ```batch_collect()``` to collect Github trending
```python
class GithubTd:
    
    def __init__(self):
        ...
    
    def batch_collect(self, language_list, since='daily'):
        # language_list: ['C++', 'java', 'python', ...]
        # since: daily | weekly | monthly
        ...

gt = GithubTd()
gt.batch_collect(language_list=['C++', 'java', 'python'])
```
After the program runs, it will generate three json file