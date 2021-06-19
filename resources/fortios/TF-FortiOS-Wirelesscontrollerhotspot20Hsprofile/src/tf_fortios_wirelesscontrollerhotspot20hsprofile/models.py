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
    AccessNetworkAsra: Optional[str]
    AccessNetworkEsr: Optional[str]
    AccessNetworkInternet: Optional[str]
    AccessNetworkType: Optional[str]
    AccessNetworkUesa: Optional[str]
    AnqpDomainId: Optional[float]
    BssTransition: Optional[str]
    ConnCap: Optional[str]
    DeauthRequestTimeout: Optional[float]
    Dgaf: Optional[str]
    DomainName: Optional[str]
    DynamicSortSubtable: Optional[str]
    GasComebackDelay: Optional[float]
    GasFragmentationLimit: Optional[float]
    Hessid: Optional[str]
    Id: Optional[str]
    IpAddrType: Optional[str]
    L2tif: Optional[str]
    N3gppPlmn: Optional[str]
    NaiRealm: Optional[str]
    Name: Optional[str]
    NetworkAuth: Optional[str]
    OperFriendlyName: Optional[str]
    OsuSsid: Optional[str]
    PameBi: Optional[str]
    ProxyArp: Optional[str]
    QosMap: Optional[str]
    RoamingConsortium: Optional[str]
    Vdomparam: Optional[str]
    VenueGroup: Optional[str]
    VenueName: Optional[str]
    VenueType: Optional[str]
    WanMetrics: Optional[str]
    WnmSleepMode: Optional[str]
    OsuProvider: Optional[Sequence["_OsuProviderDefinition"]]

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
            AccessNetworkAsra=json_data.get("AccessNetworkAsra"),
            AccessNetworkEsr=json_data.get("AccessNetworkEsr"),
            AccessNetworkInternet=json_data.get("AccessNetworkInternet"),
            AccessNetworkType=json_data.get("AccessNetworkType"),
            AccessNetworkUesa=json_data.get("AccessNetworkUesa"),
            AnqpDomainId=json_data.get("AnqpDomainId"),
            BssTransition=json_data.get("BssTransition"),
            ConnCap=json_data.get("ConnCap"),
            DeauthRequestTimeout=json_data.get("DeauthRequestTimeout"),
            Dgaf=json_data.get("Dgaf"),
            DomainName=json_data.get("DomainName"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GasComebackDelay=json_data.get("GasComebackDelay"),
            GasFragmentationLimit=json_data.get("GasFragmentationLimit"),
            Hessid=json_data.get("Hessid"),
            Id=json_data.get("Id"),
            IpAddrType=json_data.get("IpAddrType"),
            L2tif=json_data.get("L2tif"),
            N3gppPlmn=json_data.get("N3gppPlmn"),
            NaiRealm=json_data.get("NaiRealm"),
            Name=json_data.get("Name"),
            NetworkAuth=json_data.get("NetworkAuth"),
            OperFriendlyName=json_data.get("OperFriendlyName"),
            OsuSsid=json_data.get("OsuSsid"),
            PameBi=json_data.get("PameBi"),
            ProxyArp=json_data.get("ProxyArp"),
            QosMap=json_data.get("QosMap"),
            RoamingConsortium=json_data.get("RoamingConsortium"),
            Vdomparam=json_data.get("Vdomparam"),
            VenueGroup=json_data.get("VenueGroup"),
            VenueName=json_data.get("VenueName"),
            VenueType=json_data.get("VenueType"),
            WanMetrics=json_data.get("WanMetrics"),
            WnmSleepMode=json_data.get("WnmSleepMode"),
            OsuProvider=deserialize_list(json_data.get("OsuProvider"), OsuProviderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OsuProviderDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsuProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsuProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsuProviderDefinition = OsuProviderDefinition


