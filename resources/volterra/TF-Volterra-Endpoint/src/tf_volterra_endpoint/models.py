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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    DnsName: Optional[str]
    HealthCheckPort: Optional[float]
    Id: Optional[str]
    Ip: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    DnsNameAdvanced: Optional[Sequence["_DnsNameAdvancedDefinition"]]
    ServiceInfo: Optional[Sequence["_ServiceInfoDefinition"]]
    Where: Optional[Sequence["_WhereDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DnsName=json_data.get("DnsName"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            DnsNameAdvanced=deserialize_list(json_data.get("DnsNameAdvanced"), DnsNameAdvancedDefinition),
            ServiceInfo=deserialize_list(json_data.get("ServiceInfo"), ServiceInfoDefinition),
            Where=deserialize_list(json_data.get("Where"), WhereDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class DnsNameAdvancedDefinition(BaseModel):
    Name: Optional[str]
    RefreshInterval: Optional[float]
    StrictTtl: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DnsNameAdvancedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsNameAdvancedDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RefreshInterval=json_data.get("RefreshInterval"),
            StrictTtl=json_data.get("StrictTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsNameAdvancedDefinition = DnsNameAdvancedDefinition


@dataclass
class ServiceInfoDefinition(BaseModel):
    DiscoveryType: Optional[str]
    ServiceName: Optional[str]
    ServiceSelector: Optional[Sequence["_ServiceSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            DiscoveryType=json_data.get("DiscoveryType"),
            ServiceName=json_data.get("ServiceName"),
            ServiceSelector=deserialize_list(json_data.get("ServiceSelector"), ServiceSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceInfoDefinition = ServiceInfoDefinition


@dataclass
class ServiceSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceSelectorDefinition = ServiceSelectorDefinition


@dataclass
class WhereDefinition(BaseModel):
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualNetwork: Optional[Sequence["_VirtualNetworkDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WhereDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhereDefinition"]:
        if not json_data:
            return None
        return cls(
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualNetwork=deserialize_list(json_data.get("VirtualNetwork"), VirtualNetworkDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhereDefinition = WhereDefinition


@dataclass
class SiteDefinition(BaseModel):
    NetworkType: Optional[str]
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteDefinition = SiteDefinition


@dataclass
class RefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefDefinition = RefDefinition


@dataclass
class VirtualNetworkDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkDefinition = VirtualNetworkDefinition


@dataclass
class VirtualSiteDefinition(BaseModel):
    NetworkType: Optional[str]
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualSiteDefinition = VirtualSiteDefinition


