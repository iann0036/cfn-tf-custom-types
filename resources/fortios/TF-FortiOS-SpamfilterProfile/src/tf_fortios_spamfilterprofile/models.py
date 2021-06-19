# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Comment: Optional[str]
    External: Optional[str]
    FlowBased: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Options: Optional[str]
    ReplacemsgGroup: Optional[str]
    SpamBwlTable: Optional[float]
    SpamBwordTable: Optional[float]
    SpamBwordThreshold: Optional[float]
    SpamFiltering: Optional[str]
    SpamIptrustTable: Optional[float]
    SpamLog: Optional[str]
    SpamLogFortiguardResponse: Optional[str]
    SpamMheaderTable: Optional[float]
    SpamRblTable: Optional[float]
    Vdomparam: Optional[str]
    Gmail: Optional[Sequence["_GmailDefinition"]]
    Imap: Optional[Sequence["_ImapDefinition"]]
    Mapi: Optional[Sequence["_MapiDefinition"]]
    MsnHotmail: Optional[Sequence["_MsnHotmailDefinition"]]
    Pop3: Optional[Sequence["_Pop3Definition"]]
    Smtp: Optional[Sequence["_SmtpDefinition"]]
    YahooMail: Optional[Sequence["_YahooMailDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Comment=json_data.get("Comment"),
            External=json_data.get("External"),
            FlowBased=json_data.get("FlowBased"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            SpamBwlTable=json_data.get("SpamBwlTable"),
            SpamBwordTable=json_data.get("SpamBwordTable"),
            SpamBwordThreshold=json_data.get("SpamBwordThreshold"),
            SpamFiltering=json_data.get("SpamFiltering"),
            SpamIptrustTable=json_data.get("SpamIptrustTable"),
            SpamLog=json_data.get("SpamLog"),
            SpamLogFortiguardResponse=json_data.get("SpamLogFortiguardResponse"),
            SpamMheaderTable=json_data.get("SpamMheaderTable"),
            SpamRblTable=json_data.get("SpamRblTable"),
            Vdomparam=json_data.get("Vdomparam"),
            Gmail=deserialize_list(json_data.get("Gmail"), GmailDefinition),
            Imap=deserialize_list(json_data.get("Imap"), ImapDefinition),
            Mapi=deserialize_list(json_data.get("Mapi"), MapiDefinition),
            MsnHotmail=deserialize_list(json_data.get("MsnHotmail"), MsnHotmailDefinition),
            Pop3=deserialize_list(json_data.get("Pop3"), Pop3Definition),
            Smtp=deserialize_list(json_data.get("Smtp"), SmtpDefinition),
            YahooMail=deserialize_list(json_data.get("YahooMail"), YahooMailDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GmailDefinition(BaseModel):
    Log: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GmailDefinition"]:
        if not json_data:
            return None
        return cls(
            Log=json_data.get("Log"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GmailDefinition = GmailDefinition


@dataclass
class ImapDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    TagMsg: Optional[str]
    TagType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImapDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            TagMsg=json_data.get("TagMsg"),
            TagType=json_data.get("TagType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImapDefinition = ImapDefinition


@dataclass
class MapiDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapiDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapiDefinition = MapiDefinition


@dataclass
class MsnHotmailDefinition(BaseModel):
    Log: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MsnHotmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MsnHotmailDefinition"]:
        if not json_data:
            return None
        return cls(
            Log=json_data.get("Log"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MsnHotmailDefinition = MsnHotmailDefinition


@dataclass
class Pop3Definition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    TagMsg: Optional[str]
    TagType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Pop3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pop3Definition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            TagMsg=json_data.get("TagMsg"),
            TagType=json_data.get("TagType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pop3Definition = Pop3Definition


@dataclass
class SmtpDefinition(BaseModel):
    Action: Optional[str]
    Hdrip: Optional[str]
    LocalOverride: Optional[str]
    Log: Optional[str]
    TagMsg: Optional[str]
    TagType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Hdrip=json_data.get("Hdrip"),
            LocalOverride=json_data.get("LocalOverride"),
            Log=json_data.get("Log"),
            TagMsg=json_data.get("TagMsg"),
            TagType=json_data.get("TagType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpDefinition = SmtpDefinition


@dataclass
class YahooMailDefinition(BaseModel):
    Log: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_YahooMailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YahooMailDefinition"]:
        if not json_data:
            return None
        return cls(
            Log=json_data.get("Log"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YahooMailDefinition = YahooMailDefinition


