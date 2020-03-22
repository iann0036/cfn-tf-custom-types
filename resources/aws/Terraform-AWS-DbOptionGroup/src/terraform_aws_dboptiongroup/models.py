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
    Arn: Optional[str]
    EngineName: Optional[str]
    Id: Optional[str]
    MajorEngineVersion: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    OptionGroupDescription: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Option: Optional[Sequence["_Option"]]
    Timeouts: Optional["_Timeouts"]
    OptionSettings: Optional[Sequence["_OptionSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            EngineName=json_data.get("EngineName"),
            Id=json_data.get("Id"),
            MajorEngineVersion=json_data.get("MajorEngineVersion"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            OptionGroupDescription=json_data.get("OptionGroupDescription"),
            Tags=json_data.get("Tags"),
            Option=json_data.get("Option"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            OptionSettings=json_data.get("OptionSettings"),
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
class Option:
    DbSecurityGroupMemberships: Optional[Sequence[str]]
    OptionName: Optional[str]
    Port: Optional[float]
    Version: Optional[str]
    VpcSecurityGroupMemberships: Optional[Sequence[str]]
    OptionSettings: Optional[Sequence["_OptionSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_Option"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Option"]:
        if not json_data:
            return None
        return cls(
            DbSecurityGroupMemberships=json_data.get("DbSecurityGroupMemberships"),
            OptionName=json_data.get("OptionName"),
            Port=json_data.get("Port"),
            Version=json_data.get("Version"),
            VpcSecurityGroupMemberships=json_data.get("VpcSecurityGroupMemberships"),
            OptionSettings=json_data.get("OptionSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Option = Option


@dataclass
class OptionSettings:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionSettings"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionSettings = OptionSettings


@dataclass
class Timeouts:
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


