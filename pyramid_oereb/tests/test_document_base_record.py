# -*- coding: utf-8 -*-
import pytest
import datetime
from pyramid_oereb.lib.records.documents import DocumentBaseRecord


def test_get_fields():
    expected_fields = [
        'text_at_web',
        'law_status',
        'published_from'
    ]
    fields = DocumentBaseRecord.get_fields()
    assert fields == expected_fields


def test_mandatory_fields():
    with pytest.raises(TypeError):
        DocumentBaseRecord()


def test_init():
    record = DocumentBaseRecord("runningModifications", datetime.date(1985, 8, 29))
    assert isinstance(record.law_status, str)
    assert record.text_at_web is None
    assert isinstance(record.published_from, datetime.date)
