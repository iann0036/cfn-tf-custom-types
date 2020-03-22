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
    AclId: Optional[str]
    Cidr: Optional[str]
    DisplayText: Optional[str]
    Endip: Optional[str]
    Gateway: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NetworkDomain: Optional[str]
    NetworkOffering: Optional[str]
    Project: Optional[str]
    SourceNatIp: Optional[bool]
    SourceNatIpId: Optional[str]
    Startip: Optional[str]
    Vlan: Optional[float]
    VpcId: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AclId=json_data.get("AclId"),
            Cidr=json_data.get("Cidr"),
            DisplayText=json_data.get("DisplayText"),
            Endip=json_data.get("Endip"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkDomain=json_data.get("NetworkDomain"),
            NetworkOffering=json_data.get("NetworkOffering"),
            Project=json_data.get("Project"),
            SourceNatIp=json_data.get("SourceNatIp"),
            SourceNatIpId=json_data.get("SourceNatIpId"),
            Startip=json_data.get("Startip"),
            Vlan=json_data.get("Vlan"),
            VpcId=json_data.get("VpcId"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


