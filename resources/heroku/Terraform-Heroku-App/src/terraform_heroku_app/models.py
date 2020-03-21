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
    Acm: Optional[bool]
    AllConfigVars: Optional[Sequence["_AllConfigVars"]]
    Buildpacks: Optional[Sequence[str]]
    ConfigVars: Optional[Sequence["_ConfigVars"]]
    GitUrl: Optional[str]
    HerokuHostname: Optional[str]
    InternalRouting: Optional[bool]
    Name: Optional[str]
    Region: Optional[str]
    SensitiveConfigVars: Optional[Sequence["_SensitiveConfigVars"]]
    Space: Optional[str]
    Stack: Optional[str]
    Uuid: Optional[str]
    WebUrl: Optional[str]
    Organization: Optional[Sequence["_Organization"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Acm=json_data.get("Acm"),
            AllConfigVars=json_data.get("AllConfigVars"),
            Buildpacks=json_data.get("Buildpacks"),
            ConfigVars=json_data.get("ConfigVars"),
            GitUrl=json_data.get("GitUrl"),
            HerokuHostname=json_data.get("HerokuHostname"),
            InternalRouting=json_data.get("InternalRouting"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SensitiveConfigVars=json_data.get("SensitiveConfigVars"),
            Space=json_data.get("Space"),
            Stack=json_data.get("Stack"),
            Uuid=json_data.get("Uuid"),
            WebUrl=json_data.get("WebUrl"),
            Organization=json_data.get("Organization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllConfigVars:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllConfigVars"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllConfigVars"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllConfigVars = AllConfigVars


@dataclass
class ConfigVars:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigVars"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigVars"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigVars = ConfigVars


@dataclass
class SensitiveConfigVars:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SensitiveConfigVars"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitiveConfigVars"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitiveConfigVars = SensitiveConfigVars


@dataclass
class Organization:
    Locked: Optional[bool]
    Name: Optional[str]
    Personal: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Organization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Organization"]:
        if not json_data:
            return None
        return cls(
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            Personal=json_data.get("Personal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Organization = Organization


