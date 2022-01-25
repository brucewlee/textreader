<img alt="cc-by-nc-sa-4.0" src="https://img.shields.io/badge/License-cc--by--nc--sa--4.0-critical"></a>
[![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)
<a href="https://pypi.org/project/textreader"><img alt="PyPI" src="https://img.shields.io/badge/pypi-supported-yellow"></a>
<img alt="textreader" src="https://img.shields.io/badge/textreader-v.1.1.6-informational"></a>
<img alt="Dev Status" src="https://img.shields.io/badge/Status-Stable-success"></a>

# TextReader

TextReader is a research-based library to calculate readability statistics from an English text input. It is an easy and proven method to see readability and reading time.

## To Note
This library uses recalibrated versions of the below readability formulas (by default). Recalibration was made for equation to output US-based school grade (K1-12). To use original versions, see [Usage](#Usage)

Research paper is currently under peer-review.

## Usage

```python
>>> import textreader

>>> input_text = 
    "Here we go again. We were all standing in line waiting for breakfast when one of the caseworkers came in and taptap-tapped down the line. Uh-oh, this meant bad news, either they’d found a foster home for somebody or somebody was about to get paddled. All the kids watched the woman as she moved along the line, her high-heeled shoes sounding like little fire-crackers going off on the wooden floor.Shoot! She stopped at me and said, “Are you Buddy Caldwell?”I said, “It’s Bud, not Buddy, ma’am.”She put her hand on my shoulder and took me out of the line. Then she pulled Jerry, one of the littler boys, over."

>>> TextReader = textreader.request(input_text)


"""
- below equations are recalibrated to output US-based school grade (K1-12) for easy use
- pass in adjusted = False to use original formulas
"""
>>> print(TextReader.flesch_kincaid_grade_level()) #or .FKGL()
>>> print(TextReader.fog_index()) #or .FOGI()
>>> print(TextReader.smog_index())) #or .SMOG()
>>> print(TextReader.coleman_liau_index()) #or .COLE()
>>> print(TextReader.automated_readability_index()) #or .AUTO()


"""
- pass in speed = slow for slow reader 
- speed = fast for fast readers
- speed = average for general uses (default)
"""
>>> print(TextReader.read_time()) #or .RT()
```

## Install

### Install using pip
```shell
pip install textreader
```