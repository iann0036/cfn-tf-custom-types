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
    Description: Optional[str]
    DeviceGroup: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Vsys: Optional[str]
    FileProperty: Optional[Sequence["_FilePropertyDefinition"]]
    PredefinedPattern: Optional[Sequence["_PredefinedPatternDefinition"]]
    Regex: Optional[Sequence["_RegexDefinition"]]

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
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Vsys=json_data.get("Vsys"),
            FileProperty=deserialize_list(json_data.get("FileProperty"), FilePropertyDefinition),
            PredefinedPattern=deserialize_list(json_data.get("PredefinedPattern"), PredefinedPatternDefinition),
            Regex=deserialize_list(json_data.get("Regex"), RegexDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilePropertyDefinition(BaseModel):
    FileProperty: Optional[str]
    FileType: Optional[str]
    Name: Optional[str]
    PropertyValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilePropertyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilePropertyDefinition"]:
        if not json_data:
            return None
        return cls(
            FileProperty=json_data.get("FileProperty"),
            FileType=json_data.get("FileType"),
            Name=json_data.get("Name"),
            PropertyValue=json_data.get("PropertyValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilePropertyDefinition = FilePropertyDefinition


@dataclass
class PredefinedPatternDefinition(BaseModel):
    FileTypes: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedPatternDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedPatternDefinition"]:
        if not json_data:
            return None
        return cls(
            FileTypes=json_data.get("FileTypes"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedPatternDefinition = PredefinedPatternDefinition


@dataclass
class RegexDefinition(BaseModel):
    FileTypes: Optional[Sequence[str]]
    Name: Optional[str]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexDefinition"]:
        if not json_data:
            return None
        return cls(
            FileTypes=json_data.get("FileTypes"),
            Name=json_data.get("Name"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexDefinition = RegexDefinition


