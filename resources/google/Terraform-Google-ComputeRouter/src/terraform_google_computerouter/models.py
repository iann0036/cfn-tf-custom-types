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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    Bgp: Optional[Sequence["_Bgp"]]
    Timeouts: Optional["_Timeouts"]
    AdvertisedIpRanges: Optional[Sequence["_AdvertisedIpRanges"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Bgp=json_data.get("Bgp"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            AdvertisedIpRanges=json_data.get("AdvertisedIpRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Bgp:
    AdvertiseMode: Optional[str]
    AdvertisedGroups: Optional[Sequence[str]]
    Asn: Optional[float]
    AdvertisedIpRanges: Optional[Sequence["_AdvertisedIpRanges"]]

    @classmethod
    def _deserialize(
        cls: Type["_Bgp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bgp"]:
        if not json_data:
            return None
        return cls(
            AdvertiseMode=json_data.get("AdvertiseMode"),
            AdvertisedGroups=json_data.get("AdvertisedGroups"),
            Asn=json_data.get("Asn"),
            AdvertisedIpRanges=json_data.get("AdvertisedIpRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bgp = Bgp


@dataclass
class AdvertisedIpRanges:
    Description: Optional[str]
    Range: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertisedIpRanges"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertisedIpRanges"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Range=json_data.get("Range"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertisedIpRanges = AdvertisedIpRanges


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


