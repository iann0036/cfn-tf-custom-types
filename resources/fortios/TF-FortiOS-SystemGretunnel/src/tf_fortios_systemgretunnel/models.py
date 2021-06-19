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
    ChecksumReception: Optional[str]
    ChecksumTransmission: Optional[str]
    Diffservcode: Optional[str]
    DscpCopying: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    IpVersion: Optional[str]
    KeepaliveFailtimes: Optional[float]
    KeepaliveInterval: Optional[float]
    KeyInbound: Optional[float]
    KeyOutbound: Optional[float]
    LocalGw: Optional[str]
    LocalGw6: Optional[str]
    Name: Optional[str]
    RemoteGw: Optional[str]
    RemoteGw6: Optional[str]
    SequenceNumberReception: Optional[str]
    SequenceNumberTransmission: Optional[str]
    Vdomparam: Optional[str]

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
            ChecksumReception=json_data.get("ChecksumReception"),
            ChecksumTransmission=json_data.get("ChecksumTransmission"),
            Diffservcode=json_data.get("Diffservcode"),
            DscpCopying=json_data.get("DscpCopying"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpVersion=json_data.get("IpVersion"),
            KeepaliveFailtimes=json_data.get("KeepaliveFailtimes"),
            KeepaliveInterval=json_data.get("KeepaliveInterval"),
            KeyInbound=json_data.get("KeyInbound"),
            KeyOutbound=json_data.get("KeyOutbound"),
            LocalGw=json_data.get("LocalGw"),
            LocalGw6=json_data.get("LocalGw6"),
            Name=json_data.get("Name"),
            RemoteGw=json_data.get("RemoteGw"),
            RemoteGw6=json_data.get("RemoteGw6"),
            SequenceNumberReception=json_data.get("SequenceNumberReception"),
            SequenceNumberTransmission=json_data.get("SequenceNumberTransmission"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


