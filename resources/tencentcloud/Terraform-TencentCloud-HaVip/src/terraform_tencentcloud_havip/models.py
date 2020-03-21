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
    AddressIp: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    Name: Optional[str]
    NetworkInterfaceId: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    Vip: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AddressIp=json_data.get("AddressIp"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            Name=json_data.get("Name"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            Vip=json_data.get("Vip"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


