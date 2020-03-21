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
    ConfigurationParameters: Optional[Sequence["_ConfigurationParameters"]]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Values: Optional[Sequence["_Values"]]
    Datastore: Optional[Sequence["_Datastore"]]
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
            ConfigurationParameters=json_data.get("ConfigurationParameters"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
            Datastore=json_data.get("Datastore"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigurationParameters:
    Description: Optional[str]
    Name: Optional[str]
    Readonly: Optional[bool]
    RestartRequired: Optional[bool]
    Type: Optional[str]
    Value: Optional[str]
    ValueRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationParameters"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Readonly=json_data.get("Readonly"),
            RestartRequired=json_data.get("RestartRequired"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            ValueRange=json_data.get("ValueRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationParameters = ConfigurationParameters


@dataclass
class Values:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Values"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Values"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Values = Values


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


