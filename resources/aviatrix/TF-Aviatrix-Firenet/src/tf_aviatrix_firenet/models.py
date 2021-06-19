# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    EgressEnabled: Optional[bool]
    EgressStaticCidrs: Optional[Sequence[str]]
    HashingAlgorithm: Optional[str]
    Id: Optional[str]
    InspectionEnabled: Optional[bool]
    KeepAliveViaLanInterfaceEnabled: Optional[bool]
    ManageFirewallInstanceAssociation: Optional[bool]
    TgwSegmentationForEgressEnabled: Optional[bool]
    VpcId: Optional[str]
    FirewallInstanceAssociation: Optional[Sequence["_FirewallInstanceAssociationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EgressEnabled=json_data.get("EgressEnabled"),
            EgressStaticCidrs=json_data.get("EgressStaticCidrs"),
            HashingAlgorithm=json_data.get("HashingAlgorithm"),
            Id=json_data.get("Id"),
            InspectionEnabled=json_data.get("InspectionEnabled"),
            KeepAliveViaLanInterfaceEnabled=json_data.get("KeepAliveViaLanInterfaceEnabled"),
            ManageFirewallInstanceAssociation=json_data.get("ManageFirewallInstanceAssociation"),
            TgwSegmentationForEgressEnabled=json_data.get("TgwSegmentationForEgressEnabled"),
            VpcId=json_data.get("VpcId"),
            FirewallInstanceAssociation=deserialize_list(json_data.get("FirewallInstanceAssociation"), FirewallInstanceAssociationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallInstanceAssociationDefinition(BaseModel):
    Attached: Optional[bool]
    EgressInterface: Optional[str]
    FirenetGwName: Optional[str]
    FirewallName: Optional[str]
    InstanceId: Optional[str]
    LanInterface: Optional[str]
    ManagementInterface: Optional[str]
    VendorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallInstanceAssociationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallInstanceAssociationDefinition"]:
        if not json_data:
            return None
        return cls(
            Attached=json_data.get("Attached"),
            EgressInterface=json_data.get("EgressInterface"),
            FirenetGwName=json_data.get("FirenetGwName"),
            FirewallName=json_data.get("FirewallName"),
            InstanceId=json_data.get("InstanceId"),
            LanInterface=json_data.get("LanInterface"),
            ManagementInterface=json_data.get("ManagementInterface"),
            VendorType=json_data.get("VendorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallInstanceAssociationDefinition = FirewallInstanceAssociationDefinition


