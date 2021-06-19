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
    FirewallArn: Optional[str]
    Id: Optional[str]
    LoggingConfiguration: Optional[Sequence["_LoggingConfigurationDefinition"]]

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
            FirewallArn=json_data.get("FirewallArn"),
            Id=json_data.get("Id"),
            LoggingConfiguration=deserialize_list(json_data.get("LoggingConfiguration"), LoggingConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoggingConfigurationDefinition(BaseModel):
    LogDestinationConfig: Optional[Sequence["_LogDestinationConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            LogDestinationConfig=deserialize_list(json_data.get("LogDestinationConfig"), LogDestinationConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfigurationDefinition = LoggingConfigurationDefinition


@dataclass
class LogDestinationConfigDefinition(BaseModel):
    LogDestination: Optional[Sequence["_LogDestinationDefinition"]]
    LogDestinationType: Optional[str]
    LogType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogDestinationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDestinationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LogDestination=deserialize_list(json_data.get("LogDestination"), LogDestinationDefinition),
            LogDestinationType=json_data.get("LogDestinationType"),
            LogType=json_data.get("LogType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDestinationConfigDefinition = LogDestinationConfigDefinition


@dataclass
class LogDestinationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDestinationDefinition = LogDestinationDefinition


