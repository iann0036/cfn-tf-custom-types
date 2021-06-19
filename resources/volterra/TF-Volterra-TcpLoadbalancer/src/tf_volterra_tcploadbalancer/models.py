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
    AdvertiseOnPublicDefaultVip: Optional[bool]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    DnsVolterraManaged: Optional[bool]
    DoNotAdvertise: Optional[bool]
    DoNotRetractCluster: Optional[bool]
    Domains: Optional[Sequence[str]]
    HashPolicyChoiceLeastActive: Optional[bool]
    HashPolicyChoiceRandom: Optional[bool]
    HashPolicyChoiceRoundRobin: Optional[bool]
    HashPolicyChoiceSourceIpStickiness: Optional[bool]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    ListenPort: Optional[float]
    Name: Optional[str]
    Namespace: Optional[str]
    RetractCluster: Optional[bool]
    WithSni: Optional[bool]
    AdvertiseCustom: Optional[Sequence["_AdvertiseCustomDefinition"]]
    AdvertiseOnPublic: Optional[Sequence["_AdvertiseOnPublicDefinition"]]
    OriginPoolsWeights: Optional[Sequence["_OriginPoolsWeightsDefinition"]]

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
            AdvertiseOnPublicDefaultVip=json_data.get("AdvertiseOnPublicDefaultVip"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DnsVolterraManaged=json_data.get("DnsVolterraManaged"),
            DoNotAdvertise=json_data.get("DoNotAdvertise"),
            DoNotRetractCluster=json_data.get("DoNotRetractCluster"),
            Domains=json_data.get("Domains"),
            HashPolicyChoiceLeastActive=json_data.get("HashPolicyChoiceLeastActive"),
            HashPolicyChoiceRandom=json_data.get("HashPolicyChoiceRandom"),
            HashPolicyChoiceRoundRobin=json_data.get("HashPolicyChoiceRoundRobin"),
            HashPolicyChoiceSourceIpStickiness=json_data.get("HashPolicyChoiceSourceIpStickiness"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            ListenPort=json_data.get("ListenPort"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            RetractCluster=json_data.get("RetractCluster"),
            WithSni=json_data.get("WithSni"),
            AdvertiseCustom=deserialize_list(json_data.get("AdvertiseCustom"), AdvertiseCustomDefinition),
            AdvertiseOnPublic=deserialize_list(json_data.get("AdvertiseOnPublic"), AdvertiseOnPublicDefinition),
            OriginPoolsWeights=deserialize_list(json_data.get("OriginPoolsWeights"), OriginPoolsWeightsDefinition),
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
class AdvertiseCustomDefinition(BaseModel):
    AdvertiseWhere: Optional[Sequence["_AdvertiseWhereDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertiseCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertiseCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseWhere=deserialize_list(json_data.get("AdvertiseWhere"), AdvertiseWhereDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertiseCustomDefinition = AdvertiseCustomDefinition


@dataclass
class AdvertiseWhereDefinition(BaseModel):
    Port: Optional[float]
    UseDefaultPort: Optional[bool]
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualNetwork: Optional[Sequence["_VirtualNetworkDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]
    Vk8sService: Optional[Sequence["_Vk8sServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertiseWhereDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertiseWhereDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            UseDefaultPort=json_data.get("UseDefaultPort"),
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualNetwork=deserialize_list(json_data.get("VirtualNetwork"), VirtualNetworkDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
            Vk8sService=deserialize_list(json_data.get("Vk8sService"), Vk8sServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertiseWhereDefinition = AdvertiseWhereDefinition


@dataclass
class SiteDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteDefinition = SiteDefinition


@dataclass
class VirtualNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkDefinition = VirtualNetworkDefinition


@dataclass
class VirtualSiteDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualSiteDefinition = VirtualSiteDefinition


@dataclass
class Vk8sServiceDefinition(BaseModel):
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Vk8sServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vk8sServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vk8sServiceDefinition = Vk8sServiceDefinition


@dataclass
class AdvertiseOnPublicDefinition(BaseModel):
    PublicIp: Optional[Sequence["_PublicIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertiseOnPublicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertiseOnPublicDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicIp=deserialize_list(json_data.get("PublicIp"), PublicIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertiseOnPublicDefinition = AdvertiseOnPublicDefinition


@dataclass
class PublicIpDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpDefinition = PublicIpDefinition


@dataclass
class OriginPoolsWeightsDefinition(BaseModel):
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition"]]
    Weight: Optional[float]
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    Pool: Optional[Sequence["_PoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginPoolsWeightsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginPoolsWeightsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition),
            Weight=json_data.get("Weight"),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            Pool=deserialize_list(json_data.get("Pool"), PoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginPoolsWeightsDefinition = OriginPoolsWeightsDefinition


@dataclass
class EndpointSubsetsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSubsetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSubsetsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSubsetsDefinition = EndpointSubsetsDefinition


@dataclass
class ClusterDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterDefinition = ClusterDefinition


@dataclass
class PoolDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoolDefinition = PoolDefinition


