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
    Id: Optional[str]
    InternetSecurityEnabled: Optional[bool]
    Name: Optional[str]
    RemoteVpnSiteId: Optional[str]
    VpnGatewayId: Optional[str]
    Routing: Optional[Sequence["_RoutingDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VpnLink: Optional[Sequence["_VpnLinkDefinition"]]

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
            Id=json_data.get("Id"),
            InternetSecurityEnabled=json_data.get("InternetSecurityEnabled"),
            Name=json_data.get("Name"),
            RemoteVpnSiteId=json_data.get("RemoteVpnSiteId"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            Routing=deserialize_list(json_data.get("Routing"), RoutingDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VpnLink=deserialize_list(json_data.get("VpnLink"), VpnLinkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoutingDefinition(BaseModel):
    AssociatedRouteTable: Optional[str]
    PropagatedRouteTables: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            AssociatedRouteTable=json_data.get("AssociatedRouteTable"),
            PropagatedRouteTables=json_data.get("PropagatedRouteTables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingDefinition = RoutingDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VpnLinkDefinition(BaseModel):
    BandwidthMbps: Optional[float]
    BgpEnabled: Optional[bool]
    LocalAzureIpAddressEnabled: Optional[bool]
    Name: Optional[str]
    PolicyBasedTrafficSelectorEnabled: Optional[bool]
    Protocol: Optional[str]
    RatelimitEnabled: Optional[bool]
    RouteWeight: Optional[float]
    SharedKey: Optional[str]
    VpnSiteLinkId: Optional[str]
    IpsecPolicy: Optional[Sequence["_IpsecPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VpnLinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnLinkDefinition"]:
        if not json_data:
            return None
        return cls(
            BandwidthMbps=json_data.get("BandwidthMbps"),
            BgpEnabled=json_data.get("BgpEnabled"),
            LocalAzureIpAddressEnabled=json_data.get("LocalAzureIpAddressEnabled"),
            Name=json_data.get("Name"),
            PolicyBasedTrafficSelectorEnabled=json_data.get("PolicyBasedTrafficSelectorEnabled"),
            Protocol=json_data.get("Protocol"),
            RatelimitEnabled=json_data.get("RatelimitEnabled"),
            RouteWeight=json_data.get("RouteWeight"),
            SharedKey=json_data.get("SharedKey"),
            VpnSiteLinkId=json_data.get("VpnSiteLinkId"),
            IpsecPolicy=deserialize_list(json_data.get("IpsecPolicy"), IpsecPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnLinkDefinition = VpnLinkDefinition


@dataclass
class IpsecPolicyDefinition(BaseModel):
    DhGroup: Optional[str]
    EncryptionAlgorithm: Optional[str]
    IkeEncryptionAlgorithm: Optional[str]
    IkeIntegrityAlgorithm: Optional[str]
    IntegrityAlgorithm: Optional[str]
    PfsGroup: Optional[str]
    SaDataSizeKb: Optional[float]
    SaLifetimeSec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DhGroup=json_data.get("DhGroup"),
            EncryptionAlgorithm=json_data.get("EncryptionAlgorithm"),
            IkeEncryptionAlgorithm=json_data.get("IkeEncryptionAlgorithm"),
            IkeIntegrityAlgorithm=json_data.get("IkeIntegrityAlgorithm"),
            IntegrityAlgorithm=json_data.get("IntegrityAlgorithm"),
            PfsGroup=json_data.get("PfsGroup"),
            SaDataSizeKb=json_data.get("SaDataSizeKb"),
            SaLifetimeSec=json_data.get("SaLifetimeSec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecPolicyDefinition = IpsecPolicyDefinition


