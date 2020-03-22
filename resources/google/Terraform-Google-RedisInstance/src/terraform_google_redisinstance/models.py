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
    AlternativeLocationId: Optional[str]
    AuthorizedNetwork: Optional[str]
    CreateTime: Optional[str]
    CurrentLocationId: Optional[str]
    DisplayName: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    LocationId: Optional[str]
    MemorySizeGb: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Project: Optional[str]
    RedisConfigs: Optional[Sequence["_RedisConfigs"]]
    RedisVersion: Optional[str]
    Region: Optional[str]
    ReservedIpRange: Optional[str]
    Tier: Optional[str]
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
            AlternativeLocationId=json_data.get("AlternativeLocationId"),
            AuthorizedNetwork=json_data.get("AuthorizedNetwork"),
            CreateTime=json_data.get("CreateTime"),
            CurrentLocationId=json_data.get("CurrentLocationId"),
            DisplayName=json_data.get("DisplayName"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LocationId=json_data.get("LocationId"),
            MemorySizeGb=json_data.get("MemorySizeGb"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Project=json_data.get("Project"),
            RedisConfigs=json_data.get("RedisConfigs"),
            RedisVersion=json_data.get("RedisVersion"),
            Region=json_data.get("Region"),
            ReservedIpRange=json_data.get("ReservedIpRange"),
            Tier=json_data.get("Tier"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class RedisConfigs:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedisConfigs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisConfigs"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisConfigs = RedisConfigs


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


