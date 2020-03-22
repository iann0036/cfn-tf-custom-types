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
    Description: Optional[str]
    DestinationCidrBlock: Optional[str]
    Id: Optional[str]
    Protocol: Optional[float]
    RuleAction: Optional[str]
    RuleNumber: Optional[float]
    SourceCidrBlock: Optional[str]
    TrafficDirection: Optional[str]
    TrafficMirrorFilterId: Optional[str]
    DestinationPortRange: Optional[Sequence["_DestinationPortRange"]]
    SourcePortRange: Optional[Sequence["_SourcePortRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            Id=json_data.get("Id"),
            Protocol=json_data.get("Protocol"),
            RuleAction=json_data.get("RuleAction"),
            RuleNumber=json_data.get("RuleNumber"),
            SourceCidrBlock=json_data.get("SourceCidrBlock"),
            TrafficDirection=json_data.get("TrafficDirection"),
            TrafficMirrorFilterId=json_data.get("TrafficMirrorFilterId"),
            DestinationPortRange=json_data.get("DestinationPortRange"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationPortRange:
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationPortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationPortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationPortRange = DestinationPortRange


@dataclass
class SourcePortRange:
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortRange = SourcePortRange


