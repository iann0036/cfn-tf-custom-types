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
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Subnet: Optional[str]
    Uuid: Optional[str]
    Device: Optional[Sequence["_DeviceDefinition"]]
    Link: Optional[Sequence["_LinkDefinition"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Subnet=json_data.get("Subnet"),
            Uuid=json_data.get("Uuid"),
            Device=deserialize_list(json_data.get("Device"), DeviceDefinition),
            Link=deserialize_list(json_data.get("Link"), LinkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeviceDefinition(BaseModel):
    Asn: Optional[float]
    Id: Optional[str]
    InterfaceId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            Id=json_data.get("Id"),
            InterfaceId=json_data.get("InterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceDefinition = DeviceDefinition


@dataclass
class LinkDefinition(BaseModel):
    AccountNumber: Optional[str]
    DstMetroCode: Optional[str]
    DstZoneCode: Optional[str]
    SrcMetroCode: Optional[str]
    SrcZoneCode: Optional[str]
    Throughput: Optional[str]
    ThroughputUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountNumber=json_data.get("AccountNumber"),
            DstMetroCode=json_data.get("DstMetroCode"),
            DstZoneCode=json_data.get("DstZoneCode"),
            SrcMetroCode=json_data.get("SrcMetroCode"),
            SrcZoneCode=json_data.get("SrcZoneCode"),
            Throughput=json_data.get("Throughput"),
            ThroughputUnit=json_data.get("ThroughputUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkDefinition = LinkDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


