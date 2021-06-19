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
    AppImageConfigName: Optional[str]
    Arn: Optional[str]
    Id: Optional[str]
    KernelGatewayImageConfig: Optional[Sequence["_KernelGatewayImageConfigDefinition"]]

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
            AppImageConfigName=json_data.get("AppImageConfigName"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            KernelGatewayImageConfig=deserialize_list(json_data.get("KernelGatewayImageConfig"), KernelGatewayImageConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KernelGatewayImageConfigDefinition(BaseModel):
    FileSystemConfig: Optional[Sequence["_FileSystemConfigDefinition"]]
    KernelSpec: Optional[Sequence["_KernelSpecDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KernelGatewayImageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelGatewayImageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FileSystemConfig=deserialize_list(json_data.get("FileSystemConfig"), FileSystemConfigDefinition),
            KernelSpec=deserialize_list(json_data.get("KernelSpec"), KernelSpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelGatewayImageConfigDefinition = KernelGatewayImageConfigDefinition


@dataclass
class FileSystemConfigDefinition(BaseModel):
    DefaultGid: Optional[float]
    DefaultUid: Optional[float]
    MountPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystemConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystemConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultGid=json_data.get("DefaultGid"),
            DefaultUid=json_data.get("DefaultUid"),
            MountPath=json_data.get("MountPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystemConfigDefinition = FileSystemConfigDefinition


@dataclass
class KernelSpecDefinition(BaseModel):
    DisplayName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KernelSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelSpecDefinition = KernelSpecDefinition


