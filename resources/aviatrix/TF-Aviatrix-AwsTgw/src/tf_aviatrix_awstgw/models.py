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
    AccountName: Optional[str]
    AttachedAviatrixTransitGateway: Optional[Sequence[str]]
    AwsSideAsNumber: Optional[str]
    Cidrs: Optional[Sequence[str]]
    CloudType: Optional[float]
    EnableMulticast: Optional[bool]
    Id: Optional[str]
    ManageSecurityDomain: Optional[bool]
    ManageTransitGatewayAttachment: Optional[bool]
    ManageVpcAttachment: Optional[bool]
    Region: Optional[str]
    TgwId: Optional[str]
    TgwName: Optional[str]
    SecurityDomains: Optional[Sequence["_SecurityDomainsDefinition"]]

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
            AccountName=json_data.get("AccountName"),
            AttachedAviatrixTransitGateway=json_data.get("AttachedAviatrixTransitGateway"),
            AwsSideAsNumber=json_data.get("AwsSideAsNumber"),
            Cidrs=json_data.get("Cidrs"),
            CloudType=json_data.get("CloudType"),
            EnableMulticast=json_data.get("EnableMulticast"),
            Id=json_data.get("Id"),
            ManageSecurityDomain=json_data.get("ManageSecurityDomain"),
            ManageTransitGatewayAttachment=json_data.get("ManageTransitGatewayAttachment"),
            ManageVpcAttachment=json_data.get("ManageVpcAttachment"),
            Region=json_data.get("Region"),
            TgwId=json_data.get("TgwId"),
            TgwName=json_data.get("TgwName"),
            SecurityDomains=deserialize_list(json_data.get("SecurityDomains"), SecurityDomainsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SecurityDomainsDefinition(BaseModel):
    AviatrixFirewall: Optional[bool]
    ConnectedDomains: Optional[Sequence[str]]
    NativeEgress: Optional[bool]
    NativeFirewall: Optional[bool]
    SecurityDomainName: Optional[str]
    AttachedVpc: Optional[Sequence["_AttachedVpcDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityDomainsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityDomainsDefinition"]:
        if not json_data:
            return None
        return cls(
            AviatrixFirewall=json_data.get("AviatrixFirewall"),
            ConnectedDomains=json_data.get("ConnectedDomains"),
            NativeEgress=json_data.get("NativeEgress"),
            NativeFirewall=json_data.get("NativeFirewall"),
            SecurityDomainName=json_data.get("SecurityDomainName"),
            AttachedVpc=deserialize_list(json_data.get("AttachedVpc"), AttachedVpcDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityDomainsDefinition = SecurityDomainsDefinition


@dataclass
class AttachedVpcDefinition(BaseModel):
    CustomizedRouteAdvertisement: Optional[str]
    CustomizedRoutes: Optional[str]
    DisableLocalRoutePropagation: Optional[bool]
    RouteTables: Optional[str]
    Subnets: Optional[str]
    VpcAccountName: Optional[str]
    VpcId: Optional[str]
    VpcRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachedVpcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachedVpcDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomizedRouteAdvertisement=json_data.get("CustomizedRouteAdvertisement"),
            CustomizedRoutes=json_data.get("CustomizedRoutes"),
            DisableLocalRoutePropagation=json_data.get("DisableLocalRoutePropagation"),
            RouteTables=json_data.get("RouteTables"),
            Subnets=json_data.get("Subnets"),
            VpcAccountName=json_data.get("VpcAccountName"),
            VpcId=json_data.get("VpcId"),
            VpcRegion=json_data.get("VpcRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachedVpcDefinition = AttachedVpcDefinition


