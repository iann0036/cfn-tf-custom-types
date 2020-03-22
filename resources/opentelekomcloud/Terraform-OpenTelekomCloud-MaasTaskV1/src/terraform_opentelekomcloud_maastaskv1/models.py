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
    EnableKms: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[float]
    ThreadNum: Optional[float]
    DstNode: Optional[Sequence["_DstNode"]]
    SmnInfo: Optional[Sequence["_SmnInfo"]]
    SrcNode: Optional[Sequence["_SrcNode"]]
    Timeouts: Optional["_Timeouts"]

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
            EnableKms=json_data.get("EnableKms"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            ThreadNum=json_data.get("ThreadNum"),
            DstNode=json_data.get("DstNode"),
            SmnInfo=json_data.get("SmnInfo"),
            SrcNode=json_data.get("SrcNode"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DstNode:
    Ak: Optional[str]
    Bucket: Optional[str]
    ObjectKey: Optional[str]
    Region: Optional[str]
    Sk: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstNode"]:
        if not json_data:
            return None
        return cls(
            Ak=json_data.get("Ak"),
            Bucket=json_data.get("Bucket"),
            ObjectKey=json_data.get("ObjectKey"),
            Region=json_data.get("Region"),
            Sk=json_data.get("Sk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstNode = DstNode


@dataclass
class SmnInfo:
    Language: Optional[str]
    TopicUrn: Optional[str]
    TriggerConditions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SmnInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmnInfo"]:
        if not json_data:
            return None
        return cls(
            Language=json_data.get("Language"),
            TopicUrn=json_data.get("TopicUrn"),
            TriggerConditions=json_data.get("TriggerConditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmnInfo = SmnInfo


@dataclass
class SrcNode:
    Ak: Optional[str]
    Bucket: Optional[str]
    CloudType: Optional[str]
    ObjectKey: Optional[str]
    Region: Optional[str]
    Sk: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcNode"]:
        if not json_data:
            return None
        return cls(
            Ak=json_data.get("Ak"),
            Bucket=json_data.get("Bucket"),
            CloudType=json_data.get("CloudType"),
            ObjectKey=json_data.get("ObjectKey"),
            Region=json_data.get("Region"),
            Sk=json_data.get("Sk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcNode = SrcNode


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


