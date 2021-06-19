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
    BillingTags: Optional[Sequence[float]]
    Cxp: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Segment: Optional[str]
    Size: Optional[str]
    VpnMode: Optional[str]
    Endpoint: Optional[Sequence["_EndpointDefinition"]]
    PolicyOptions: Optional[Sequence["_PolicyOptionsDefinition"]]
    RoutingOptions: Optional[Sequence["_RoutingOptionsDefinition"]]
    SegmentOptions: Optional[Sequence["_SegmentOptionsDefinition"]]

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
            BillingTags=json_data.get("BillingTags"),
            Cxp=json_data.get("Cxp"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Segment=json_data.get("Segment"),
            Size=json_data.get("Size"),
            VpnMode=json_data.get("VpnMode"),
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
            PolicyOptions=deserialize_list(json_data.get("PolicyOptions"), PolicyOptionsDefinition),
            RoutingOptions=deserialize_list(json_data.get("RoutingOptions"), RoutingOptionsDefinition),
            SegmentOptions=deserialize_list(json_data.get("SegmentOptions"), SegmentOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointDefinition(BaseModel):
    CustomerGatewayAsn: Optional[str]
    CustomerGatewayIp: Optional[str]
    Name: Optional[str]
    PresharedKeys: Optional[Sequence[str]]
    Advanced: Optional[Sequence["_AdvancedDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomerGatewayAsn=json_data.get("CustomerGatewayAsn"),
            CustomerGatewayIp=json_data.get("CustomerGatewayIp"),
            Name=json_data.get("Name"),
            PresharedKeys=json_data.get("PresharedKeys"),
            Advanced=deserialize_list(json_data.get("Advanced"), AdvancedDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


@dataclass
class AdvancedDefinition(BaseModel):
    DpdDelay: Optional[str]
    DpdTimeout: Optional[str]
    EspDhGroupNumbers: Optional[str]
    EspEncryptionAlgorithms: Optional[str]
    EspIntegrityAlgorithms: Optional[str]
    EspLifeTime: Optional[float]
    EspRandomTime: Optional[str]
    EspRekeyTime: Optional[str]
    IkeDhGroupNumbers: Optional[str]
    IkeEncryptionAlgorithms: Optional[str]
    IkeIntegrityAlgorithms: Optional[str]
    IkeOverTime: Optional[float]
    IkeRandomTime: Optional[float]
    IkeRekeyTime: Optional[float]
    IkeVersion: Optional[str]
    Initiator: Optional[str]
    LocalAuthType: Optional[str]
    LocalAuthValue: Optional[str]
    RemoteAuthType: Optional[str]
    RemoteAuthValue: Optional[str]
    ReplayWindowSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedDefinition"]:
        if not json_data:
            return None
        return cls(
            DpdDelay=json_data.get("DpdDelay"),
            DpdTimeout=json_data.get("DpdTimeout"),
            EspDhGroupNumbers=json_data.get("EspDhGroupNumbers"),
            EspEncryptionAlgorithms=json_data.get("EspEncryptionAlgorithms"),
            EspIntegrityAlgorithms=json_data.get("EspIntegrityAlgorithms"),
            EspLifeTime=json_data.get("EspLifeTime"),
            EspRandomTime=json_data.get("EspRandomTime"),
            EspRekeyTime=json_data.get("EspRekeyTime"),
            IkeDhGroupNumbers=json_data.get("IkeDhGroupNumbers"),
            IkeEncryptionAlgorithms=json_data.get("IkeEncryptionAlgorithms"),
            IkeIntegrityAlgorithms=json_data.get("IkeIntegrityAlgorithms"),
            IkeOverTime=json_data.get("IkeOverTime"),
            IkeRandomTime=json_data.get("IkeRandomTime"),
            IkeRekeyTime=json_data.get("IkeRekeyTime"),
            IkeVersion=json_data.get("IkeVersion"),
            Initiator=json_data.get("Initiator"),
            LocalAuthType=json_data.get("LocalAuthType"),
            LocalAuthValue=json_data.get("LocalAuthValue"),
            RemoteAuthType=json_data.get("RemoteAuthType"),
            RemoteAuthValue=json_data.get("RemoteAuthValue"),
            ReplayWindowSize=json_data.get("ReplayWindowSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedDefinition = AdvancedDefinition


@dataclass
class PolicyOptionsDefinition(BaseModel):
    CxpPrefixListIds: Optional[Sequence[float]]
    OnPremPrefixListIds: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CxpPrefixListIds=json_data.get("CxpPrefixListIds"),
            OnPremPrefixListIds=json_data.get("OnPremPrefixListIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyOptionsDefinition = PolicyOptionsDefinition


@dataclass
class RoutingOptionsDefinition(BaseModel):
    CustomerGatewayAsn: Optional[str]
    PrefixListId: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomerGatewayAsn=json_data.get("CustomerGatewayAsn"),
            PrefixListId=json_data.get("PrefixListId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingOptionsDefinition = RoutingOptionsDefinition


@dataclass
class SegmentOptionsDefinition(BaseModel):
    DisableAdvertiseOnPremRoutes: Optional[bool]
    DisableInternetExit: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SegmentOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegmentOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableAdvertiseOnPremRoutes=json_data.get("DisableAdvertiseOnPremRoutes"),
            DisableInternetExit=json_data.get("DisableInternetExit"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegmentOptionsDefinition = SegmentOptionsDefinition


