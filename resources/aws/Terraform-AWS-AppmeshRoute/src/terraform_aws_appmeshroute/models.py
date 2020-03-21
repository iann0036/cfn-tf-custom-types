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
    CreatedDate: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VirtualRouterName: Optional[str]
    Spec: Optional[Sequence["_Spec"]]
    HttpRoute: Optional[Sequence["_HttpRoute"]]
    TcpRoute: Optional[Sequence["_TcpRoute"]]
    Action: Optional[Sequence["_Action"]]
    Match: Optional[Sequence["_Match"]]
    WeightedTarget: Optional[Sequence["_WeightedTarget"]]
    Header: Optional[Sequence["_Header"]]
    Range: Optional[Sequence["_Range"]]

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
            CreatedDate=json_data.get("CreatedDate"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            VirtualRouterName=json_data.get("VirtualRouterName"),
            Spec=json_data.get("Spec"),
            HttpRoute=json_data.get("HttpRoute"),
            TcpRoute=json_data.get("TcpRoute"),
            Action=json_data.get("Action"),
            Match=json_data.get("Match"),
            WeightedTarget=json_data.get("WeightedTarget"),
            Header=json_data.get("Header"),
            Range=json_data.get("Range"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Spec:
    Priority: Optional[float]
    HttpRoute: Optional[Sequence["_HttpRoute"]]
    TcpRoute: Optional[Sequence["_TcpRoute"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            HttpRoute=json_data.get("HttpRoute"),
            TcpRoute=json_data.get("TcpRoute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class HttpRoute:
    Action: Optional[Sequence["_Action"]]
    Match: Optional[Sequence["_Match"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRoute"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRoute = HttpRoute


@dataclass
class Action:
    WeightedTarget: Optional[Sequence["_WeightedTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            WeightedTarget=json_data.get("WeightedTarget"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class WeightedTarget:
    VirtualNode: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedTarget"]:
        if not json_data:
            return None
        return cls(
            VirtualNode=json_data.get("VirtualNode"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedTarget = WeightedTarget


@dataclass
class Match:
    Exact: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]
    Suffix: Optional[str]
    Range: Optional[Sequence["_Range"]]

    @classmethod
    def _deserialize(
        cls: Type["_Match"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Match"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
            Suffix=json_data.get("Suffix"),
            Range=json_data.get("Range"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Match = Match


@dataclass
class Range:
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Range"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Range"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Range = Range


@dataclass
class TcpRoute:
    Action: Optional[Sequence["_Action"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpRoute"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpRoute = TcpRoute


@dataclass
class Header:
    Invert: Optional[bool]
    Name: Optional[str]
    Match: Optional[Sequence["_Match"]]

    @classmethod
    def _deserialize(
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
        if not json_data:
            return None
        return cls(
            Invert=json_data.get("Invert"),
            Name=json_data.get("Name"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Header = Header


