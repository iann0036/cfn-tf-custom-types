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
    Id: Optional[str]
    PublishedHostname: Optional[str]
    PublishedPath: Optional[str]
    ServiceProfile: Optional[str]
    Shortname: Optional[str]
    SourceHostname: Optional[str]
    SourcePath: Optional[str]
    VersionNumber: Optional[float]
    ProtocolSet: Optional[Sequence["_ProtocolSetDefinition"]]

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
            Id=json_data.get("Id"),
            PublishedHostname=json_data.get("PublishedHostname"),
            PublishedPath=json_data.get("PublishedPath"),
            ServiceProfile=json_data.get("ServiceProfile"),
            Shortname=json_data.get("Shortname"),
            SourceHostname=json_data.get("SourceHostname"),
            SourcePath=json_data.get("SourcePath"),
            VersionNumber=json_data.get("VersionNumber"),
            ProtocolSet=deserialize_list(json_data.get("ProtocolSet"), ProtocolSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProtocolSetDefinition(BaseModel):
    PublishedProtocol: Optional[str]
    SourcePort: Optional[float]
    SourceProtocol: Optional[str]
    Option: Optional[Sequence["_OptionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolSetDefinition"]:
        if not json_data:
            return None
        return cls(
            PublishedProtocol=json_data.get("PublishedProtocol"),
            SourcePort=json_data.get("SourcePort"),
            SourceProtocol=json_data.get("SourceProtocol"),
            Option=deserialize_list(json_data.get("Option"), OptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolSetDefinition = ProtocolSetDefinition


@dataclass
class OptionDefinition(BaseModel):
    Name: Optional[str]
    Parameters: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionDefinition = OptionDefinition


