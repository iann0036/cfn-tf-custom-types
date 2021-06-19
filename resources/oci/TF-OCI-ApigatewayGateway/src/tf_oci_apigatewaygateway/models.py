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
    CertificateId: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    EndpointType: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Hostname: Optional[str]
    Id: Optional[str]
    IpAddresses: Optional[Sequence["_IpAddressesDefinition"]]
    LifecycleDetails: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    ResponseCacheDetails: Optional[Sequence["_ResponseCacheDetailsDefinition"]]
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
            CertificateId=json_data.get("CertificateId"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            EndpointType=json_data.get("EndpointType"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IpAddresses=deserialize_list(json_data.get("IpAddresses"), IpAddressesDefinition),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            ResponseCacheDetails=deserialize_list(json_data.get("ResponseCacheDetails"), ResponseCacheDetailsDefinition),
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
class IpAddressesDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressesDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressesDefinition = IpAddressesDefinition


@dataclass
class ResponseCacheDetailsDefinition(BaseModel):
    AuthenticationSecretId: Optional[str]
    AuthenticationSecretVersionNumber: Optional[str]
    ConnectTimeoutInMs: Optional[float]
    IsSslEnabled: Optional[bool]
    IsSslVerifyDisabled: Optional[bool]
    ReadTimeoutInMs: Optional[float]
    SendTimeoutInMs: Optional[float]
    Type: Optional[str]
    Servers: Optional[Sequence["_ServersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseCacheDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseCacheDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationSecretId=json_data.get("AuthenticationSecretId"),
            AuthenticationSecretVersionNumber=json_data.get("AuthenticationSecretVersionNumber"),
            ConnectTimeoutInMs=json_data.get("ConnectTimeoutInMs"),
            IsSslEnabled=json_data.get("IsSslEnabled"),
            IsSslVerifyDisabled=json_data.get("IsSslVerifyDisabled"),
            ReadTimeoutInMs=json_data.get("ReadTimeoutInMs"),
            SendTimeoutInMs=json_data.get("SendTimeoutInMs"),
            Type=json_data.get("Type"),
            Servers=deserialize_list(json_data.get("Servers"), ServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseCacheDetailsDefinition = ResponseCacheDetailsDefinition


@dataclass
class ServersDefinition(BaseModel):
    Host: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServersDefinition = ServersDefinition


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


