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
    CaPort: Optional[float]
    CodeChecksum: Optional[str]
    Description: Optional[str]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition"]]
    Filename: Optional[str]
    FunctionId: Optional[str]
    Handler: Optional[str]
    Id: Optional[str]
    InitializationTimeout: Optional[float]
    Initializer: Optional[str]
    InstanceConcurrency: Optional[float]
    InstanceType: Optional[str]
    LastModified: Optional[str]
    MemorySize: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    OssBucket: Optional[str]
    OssKey: Optional[str]
    Runtime: Optional[str]
    Service: Optional[str]
    Timeout: Optional[float]
    CustomContainerConfig: Optional[Sequence["_CustomContainerConfigDefinition"]]

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
            CaPort=json_data.get("CaPort"),
            CodeChecksum=json_data.get("CodeChecksum"),
            Description=json_data.get("Description"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition),
            Filename=json_data.get("Filename"),
            FunctionId=json_data.get("FunctionId"),
            Handler=json_data.get("Handler"),
            Id=json_data.get("Id"),
            InitializationTimeout=json_data.get("InitializationTimeout"),
            Initializer=json_data.get("Initializer"),
            InstanceConcurrency=json_data.get("InstanceConcurrency"),
            InstanceType=json_data.get("InstanceType"),
            LastModified=json_data.get("LastModified"),
            MemorySize=json_data.get("MemorySize"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            OssBucket=json_data.get("OssBucket"),
            OssKey=json_data.get("OssKey"),
            Runtime=json_data.get("Runtime"),
            Service=json_data.get("Service"),
            Timeout=json_data.get("Timeout"),
            CustomContainerConfig=deserialize_list(json_data.get("CustomContainerConfig"), CustomContainerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariablesDefinition = EnvironmentVariablesDefinition


@dataclass
class CustomContainerConfigDefinition(BaseModel):
    Args: Optional[str]
    Command: Optional[str]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomContainerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomContainerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Command=json_data.get("Command"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomContainerConfigDefinition = CustomContainerConfigDefinition


