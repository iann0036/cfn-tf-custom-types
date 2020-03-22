# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    InputParameters: Optional[str]
    MaximumExecutionFrequency: Optional[str]
    Name: Optional[str]
    RuleId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Scope: Optional[Sequence["_Scope"]]
    Source: Optional[Sequence["_Source"]]
    SourceDetail: Optional[Sequence["_SourceDetail"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InputParameters=json_data.get("InputParameters"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            Name=json_data.get("Name"),
            RuleId=json_data.get("RuleId"),
            Tags=json_data.get("Tags"),
            Scope=json_data.get("Scope"),
            Source=json_data.get("Source"),
            SourceDetail=json_data.get("SourceDetail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Scope:
    ComplianceResourceId: Optional[str]
    ComplianceResourceTypes: Optional[Sequence[str]]
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Scope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scope"]:
        if not json_data:
            return None
        return cls(
            ComplianceResourceId=json_data.get("ComplianceResourceId"),
            ComplianceResourceTypes=json_data.get("ComplianceResourceTypes"),
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scope = Scope


@dataclass
class Source:
    Owner: Optional[str]
    SourceIdentifier: Optional[str]
    SourceDetail: Optional[Sequence["_SourceDetail"]]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
            SourceIdentifier=json_data.get("SourceIdentifier"),
            SourceDetail=json_data.get("SourceDetail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class SourceDetail:
    EventSource: Optional[str]
    MaximumExecutionFrequency: Optional[str]
    MessageType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetail"]:
        if not json_data:
            return None
        return cls(
            EventSource=json_data.get("EventSource"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            MessageType=json_data.get("MessageType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetail = SourceDetail


