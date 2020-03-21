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
    CodeChecksum: Optional[str]
    Description: Optional[str]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariables"]]
    Filename: Optional[str]
    FunctionId: Optional[str]
    Handler: Optional[str]
    LastModified: Optional[str]
    MemorySize: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    OssBucket: Optional[str]
    OssKey: Optional[str]
    Runtime: Optional[str]
    Service: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CodeChecksum=json_data.get("CodeChecksum"),
            Description=json_data.get("Description"),
            EnvironmentVariables=json_data.get("EnvironmentVariables"),
            Filename=json_data.get("Filename"),
            FunctionId=json_data.get("FunctionId"),
            Handler=json_data.get("Handler"),
            LastModified=json_data.get("LastModified"),
            MemorySize=json_data.get("MemorySize"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            OssBucket=json_data.get("OssBucket"),
            OssKey=json_data.get("OssKey"),
            Runtime=json_data.get("Runtime"),
            Service=json_data.get("Service"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentVariables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariables = EnvironmentVariables


