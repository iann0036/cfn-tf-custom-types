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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    Bgp: Optional[Sequence["_BgpDefinition"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            Bgp=deserialize_list(json_data.get("Bgp"), BgpDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BgpDefinition(BaseModel):
    AdvertiseMode: Optional[str]
    AdvertisedGroups: Optional[Sequence[str]]
    Asn: Optional[float]
    AdvertisedIpRanges: Optional[Sequence["_AdvertisedIpRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BgpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseMode=json_data.get("AdvertiseMode"),
            AdvertisedGroups=json_data.get("AdvertisedGroups"),
            Asn=json_data.get("Asn"),
            AdvertisedIpRanges=deserialize_list(json_data.get("AdvertisedIpRanges"), AdvertisedIpRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpDefinition = BgpDefinition


@dataclass
class AdvertisedIpRangesDefinition(BaseModel):
    Description: Optional[str]
    Range: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertisedIpRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertisedIpRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Range=json_data.get("Range"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertisedIpRangesDefinition = AdvertisedIpRangesDefinition


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


