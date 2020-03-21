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
    ConfigurationId: Optional[str]
    FlavorId: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Size: Optional[float]
    Database: Optional[Sequence["_Database"]]
    Datastore: Optional[Sequence["_Datastore"]]
    Network: Optional[Sequence["_Network"]]
    Timeouts: Optional["_Timeouts"]
    User: Optional[Sequence["_User"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConfigurationId=json_data.get("ConfigurationId"),
            FlavorId=json_data.get("FlavorId"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            Database=json_data.get("Database"),
            Datastore=json_data.get("Datastore"),
            Network=json_data.get("Network"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Database:
    Charset: Optional[str]
    Collate: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Database"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Database"]:
        if not json_data:
            return None
        return cls(
            Charset=json_data.get("Charset"),
            Collate=json_data.get("Collate"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Database = Database


@dataclass
class Datastore:
    Type: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Datastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Datastore"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Datastore = Datastore


@dataclass
class Network:
    FixedIpV4: Optional[str]
    FixedIpV6: Optional[str]
    Port: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            FixedIpV4=json_data.get("FixedIpV4"),
            FixedIpV6=json_data.get("FixedIpV6"),
            Port=json_data.get("Port"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


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


@dataclass
class User:
    Databases: Optional[Sequence[str]]
    Host: Optional[str]
    Name: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_User"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_User"]:
        if not json_data:
            return None
        return cls(
            Databases=json_data.get("Databases"),
            Host=json_data.get("Host"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_User = User


