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
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Spec: Optional[Sequence["_Spec"]]
    Provider: Optional[Sequence["_Provider"]]
    VirtualNode: Optional[Sequence["_VirtualNode"]]
    VirtualRouter: Optional[Sequence["_VirtualRouter"]]

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
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Spec=json_data.get("Spec"),
            Provider=json_data.get("Provider"),
            VirtualNode=json_data.get("VirtualNode"),
            VirtualRouter=json_data.get("VirtualRouter"),
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
    Provider: Optional[Sequence["_Provider"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Provider:
    VirtualNode: Optional[Sequence["_VirtualNode"]]
    VirtualRouter: Optional[Sequence["_VirtualRouter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Provider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Provider"]:
        if not json_data:
            return None
        return cls(
            VirtualNode=json_data.get("VirtualNode"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Provider = Provider


@dataclass
class VirtualNode:
    VirtualNodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNode"]:
        if not json_data:
            return None
        return cls(
            VirtualNodeName=json_data.get("VirtualNodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNode = VirtualNode


@dataclass
class VirtualRouter:
    VirtualRouterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualRouter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualRouter"]:
        if not json_data:
            return None
        return cls(
            VirtualRouterName=json_data.get("VirtualRouterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualRouter = VirtualRouter


