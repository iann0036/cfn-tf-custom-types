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
    Circuit: Optional[Sequence["_CircuitDefinition"]]
    HcxCloudManagerEndpoint: Optional[str]
    Id: Optional[str]
    InternetConnectionEnabled: Optional[bool]
    Location: Optional[str]
    ManagementSubnetCidr: Optional[str]
    Name: Optional[str]
    NetworkSubnetCidr: Optional[str]
    NsxtCertificateThumbprint: Optional[str]
    NsxtManagerEndpoint: Optional[str]
    NsxtPassword: Optional[str]
    ProvisioningSubnetCidr: Optional[str]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VcenterCertificateThumbprint: Optional[str]
    VcenterPassword: Optional[str]
    VcsaEndpoint: Optional[str]
    VmotionSubnetCidr: Optional[str]
    ManagementCluster: Optional[Sequence["_ManagementClusterDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Circuit=deserialize_list(json_data.get("Circuit"), CircuitDefinition),
            HcxCloudManagerEndpoint=json_data.get("HcxCloudManagerEndpoint"),
            Id=json_data.get("Id"),
            InternetConnectionEnabled=json_data.get("InternetConnectionEnabled"),
            Location=json_data.get("Location"),
            ManagementSubnetCidr=json_data.get("ManagementSubnetCidr"),
            Name=json_data.get("Name"),
            NetworkSubnetCidr=json_data.get("NetworkSubnetCidr"),
            NsxtCertificateThumbprint=json_data.get("NsxtCertificateThumbprint"),
            NsxtManagerEndpoint=json_data.get("NsxtManagerEndpoint"),
            NsxtPassword=json_data.get("NsxtPassword"),
            ProvisioningSubnetCidr=json_data.get("ProvisioningSubnetCidr"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VcenterCertificateThumbprint=json_data.get("VcenterCertificateThumbprint"),
            VcenterPassword=json_data.get("VcenterPassword"),
            VcsaEndpoint=json_data.get("VcsaEndpoint"),
            VmotionSubnetCidr=json_data.get("VmotionSubnetCidr"),
            ManagementCluster=deserialize_list(json_data.get("ManagementCluster"), ManagementClusterDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CircuitDefinition(BaseModel):
    ExpressRouteId: Optional[str]
    ExpressRoutePrivatePeeringId: Optional[str]
    PrimarySubnetCidr: Optional[str]
    SecondarySubnetCidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CircuitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CircuitDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpressRouteId=json_data.get("ExpressRouteId"),
            ExpressRoutePrivatePeeringId=json_data.get("ExpressRoutePrivatePeeringId"),
            PrimarySubnetCidr=json_data.get("PrimarySubnetCidr"),
            SecondarySubnetCidr=json_data.get("SecondarySubnetCidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CircuitDefinition = CircuitDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class ManagementClusterDefinition(BaseModel):
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementClusterDefinition = ManagementClusterDefinition


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


