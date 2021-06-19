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
    CompartmentId: Optional[str]
    ConsumptionModel: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IdcsAt: Optional[str]
    InstanceUrl: Optional[str]
    IntegrationInstanceType: Optional[str]
    IsByol: Optional[bool]
    IsFileServerEnabled: Optional[bool]
    IsVisualBuilderEnabled: Optional[bool]
    MessagePacks: Optional[float]
    State: Optional[str]
    StateMessage: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    AlternateCustomEndpoints: Optional[Sequence["_AlternateCustomEndpointsDefinition"]]
    CustomEndpoint: Optional[Sequence["_CustomEndpointDefinition"]]
    NetworkEndpointDetails: Optional[Sequence["_NetworkEndpointDetailsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            ConsumptionModel=json_data.get("ConsumptionModel"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IdcsAt=json_data.get("IdcsAt"),
            InstanceUrl=json_data.get("InstanceUrl"),
            IntegrationInstanceType=json_data.get("IntegrationInstanceType"),
            IsByol=json_data.get("IsByol"),
            IsFileServerEnabled=json_data.get("IsFileServerEnabled"),
            IsVisualBuilderEnabled=json_data.get("IsVisualBuilderEnabled"),
            MessagePacks=json_data.get("MessagePacks"),
            State=json_data.get("State"),
            StateMessage=json_data.get("StateMessage"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            AlternateCustomEndpoints=deserialize_list(json_data.get("AlternateCustomEndpoints"), AlternateCustomEndpointsDefinition),
            CustomEndpoint=deserialize_list(json_data.get("CustomEndpoint"), CustomEndpointDefinition),
            NetworkEndpointDetails=deserialize_list(json_data.get("NetworkEndpointDetails"), NetworkEndpointDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class AlternateCustomEndpointsDefinition(BaseModel):
    CertificateSecretId: Optional[str]
    Hostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlternateCustomEndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlternateCustomEndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSecretId=json_data.get("CertificateSecretId"),
            Hostname=json_data.get("Hostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlternateCustomEndpointsDefinition = AlternateCustomEndpointsDefinition


@dataclass
class CustomEndpointDefinition(BaseModel):
    CertificateSecretId: Optional[str]
    Hostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSecretId=json_data.get("CertificateSecretId"),
            Hostname=json_data.get("Hostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEndpointDefinition = CustomEndpointDefinition


@dataclass
class NetworkEndpointDetailsDefinition(BaseModel):
    AllowlistedHttpIps: Optional[Sequence[str]]
    IsIntegrationVcnAllowlisted: Optional[bool]
    NetworkEndpointType: Optional[str]
    AllowlistedHttpVcns: Optional[Sequence["_AllowlistedHttpVcnsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkEndpointDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkEndpointDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowlistedHttpIps=json_data.get("AllowlistedHttpIps"),
            IsIntegrationVcnAllowlisted=json_data.get("IsIntegrationVcnAllowlisted"),
            NetworkEndpointType=json_data.get("NetworkEndpointType"),
            AllowlistedHttpVcns=deserialize_list(json_data.get("AllowlistedHttpVcns"), AllowlistedHttpVcnsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkEndpointDetailsDefinition = NetworkEndpointDetailsDefinition


@dataclass
class AllowlistedHttpVcnsDefinition(BaseModel):
    AllowlistedIps: Optional[Sequence[str]]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowlistedHttpVcnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowlistedHttpVcnsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowlistedIps=json_data.get("AllowlistedIps"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowlistedHttpVcnsDefinition = AllowlistedHttpVcnsDefinition


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


