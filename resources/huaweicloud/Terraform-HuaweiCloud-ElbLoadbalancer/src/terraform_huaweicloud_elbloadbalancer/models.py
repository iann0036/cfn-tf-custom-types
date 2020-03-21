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
    AdminStateUp: Optional[float]
    Az: Optional[str]
    Bandwidth: Optional[float]
    ChargeMode: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    EipType: Optional[str]
    Name: Optional[str]
    SecurityGroupId: Optional[str]
    Status: Optional[str]
    Tenantid: Optional[str]
    Type: Optional[str]
    UpdateTime: Optional[str]
    VipAddress: Optional[str]
    VipSubnetId: Optional[str]
    VpcId: Optional[str]
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
            AdminStateUp=json_data.get("AdminStateUp"),
            Az=json_data.get("Az"),
            Bandwidth=json_data.get("Bandwidth"),
            ChargeMode=json_data.get("ChargeMode"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            EipType=json_data.get("EipType"),
            Name=json_data.get("Name"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Status=json_data.get("Status"),
            Tenantid=json_data.get("Tenantid"),
            Type=json_data.get("Type"),
            UpdateTime=json_data.get("UpdateTime"),
            VipAddress=json_data.get("VipAddress"),
            VipSubnetId=json_data.get("VipSubnetId"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


