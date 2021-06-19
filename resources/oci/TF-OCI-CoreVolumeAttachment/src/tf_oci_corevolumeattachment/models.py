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
    AttachmentType: Optional[str]
    AvailabilityDomain: Optional[str]
    ChapSecret: Optional[str]
    ChapUsername: Optional[str]
    CompartmentId: Optional[str]
    Device: Optional[str]
    DisplayName: Optional[str]
    EncryptionInTransitType: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    Ipv4: Optional[str]
    Iqn: Optional[str]
    IsMultipath: Optional[bool]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    IsReadOnly: Optional[bool]
    IsShareable: Optional[bool]
    IscsiLoginState: Optional[str]
    MultipathDevices: Optional[Sequence["_MultipathDevicesDefinition"]]
    Port: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    UseChap: Optional[bool]
    VolumeId: Optional[str]
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
            AttachmentType=json_data.get("AttachmentType"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            ChapSecret=json_data.get("ChapSecret"),
            ChapUsername=json_data.get("ChapUsername"),
            CompartmentId=json_data.get("CompartmentId"),
            Device=json_data.get("Device"),
            DisplayName=json_data.get("DisplayName"),
            EncryptionInTransitType=json_data.get("EncryptionInTransitType"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            Ipv4=json_data.get("Ipv4"),
            Iqn=json_data.get("Iqn"),
            IsMultipath=json_data.get("IsMultipath"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            IsReadOnly=json_data.get("IsReadOnly"),
            IsShareable=json_data.get("IsShareable"),
            IscsiLoginState=json_data.get("IscsiLoginState"),
            MultipathDevices=deserialize_list(json_data.get("MultipathDevices"), MultipathDevicesDefinition),
            Port=json_data.get("Port"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            UseChap=json_data.get("UseChap"),
            VolumeId=json_data.get("VolumeId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MultipathDevicesDefinition(BaseModel):
    Ipv4: Optional[str]
    Iqn: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MultipathDevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultipathDevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=json_data.get("Ipv4"),
            Iqn=json_data.get("Iqn"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultipathDevicesDefinition = MultipathDevicesDefinition


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


