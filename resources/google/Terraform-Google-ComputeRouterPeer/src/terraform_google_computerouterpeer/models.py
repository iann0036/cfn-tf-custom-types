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
    AdvertiseMode: Optional[str]
    AdvertisedGroups: Optional[Sequence[str]]
    AdvertisedRoutePriority: Optional[float]
    Interface: Optional[str]
    IpAddress: Optional[str]
    ManagementType: Optional[str]
    Name: Optional[str]
    PeerAsn: Optional[float]
    PeerIpAddress: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Router: Optional[str]
    AdvertisedIpRanges: Optional[Sequence["_AdvertisedIpRanges"]]
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
            AdvertiseMode=json_data.get("AdvertiseMode"),
            AdvertisedGroups=json_data.get("AdvertisedGroups"),
            AdvertisedRoutePriority=json_data.get("AdvertisedRoutePriority"),
            Interface=json_data.get("Interface"),
            IpAddress=json_data.get("IpAddress"),
            ManagementType=json_data.get("ManagementType"),
            Name=json_data.get("Name"),
            PeerAsn=json_data.get("PeerAsn"),
            PeerIpAddress=json_data.get("PeerIpAddress"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Router=json_data.get("Router"),
            AdvertisedIpRanges=json_data.get("AdvertisedIpRanges"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


