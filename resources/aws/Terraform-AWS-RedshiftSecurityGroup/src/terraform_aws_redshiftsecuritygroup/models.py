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
    Id: Optional[str]
    Name: Optional[str]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Ingress=json_data.get("Ingress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ingress:
    Cidr: Optional[str]
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
            SecurityGroupName=json_data.get("SecurityGroupName"),
            SecurityGroupOwnerId=json_data.get("SecurityGroupOwnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ingress = Ingress


