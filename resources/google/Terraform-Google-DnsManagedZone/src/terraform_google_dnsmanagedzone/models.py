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
    Description: Optional[str]
    DnsName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    NameServers: Optional[Sequence[str]]
    Project: Optional[str]
    Visibility: Optional[str]
    DnssecConfig: Optional[Sequence["_DnssecConfig"]]
    PrivateVisibilityConfig: Optional[Sequence["_PrivateVisibilityConfig"]]
    Timeouts: Optional["_Timeouts"]
    DefaultKeySpecs: Optional[Sequence["_DefaultKeySpecs"]]
    Networks: Optional[Sequence["_Networks"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DnsName=json_data.get("DnsName"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            NameServers=json_data.get("NameServers"),
            Project=json_data.get("Project"),
            Visibility=json_data.get("Visibility"),
            DnssecConfig=json_data.get("DnssecConfig"),
            PrivateVisibilityConfig=json_data.get("PrivateVisibilityConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            DefaultKeySpecs=json_data.get("DefaultKeySpecs"),
            Networks=json_data.get("Networks"),
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
class DnssecConfig:
    Kind: Optional[str]
    NonExistence: Optional[str]
    State: Optional[str]
    DefaultKeySpecs: Optional[Sequence["_DefaultKeySpecs"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnssecConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnssecConfig"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            NonExistence=json_data.get("NonExistence"),
            State=json_data.get("State"),
            DefaultKeySpecs=json_data.get("DefaultKeySpecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnssecConfig = DnssecConfig


@dataclass
class DefaultKeySpecs:
    Algorithm: Optional[str]
    KeyLength: Optional[float]
    KeyType: Optional[str]
    Kind: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultKeySpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultKeySpecs"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            KeyLength=json_data.get("KeyLength"),
            KeyType=json_data.get("KeyType"),
            Kind=json_data.get("Kind"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultKeySpecs = DefaultKeySpecs


@dataclass
class PrivateVisibilityConfig:
    Networks: Optional[Sequence["_Networks"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateVisibilityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateVisibilityConfig"]:
        if not json_data:
            return None
        return cls(
            Networks=json_data.get("Networks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateVisibilityConfig = PrivateVisibilityConfig


@dataclass
class Networks:
    NetworkUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Networks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Networks"]:
        if not json_data:
            return None
        return cls(
            NetworkUrl=json_data.get("NetworkUrl"),
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


