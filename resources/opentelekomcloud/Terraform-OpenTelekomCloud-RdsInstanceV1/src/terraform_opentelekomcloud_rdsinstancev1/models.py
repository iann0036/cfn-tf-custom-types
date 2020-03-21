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
    Availabilityzone: Optional[str]
    Created: Optional[str]
    Dbport: Optional[str]
    Dbrtpd: Optional[str]
    Flavorref: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Tag: Optional[Sequence["_Tag"]]
    Type: Optional[str]
    Updated: Optional[str]
    Vpc: Optional[str]
    Backupstrategy: Optional[Sequence["_Backupstrategy"]]
    Datastore: Optional[Sequence["_Datastore"]]
    Ha: Optional[Sequence["_Ha"]]
    Nics: Optional[Sequence["_Nics"]]
    Securitygroup: Optional[Sequence["_Securitygroup"]]
    Timeouts: Optional["_Timeouts"]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Availabilityzone=json_data.get("Availabilityzone"),
            Created=json_data.get("Created"),
            Dbport=json_data.get("Dbport"),
            Dbrtpd=json_data.get("Dbrtpd"),
            Flavorref=json_data.get("Flavorref"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Type=json_data.get("Type"),
            Updated=json_data.get("Updated"),
            Vpc=json_data.get("Vpc"),
            Backupstrategy=json_data.get("Backupstrategy"),
            Datastore=json_data.get("Datastore"),
            Ha=json_data.get("Ha"),
            Nics=json_data.get("Nics"),
            Securitygroup=json_data.get("Securitygroup"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tag:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class Backupstrategy:
    Keepdays: Optional[float]
    Starttime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Backupstrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backupstrategy"]:
        if not json_data:
            return None
        return cls(
            Keepdays=json_data.get("Keepdays"),
            Starttime=json_data.get("Starttime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backupstrategy = Backupstrategy


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
class Ha:
    Enable: Optional[bool]
    Replicationmode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ha"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ha"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Replicationmode=json_data.get("Replicationmode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ha = Ha


@dataclass
class Nics:
    Subnetid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nics"]:
        if not json_data:
            return None
        return cls(
            Subnetid=json_data.get("Subnetid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nics = Nics


@dataclass
class Securitygroup:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Securitygroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Securitygroup"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Securitygroup = Securitygroup


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
class Volume:
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


