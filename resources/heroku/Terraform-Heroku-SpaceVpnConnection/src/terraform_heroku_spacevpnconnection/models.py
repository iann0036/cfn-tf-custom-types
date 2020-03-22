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
    Id: Optional[str]
    IkeVersion: Optional[float]
    Name: Optional[str]
    PublicIp: Optional[str]
    RoutableCidrs: Optional[Sequence[str]]
    Space: Optional[str]
    SpaceCidrBlock: Optional[str]
    Tunnels: Optional[Sequence["_Tunnels"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            IkeVersion=json_data.get("IkeVersion"),
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            RoutableCidrs=json_data.get("RoutableCidrs"),
            Space=json_data.get("Space"),
            SpaceCidrBlock=json_data.get("SpaceCidrBlock"),
            Tunnels=json_data.get("Tunnels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tunnels:
    Ip: Optional[str]
    PreSharedKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tunnels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tunnels"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            PreSharedKey=json_data.get("PreSharedKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tunnels = Tunnels


