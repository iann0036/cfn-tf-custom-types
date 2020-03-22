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
    AddressScopeId: Optional[str]
    AllTags: Optional[Sequence[str]]
    CreatedAt: Optional[str]
    DefaultPrefixlen: Optional[float]
    DefaultQuota: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    IpVersion: Optional[float]
    IsDefault: Optional[bool]
    MaxPrefixlen: Optional[float]
    MinPrefixlen: Optional[float]
    Name: Optional[str]
    Prefixes: Optional[Sequence[str]]
    ProjectId: Optional[str]
    Region: Optional[str]
    RevisionNumber: Optional[float]
    Shared: Optional[bool]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
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
            AddressScopeId=json_data.get("AddressScopeId"),
            AllTags=json_data.get("AllTags"),
            CreatedAt=json_data.get("CreatedAt"),
            DefaultPrefixlen=json_data.get("DefaultPrefixlen"),
            DefaultQuota=json_data.get("DefaultQuota"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpVersion=json_data.get("IpVersion"),
            IsDefault=json_data.get("IsDefault"),
            MaxPrefixlen=json_data.get("MaxPrefixlen"),
            MinPrefixlen=json_data.get("MinPrefixlen"),
            Name=json_data.get("Name"),
            Prefixes=json_data.get("Prefixes"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            RevisionNumber=json_data.get("RevisionNumber"),
            Shared=json_data.get("Shared"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            ValueSpecs=json_data.get("ValueSpecs"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


