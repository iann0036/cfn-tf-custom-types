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
    Author: Optional[str]
    Created: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Modified: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Author=json_data.get("Author"),
            Created=json_data.get("Created"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Modified=json_data.get("Modified"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RulesDefinition(BaseModel):
    Name: Optional[str]
    Priority: Optional[float]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ActionsDefinition(BaseModel):
    CustomSeverity: Optional[str]
    FailBuild: Optional[bool]
    Mails: Optional[Sequence[str]]
    Webhooks: Optional[Sequence[str]]
    BlockDownload: Optional[Sequence["_BlockDownloadDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomSeverity=json_data.get("CustomSeverity"),
            FailBuild=json_data.get("FailBuild"),
            Mails=json_data.get("Mails"),
            Webhooks=json_data.get("Webhooks"),
            BlockDownload=deserialize_list(json_data.get("BlockDownload"), BlockDownloadDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class BlockDownloadDefinition(BaseModel):
    Active: Optional[bool]
    Unscanned: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDownloadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDownloadDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            Unscanned=json_data.get("Unscanned"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDownloadDefinition = BlockDownloadDefinition


@dataclass
class CriteriaDefinition(BaseModel):
    AllowUnknown: Optional[bool]
    AllowedLicenses: Optional[Sequence[str]]
    BannedLicenses: Optional[Sequence[str]]
    MinSeverity: Optional[str]
    CvssRange: Optional[Sequence["_CvssRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowUnknown=json_data.get("AllowUnknown"),
            AllowedLicenses=json_data.get("AllowedLicenses"),
            BannedLicenses=json_data.get("BannedLicenses"),
            MinSeverity=json_data.get("MinSeverity"),
            CvssRange=deserialize_list(json_data.get("CvssRange"), CvssRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


@dataclass
class CvssRangeDefinition(BaseModel):
    From: Optional[float]
    To: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CvssRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CvssRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            From=json_data.get("From"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CvssRangeDefinition = CvssRangeDefinition


