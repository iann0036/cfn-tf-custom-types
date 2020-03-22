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
    Databases: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Role: Optional[str]
    ServerName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    PartnerServers: Optional[Sequence["_PartnerServers"]]
    ReadWriteEndpointFailoverPolicy: Optional[Sequence["_ReadWriteEndpointFailoverPolicy"]]
    ReadonlyEndpointFailoverPolicy: Optional[Sequence["_ReadonlyEndpointFailoverPolicy"]]
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
            Databases=json_data.get("Databases"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Role=json_data.get("Role"),
            ServerName=json_data.get("ServerName"),
            Tags=json_data.get("Tags"),
            PartnerServers=json_data.get("PartnerServers"),
            ReadWriteEndpointFailoverPolicy=json_data.get("ReadWriteEndpointFailoverPolicy"),
            ReadonlyEndpointFailoverPolicy=json_data.get("ReadonlyEndpointFailoverPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class PartnerServers:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartnerServers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartnerServers"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartnerServers = PartnerServers


@dataclass
class ReadWriteEndpointFailoverPolicy:
    GraceMinutes: Optional[float]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadWriteEndpointFailoverPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadWriteEndpointFailoverPolicy"]:
        if not json_data:
            return None
        return cls(
            GraceMinutes=json_data.get("GraceMinutes"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadWriteEndpointFailoverPolicy = ReadWriteEndpointFailoverPolicy


@dataclass
class ReadonlyEndpointFailoverPolicy:
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadonlyEndpointFailoverPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadonlyEndpointFailoverPolicy"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadonlyEndpointFailoverPolicy = ReadonlyEndpointFailoverPolicy


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


