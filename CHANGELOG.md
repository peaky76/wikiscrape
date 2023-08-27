# Changelog

## 0.4.3 (2023-08-27)

#### Fixes

- tidy `Wikitable.headers`

## 0.4.2 (2023-08-27)

#### Fixes

- `Infobox.data` handles multiple elements
- `Wikitable.data` handles multiple elements

## 0.4.1 (2023-08-26)

#### Fixes

- exclude rows from `Infobox` data if no headers present

## 0.4.0 (2023-08-26)

#### New Features

- create `Infobox` class
- add `LinkedText.__repr__`

#### Others

- typing
- refactor `LinkedText` tests

## 0.3.0 (2023-08-24)

#### New Features

- create `LinkedText` class
- create `Wikitable` class

## 0.2.2 (2023-07-24)

#### Others

- add bs4 and requests types

## 0.2.1 (2023-05-20)

#### Others

- remove unneeded imports

## 0.2.0 (2023-05-20)

#### New Features

- `Wikipage.soup` property
- `Wikipage.text` property

#### Refactorings

- `Wikipage.derive_subject` method -> `.subject` property

#### Others

- add beautifulsoup4
- add requests-mock
- add requests
- add missing `Wikipage.__eq__` test

## 0.1.0 (2023-05-19)

#### New Features

- create `Markdown` class
- create `Wikipage` class
