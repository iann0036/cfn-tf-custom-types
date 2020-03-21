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
    AttachmentType: Optional[str]
    AvailabilityDomain: Optional[str]
    ChapSecret: Optional[str]
    ChapUsername: Optional[str]
    CompartmentId: Optional[str]
    Device: Optional[str]
    DisplayName: Optional[str]
    InstanceId: Optional[str]
    Ipv4: Optional[str]
    Iqn: Optional[str]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    IsReadOnly: Optional[bool]
    IsShareable: Optional[bool]
    Port: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    UseChap: Optional[bool]
    VolumeId: Optional[str]
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
            AttachmentType=json_data.get("AttachmentType"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            ChapSecret=json_data.get("ChapSecret"),
            ChapUsername=json_data.get("ChapUsername"),
            CompartmentId=json_data.get("CompartmentId"),
            Device=json_data.get("Device"),
            DisplayName=json_data.get("DisplayName"),
            InstanceId=json_data.get("InstanceId"),
            Ipv4=json_data.get("Ipv4"),
            Iqn=json_data.get("Iqn"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            IsReadOnly=json_data.get("IsReadOnly"),
            IsShareable=json_data.get("IsShareable"),
            Port=json_data.get("Port"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            UseChap=json_data.get("UseChap"),
            VolumeId=json_data.get("VolumeId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


