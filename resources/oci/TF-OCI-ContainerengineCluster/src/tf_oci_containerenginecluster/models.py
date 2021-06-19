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
    AvailableKubernetesUpgrades: Optional[Sequence[str]]
    CompartmentId: Optional[str]
    Endpoints: Optional[Sequence["_EndpointsDefinition"]]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    KubernetesVersion: Optional[str]
    LifecycleDetails: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    State: Optional[str]
    VcnId: Optional[str]
    EndpointConfig: Optional[Sequence["_EndpointConfigDefinition"]]
    ImagePolicyConfig: Optional[Sequence["_ImagePolicyConfigDefinition"]]
    Options: Optional[Sequence["_OptionsDefinition"]]
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
            AvailableKubernetesUpgrades=json_data.get("AvailableKubernetesUpgrades"),
            CompartmentId=json_data.get("CompartmentId"),
            Endpoints=deserialize_list(json_data.get("Endpoints"), EndpointsDefinition),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            VcnId=json_data.get("VcnId"),
            EndpointConfig=deserialize_list(json_data.get("EndpointConfig"), EndpointConfigDefinition),
            ImagePolicyConfig=deserialize_list(json_data.get("ImagePolicyConfig"), ImagePolicyConfigDefinition),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointsDefinition(BaseModel):
    Kubernetes: Optional[str]
    PrivateEndpoint: Optional[str]
    PublicEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            Kubernetes=json_data.get("Kubernetes"),
            PrivateEndpoint=json_data.get("PrivateEndpoint"),
            PublicEndpoint=json_data.get("PublicEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsDefinition = EndpointsDefinition


@dataclass
class MetadataDefinition(BaseModel):
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
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
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
_MetadataDefinition = MetadataDefinition


@dataclass
class EndpointConfigDefinition(BaseModel):
    IsPublicIpEnabled: Optional[bool]
    NsgIds: Optional[Sequence[str]]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IsPublicIpEnabled=json_data.get("IsPublicIpEnabled"),
            NsgIds=json_data.get("NsgIds"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigDefinition = EndpointConfigDefinition


@dataclass
class ImagePolicyConfigDefinition(BaseModel):
    IsPolicyEnabled: Optional[bool]
    KeyDetails: Optional[Sequence["_KeyDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImagePolicyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImagePolicyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IsPolicyEnabled=json_data.get("IsPolicyEnabled"),
            KeyDetails=deserialize_list(json_data.get("KeyDetails"), KeyDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImagePolicyConfigDefinition = ImagePolicyConfigDefinition


@dataclass
class KeyDetailsDefinition(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDetailsDefinition = KeyDetailsDefinition


@dataclass
class OptionsDefinition(BaseModel):
    ServiceLbSubnetIds: Optional[Sequence[str]]
    AddOns: Optional[Sequence["_AddOnsDefinition"]]
    AdmissionControllerOptions: Optional[Sequence["_AdmissionControllerOptionsDefinition"]]
    KubernetesNetworkConfig: Optional[Sequence["_KubernetesNetworkConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ServiceLbSubnetIds=json_data.get("ServiceLbSubnetIds"),
            AddOns=deserialize_list(json_data.get("AddOns"), AddOnsDefinition),
            AdmissionControllerOptions=deserialize_list(json_data.get("AdmissionControllerOptions"), AdmissionControllerOptionsDefinition),
            KubernetesNetworkConfig=deserialize_list(json_data.get("KubernetesNetworkConfig"), KubernetesNetworkConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class AddOnsDefinition(BaseModel):
    IsKubernetesDashboardEnabled: Optional[bool]
    IsTillerEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AddOnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddOnsDefinition"]:
        if not json_data:
            return None
        return cls(
            IsKubernetesDashboardEnabled=json_data.get("IsKubernetesDashboardEnabled"),
            IsTillerEnabled=json_data.get("IsTillerEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddOnsDefinition = AddOnsDefinition


@dataclass
class AdmissionControllerOptionsDefinition(BaseModel):
    IsPodSecurityPolicyEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdmissionControllerOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdmissionControllerOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            IsPodSecurityPolicyEnabled=json_data.get("IsPodSecurityPolicyEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdmissionControllerOptionsDefinition = AdmissionControllerOptionsDefinition


@dataclass
class KubernetesNetworkConfigDefinition(BaseModel):
    PodsCidr: Optional[str]
    ServicesCidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesNetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesNetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PodsCidr=json_data.get("PodsCidr"),
            ServicesCidr=json_data.get("ServicesCidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesNetworkConfigDefinition = KubernetesNetworkConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


