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
    ExternalIp: Optional[str]
    ExternalPort: Optional[str]
    ForwardEntryId: Optional[str]
    ForwardEntryName: Optional[str]
    ForwardTableId: Optional[str]
    Id: Optional[str]
    InternalIp: Optional[str]
    InternalPort: Optional[str]
    IpProtocol: Optional[str]
    Name: Optional[str]
    PortBreak: Optional[bool]
    Status: Optional[str]
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
            ExternalIp=json_data.get("ExternalIp"),
            ExternalPort=json_data.get("ExternalPort"),
            ForwardEntryId=json_data.get("ForwardEntryId"),
            ForwardEntryName=json_data.get("ForwardEntryName"),
            ForwardTableId=json_data.get("ForwardTableId"),
            Id=json_data.get("Id"),
            InternalIp=json_data.get("InternalIp"),
            InternalPort=json_data.get("InternalPort"),
            IpProtocol=json_data.get("IpProtocol"),
            Name=json_data.get("Name"),
            PortBreak=json_data.get("PortBreak"),
            Status=json_data.get("Status"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


