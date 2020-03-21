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
    CreateTime: Optional[str]
    Description: Optional[str]
    Etag: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Project: Optional[str]
    Tier: Optional[str]
    Zone: Optional[str]
    FileShares: Optional[Sequence["_FileShares"]]
    Networks: Optional[Sequence["_Networks"]]
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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Tier=json_data.get("Tier"),
            Zone=json_data.get("Zone"),
            FileShares=json_data.get("FileShares"),
            Networks=json_data.get("Networks"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class FileShares:
    CapacityGb: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileShares"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileShares"]:
        if not json_data:
            return None
        return cls(
            CapacityGb=json_data.get("CapacityGb"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileShares = FileShares


@dataclass
class Networks:
    Modes: Optional[Sequence[str]]
    Network: Optional[str]
    ReservedIpRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Networks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Networks"]:
        if not json_data:
            return None
        return cls(
            Modes=json_data.get("Modes"),
            Network=json_data.get("Network"),
            ReservedIpRange=json_data.get("ReservedIpRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Networks = Networks


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


