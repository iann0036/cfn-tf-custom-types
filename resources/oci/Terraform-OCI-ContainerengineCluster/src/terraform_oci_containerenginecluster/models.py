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
    AvailableKubernetesUpgrades: Optional[Sequence[str]]
    CompartmentId: Optional[str]
    Endpoints: Optional[Sequence["_Endpoints"]]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    KubernetesVersion: Optional[str]
    LifecycleDetails: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    State: Optional[str]
    VcnId: Optional[str]
    Options: Optional[Sequence["_Options"]]
    Timeouts: Optional["_Timeouts"]
    AddOns: Optional[Sequence["_AddOns"]]
    KubernetesNetworkConfig: Optional[Sequence["_KubernetesNetworkConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailableKubernetesUpgrades=json_data.get("AvailableKubernetesUpgrades"),
            CompartmentId=json_data.get("CompartmentId"),
            Endpoints=json_data.get("Endpoints"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            VcnId=json_data.get("VcnId"),
            Options=json_data.get("Options"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            AddOns=json_data.get("AddOns"),
            KubernetesNetworkConfig=json_data.get("KubernetesNetworkConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Endpoints:
    Kubernetes: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoints"]:
        if not json_data:
            return None
        return cls(
            Kubernetes=json_data.get("Kubernetes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoints = Endpoints


@dataclass
class Metadata:
    CreatedByUserId: Optional[str]
    CreatedByWorkRequestId: Optional[str]
    DeletedByUserId: Optional[str]
    DeletedByWorkRequestId: Optional[str]
    TimeCreated: Optional[str]
    TimeDeleted: Optional[str]
    TimeUpdated: Optional[str]
    UpdatedByUserId: Optional[str]
    UpdatedByWorkRequestId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            CreatedByUserId=json_data.get("CreatedByUserId"),
            CreatedByWorkRequestId=json_data.get("CreatedByWorkRequestId"),
            DeletedByUserId=json_data.get("DeletedByUserId"),
            DeletedByWorkRequestId=json_data.get("DeletedByWorkRequestId"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeDeleted=json_data.get("TimeDeleted"),
            TimeUpdated=json_data.get("TimeUpdated"),
            UpdatedByUserId=json_data.get("UpdatedByUserId"),
            UpdatedByWorkRequestId=json_data.get("UpdatedByWorkRequestId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Options:
    ServiceLbSubnetIds: Optional[Sequence[str]]
    AddOns: Optional[Sequence["_AddOns"]]
    KubernetesNetworkConfig: Optional[Sequence["_KubernetesNetworkConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            ServiceLbSubnetIds=json_data.get("ServiceLbSubnetIds"),
            AddOns=json_data.get("AddOns"),
            KubernetesNetworkConfig=json_data.get("KubernetesNetworkConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class AddOns:
    IsKubernetesDashboardEnabled: Optional[bool]
    IsTillerEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AddOns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddOns"]:
        if not json_data:
            return None
        return cls(
            IsKubernetesDashboardEnabled=json_data.get("IsKubernetesDashboardEnabled"),
            IsTillerEnabled=json_data.get("IsTillerEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddOns = AddOns


@dataclass
class KubernetesNetworkConfig:
    PodsCidr: Optional[str]
    ServicesCidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesNetworkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesNetworkConfig"]:
        if not json_data:
            return None
        return cls(
            PodsCidr=json_data.get("PodsCidr"),
            ServicesCidr=json_data.get("ServicesCidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesNetworkConfig = KubernetesNetworkConfig


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


