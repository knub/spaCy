# coding: utf-8

from __future__ import unicode_literals

import pytest


@pytest.mark.parametrize('text', ["aujourd'hui", "Aujourd'hui", "prud'hommes",
                                  "prud’hommal"])
def test_tokenizer_infix_exceptions(fr_tokenizer, text):
    tokens = fr_tokenizer(text)
    assert len(tokens) == 1


@pytest.mark.parametrize('text,lemma', [("janv.", "janvier"),
                                        ("juill.", "juillet"),
                                        ("sept.", "septembre")])
def test_tokenizer_handles_abbr(fr_tokenizer, text, lemma):
    tokens = fr_tokenizer(text)
    assert len(tokens) == 1
    assert tokens[0].lemma_ == lemma


def test_tokenizer_handles_exc_in_text(fr_tokenizer):
    text = "Je suis allé au mois de janv. aux prud’hommes."
    tokens = fr_tokenizer(text)
    assert len(tokens) == 10
    assert tokens[6].text == "janv."
    assert tokens[6].lemma_ == "janvier"
    assert tokens[8].text == "prud’hommes"
