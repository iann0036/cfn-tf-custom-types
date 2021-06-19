# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    EngineName: Optional[str]
    Id: Optional[str]
    MajorEngineVersion: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    OptionGroupDescription: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Option: Optional[Sequence["_OptionDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            EngineName=json_data.get("EngineName"),
            Id=json_data.get("Id"),
            MajorEngineVersion=json_data.get("MajorEngineVersion"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            OptionGroupDescription=json_data.get("OptionGroupDescription"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Option=deserialize_list(json_data.get("Option"), OptionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class OptionDefinition(BaseModel):
    DbSecurityGroupMemberships: Optional[Sequence[str]]
    OptionName: Optional[str]
    Port: Optional[float]
    Version: Optional[str]
    VpcSecurityGroupMemberships: Optional[Sequence[str]]
    OptionSettings: Optional[Sequence["_OptionSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionDefinition"]:
        if not json_data:
            return None
        return cls(
            DbSecurityGroupMemberships=json_data.get("DbSecurityGroupMemberships"),
            OptionName=json_data.get("OptionName"),
            Port=json_data.get("Port"),
            Version=json_data.get("Version"),
            VpcSecurityGroupMemberships=json_data.get("VpcSecurityGroupMemberships"),
            OptionSettings=deserialize_list(json_data.get("OptionSettings"), OptionSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionDefinition = OptionDefinition


@dataclass
class OptionSettingsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionSettingsDefinition = OptionSettingsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


