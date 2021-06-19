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
    Uuid: Optional[str]
    ControllerLimits: Optional[Sequence["_ControllerLimitsDefinition"]]
    ControllerSizes: Optional[Sequence["_ControllerSizesDefinition"]]
    ServiceengineLimits: Optional[Sequence["_ServiceengineLimitsDefinition"]]

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
            Uuid=json_data.get("Uuid"),
            ControllerLimits=deserialize_list(json_data.get("ControllerLimits"), ControllerLimitsDefinition),
            ControllerSizes=deserialize_list(json_data.get("ControllerSizes"), ControllerSizesDefinition),
            ServiceengineLimits=deserialize_list(json_data.get("ServiceengineLimits"), ServiceengineLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ControllerLimitsDefinition(BaseModel):
    CertificatesPerVirtualservice: Optional[float]
    DefaultRoutesPerVrfcontext: Optional[float]
    IpsPerIpgroup: Optional[float]
    PoolgroupsPerVirtualservice: Optional[float]
    PoolsPerPoolgroup: Optional[float]
    PoolsPerVirtualservice: Optional[float]
    RoutesPerVrfcontext: Optional[float]
    RulesPerHttppolicy: Optional[float]
    RulesPerNetworksecuritypolicy: Optional[float]
    ServersPerPool: Optional[float]
    SniChildrenPerParent: Optional[float]
    StringsPerStringgroup: Optional[float]
    VsBgpScaleout: Optional[float]
    VsL2Scaleout: Optional[float]
    ControllerCloudLimits: Optional[Sequence["_ControllerCloudLimitsDefinition"]]
    ControllerSizingLimits: Optional[Sequence["_ControllerSizingLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificatesPerVirtualservice=json_data.get("CertificatesPerVirtualservice"),
            DefaultRoutesPerVrfcontext=json_data.get("DefaultRoutesPerVrfcontext"),
            IpsPerIpgroup=json_data.get("IpsPerIpgroup"),
            PoolgroupsPerVirtualservice=json_data.get("PoolgroupsPerVirtualservice"),
            PoolsPerPoolgroup=json_data.get("PoolsPerPoolgroup"),
            PoolsPerVirtualservice=json_data.get("PoolsPerVirtualservice"),
            RoutesPerVrfcontext=json_data.get("RoutesPerVrfcontext"),
            RulesPerHttppolicy=json_data.get("RulesPerHttppolicy"),
            RulesPerNetworksecuritypolicy=json_data.get("RulesPerNetworksecuritypolicy"),
            ServersPerPool=json_data.get("ServersPerPool"),
            SniChildrenPerParent=json_data.get("SniChildrenPerParent"),
            StringsPerStringgroup=json_data.get("StringsPerStringgroup"),
            VsBgpScaleout=json_data.get("VsBgpScaleout"),
            VsL2Scaleout=json_data.get("VsL2Scaleout"),
            ControllerCloudLimits=deserialize_list(json_data.get("ControllerCloudLimits"), ControllerCloudLimitsDefinition),
            ControllerSizingLimits=deserialize_list(json_data.get("ControllerSizingLimits"), ControllerSizingLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerLimitsDefinition = ControllerLimitsDefinition


@dataclass
class ControllerCloudLimitsDefinition(BaseModel):
    NumClouds: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerCloudLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerCloudLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            NumClouds=json_data.get("NumClouds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerCloudLimitsDefinition = ControllerCloudLimitsDefinition


@dataclass
class ControllerSizingLimitsDefinition(BaseModel):
    Flavor: Optional[str]
    NumClouds: Optional[float]
    NumEastWestVirtualservices: Optional[float]
    NumServers: Optional[float]
    NumServiceengines: Optional[float]
    NumTenants: Optional[float]
    NumVirtualservices: Optional[float]
    NumVirtualservicesRtMetrics: Optional[float]
    NumVrfs: Optional[float]
    ControllerSizingCloudLimits: Optional[Sequence["_ControllerSizingCloudLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerSizingLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerSizingLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Flavor=json_data.get("Flavor"),
            NumClouds=json_data.get("NumClouds"),
            NumEastWestVirtualservices=json_data.get("NumEastWestVirtualservices"),
            NumServers=json_data.get("NumServers"),
            NumServiceengines=json_data.get("NumServiceengines"),
            NumTenants=json_data.get("NumTenants"),
            NumVirtualservices=json_data.get("NumVirtualservices"),
            NumVirtualservicesRtMetrics=json_data.get("NumVirtualservicesRtMetrics"),
            NumVrfs=json_data.get("NumVrfs"),
            ControllerSizingCloudLimits=deserialize_list(json_data.get("ControllerSizingCloudLimits"), ControllerSizingCloudLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerSizingLimitsDefinition = ControllerSizingLimitsDefinition


@dataclass
class ControllerSizingCloudLimitsDefinition(BaseModel):
    NumClouds: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerSizingCloudLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerSizingCloudLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            NumClouds=json_data.get("NumClouds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerSizingCloudLimitsDefinition = ControllerSizingCloudLimitsDefinition


@dataclass
class ControllerSizesDefinition(BaseModel):
    Flavor: Optional[str]
    MinCpus: Optional[float]
    MinMemory: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerSizesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerSizesDefinition"]:
        if not json_data:
            return None
        return cls(
            Flavor=json_data.get("Flavor"),
            MinCpus=json_data.get("MinCpus"),
            MinMemory=json_data.get("MinMemory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerSizesDefinition = ControllerSizesDefinition


@dataclass
class ServiceengineLimitsDefinition(BaseModel):
    AllVirtualservicesPerServiceengine: Optional[float]
    EwVirtualservicesPerServiceengine: Optional[float]
    NsVirtualservicesPerServiceengine: Optional[float]
    NumLogicalIntfPerSe: Optional[float]
    NumPhyIntfPerSe: Optional[float]
    NumVirtualservicesRtMetrics: Optional[float]
    NumVlanIntfPerPhyIntf: Optional[float]
    NumVlanIntfPerSe: Optional[float]
    ServiceengineCloudLimits: Optional[Sequence["_ServiceengineCloudLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceengineLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceengineLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllVirtualservicesPerServiceengine=json_data.get("AllVirtualservicesPerServiceengine"),
            EwVirtualservicesPerServiceengine=json_data.get("EwVirtualservicesPerServiceengine"),
            NsVirtualservicesPerServiceengine=json_data.get("NsVirtualservicesPerServiceengine"),
            NumLogicalIntfPerSe=json_data.get("NumLogicalIntfPerSe"),
            NumPhyIntfPerSe=json_data.get("NumPhyIntfPerSe"),
            NumVirtualservicesRtMetrics=json_data.get("NumVirtualservicesRtMetrics"),
            NumVlanIntfPerPhyIntf=json_data.get("NumVlanIntfPerPhyIntf"),
            NumVlanIntfPerSe=json_data.get("NumVlanIntfPerSe"),
            ServiceengineCloudLimits=deserialize_list(json_data.get("ServiceengineCloudLimits"), ServiceengineCloudLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceengineLimitsDefinition = ServiceengineLimitsDefinition


@dataclass
class ServiceengineCloudLimitsDefinition(BaseModel):
    Type: Optional[str]
    VrfsPerServiceengine: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceengineCloudLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceengineCloudLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            VrfsPerServiceengine=json_data.get("VrfsPerServiceengine"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceengineCloudLimitsDefinition = ServiceengineCloudLimitsDefinition


