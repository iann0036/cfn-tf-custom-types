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
    ActivationFile: Optional[str]
    AdminNetworkCidr: Optional[str]
    CloudControlPlaneServer1: Optional[str]
    CloudControlPlaneServer2: Optional[str]
    CompartmentId: Optional[str]
    CorporateProxy: Optional[str]
    CpusEnabled: Optional[float]
    DataStorageSizeInTbs: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    DnsServer: Optional[Sequence[str]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Gateway: Optional[str]
    Id: Optional[str]
    InfiniBandNetworkCidr: Optional[str]
    LifecycleDetails: Optional[str]
    Netmask: Optional[str]
    NtpServer: Optional[Sequence[str]]
    Shape: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeZone: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActivationFile=json_data.get("ActivationFile"),
            AdminNetworkCidr=json_data.get("AdminNetworkCidr"),
            CloudControlPlaneServer1=json_data.get("CloudControlPlaneServer1"),
            CloudControlPlaneServer2=json_data.get("CloudControlPlaneServer2"),
            CompartmentId=json_data.get("CompartmentId"),
            CorporateProxy=json_data.get("CorporateProxy"),
            CpusEnabled=json_data.get("CpusEnabled"),
            DataStorageSizeInTbs=json_data.get("DataStorageSizeInTbs"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            DnsServer=json_data.get("DnsServer"),
            FreeformTags=json_data.get("FreeformTags"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            InfiniBandNetworkCidr=json_data.get("InfiniBandNetworkCidr"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Netmask=json_data.get("Netmask"),
            NtpServer=json_data.get("NtpServer"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeZone=json_data.get("TimeZone"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


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


