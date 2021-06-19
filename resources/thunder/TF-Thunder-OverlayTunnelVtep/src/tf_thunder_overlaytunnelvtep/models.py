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
    Encap: Optional[str]
    Id: Optional[str]
    Id2: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    DestinationIpAddressList: Optional[Sequence["_DestinationIpAddressListDefinition"]]
    HostList: Optional[Sequence["_HostListDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]
    SourceIpAddress: Optional[Sequence["_SourceIpAddressDefinition"]]

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
            Encap=json_data.get("Encap"),
            Id=json_data.get("Id"),
            Id2=json_data.get("Id2"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            DestinationIpAddressList=deserialize_list(json_data.get("DestinationIpAddressList"), DestinationIpAddressListDefinition),
            HostList=deserialize_list(json_data.get("HostList"), HostListDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
            SourceIpAddress=deserialize_list(json_data.get("SourceIpAddress"), SourceIpAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationIpAddressListDefinition(BaseModel):
    Encap: Optional[str]
    IpAddress: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    VniList: Optional[Sequence["_VniListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationIpAddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationIpAddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            Encap=json_data.get("Encap"),
            IpAddress=json_data.get("IpAddress"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            VniList=deserialize_list(json_data.get("VniList"), VniListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationIpAddressListDefinition = DestinationIpAddressListDefinition


@dataclass
class VniListDefinition(BaseModel):
    Segment: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VniListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VniListDefinition"]:
        if not json_data:
            return None
        return cls(
            Segment=json_data.get("Segment"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VniListDefinition = VniListDefinition


@dataclass
class HostListDefinition(BaseModel):
    DestinationVtep: Optional[str]
    IpAddr: Optional[str]
    OverlayMacAddr: Optional[str]
    Uuid: Optional[str]
    Vni: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostListDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationVtep=json_data.get("DestinationVtep"),
            IpAddr=json_data.get("IpAddr"),
            OverlayMacAddr=json_data.get("OverlayMacAddr"),
            Uuid=json_data.get("Uuid"),
            Vni=json_data.get("Vni"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostListDefinition = HostListDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


@dataclass
class SourceIpAddressDefinition(BaseModel):
    IpAddress: Optional[str]
    Uuid: Optional[str]
    VniList: Optional[Sequence["_VniListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceIpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceIpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            Uuid=json_data.get("Uuid"),
            VniList=deserialize_list(json_data.get("VniList"), VniListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceIpAddressDefinition = SourceIpAddressDefinition


