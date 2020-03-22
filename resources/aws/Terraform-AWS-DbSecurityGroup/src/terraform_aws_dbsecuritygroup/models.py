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
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Ingress: Optional[Sequence["_Ingress"]]

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
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Ingress=json_data.get("Ingress"),
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
class Ingress:
    Cidr: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityGroupName: Optional[str]
    SecurityGroupOwnerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupName=json_data.get("SecurityGroupName"),
            SecurityGroupOwnerId=json_data.get("SecurityGroupOwnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ingress = Ingress


