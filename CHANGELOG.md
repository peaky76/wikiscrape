# Changelog

## 0.5.6 (2023-09-25)

#### Fixes

- handle no headers in `Wikitable`
- handle empty headers in `Wikitable`

#### Refactorings

- `Wikitable.headers` intermediate vars

## 0.5.5 (2023-09-24)

#### Refactorings

- make `Wikipage` and `LinkedText` hashable

## 0.5.4 (2023-09-13)

#### Fixes

- only remove square bracketed footnotes
- handle blanks in `Wikitable.data`

#### Refactorings

- use content in `LinkedText.link` property instead of empty object

#### Others

- ruff ignore E731
- add test for `Wikitable` handling ampersands

## 0.5.3 (2023-09-03)

#### Fixes

- remove footnotes from `Wikitable.data`

#### Refactorings

- `remove_footnotes` helper

## 0.5.2 (2023-09-03)

#### Fixes

- handle `NavigableString` case in `LinkedText`

#### Refactorings

- typing fix in `Infobox.data`
- typing fix in `Wikipage.exists`

## 0.5.1 (2023-08-28)

#### Fixes

- filter out null first elements in `Wikitable.headers`

#### Others

- ruff ignore E501

## 0.5.0 (2023-08-28)

#### New Features

- `Wikipage.from_url`

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
