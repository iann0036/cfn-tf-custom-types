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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    Name: Optional[str]
    Nameservers: Optional[Sequence["_Nameservers"]]
    Self: Optional[str]
    Serial: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    Version: Optional[str]
    ZoneType: Optional[str]
    ExternalMasters: Optional[Sequence["_ExternalMasters"]]
    Timeouts: Optional["_Timeouts"]
    Tsig: Optional[Sequence["_Tsig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Nameservers=json_data.get("Nameservers"),
            Self=json_data.get("Self"),
            Serial=json_data.get("Serial"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Version=json_data.get("Version"),
            ZoneType=json_data.get("ZoneType"),
            ExternalMasters=json_data.get("ExternalMasters"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Tsig=json_data.get("Tsig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Nameservers:
    Hostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nameservers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nameservers"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nameservers = Nameservers


@dataclass
class ExternalMasters:
    Address: Optional[str]
    Port: Optional[float]
    TsigKeyId: Optional[str]
    Tsig: Optional[Sequence["_Tsig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalMasters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalMasters"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            TsigKeyId=json_data.get("TsigKeyId"),
            Tsig=json_data.get("Tsig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalMasters = ExternalMasters


@dataclass
class Tsig:
    Algorithm: Optional[str]
    Name: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tsig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tsig"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Name=json_data.get("Name"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tsig = Tsig


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


