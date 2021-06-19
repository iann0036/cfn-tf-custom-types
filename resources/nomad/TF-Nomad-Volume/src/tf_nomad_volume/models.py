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
    AccessMode: Optional[str]
    AttachmentMode: Optional[str]
    Context: Optional[Sequence["_ContextDefinition"]]
    ControllerRequired: Optional[bool]
    ControllersExpected: Optional[float]
    ControllersHealthy: Optional[float]
    DeregisterOnDestroy: Optional[bool]
    ExternalId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    NodesExpected: Optional[float]
    NodesHealthy: Optional[float]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    PluginId: Optional[str]
    PluginProvider: Optional[str]
    PluginProviderVersion: Optional[str]
    Schedulable: Optional[bool]
    Secrets: Optional[Sequence["_SecretsDefinition"]]
    Type: Optional[str]
    VolumeId: Optional[str]
    Capability: Optional[Sequence["_CapabilityDefinition"]]
    MountOptions: Optional[Sequence["_MountOptionsDefinition"]]

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
            AccessMode=json_data.get("AccessMode"),
            AttachmentMode=json_data.get("AttachmentMode"),
            Context=deserialize_list(json_data.get("Context"), ContextDefinition),
            ControllerRequired=json_data.get("ControllerRequired"),
            ControllersExpected=json_data.get("ControllersExpected"),
            ControllersHealthy=json_data.get("ControllersHealthy"),
            DeregisterOnDestroy=json_data.get("DeregisterOnDestroy"),
            ExternalId=json_data.get("ExternalId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NodesExpected=json_data.get("NodesExpected"),
            NodesHealthy=json_data.get("NodesHealthy"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            PluginId=json_data.get("PluginId"),
            PluginProvider=json_data.get("PluginProvider"),
            PluginProviderVersion=json_data.get("PluginProviderVersion"),
            Schedulable=json_data.get("Schedulable"),
            Secrets=deserialize_list(json_data.get("Secrets"), SecretsDefinition),
            Type=json_data.get("Type"),
            VolumeId=json_data.get("VolumeId"),
            Capability=deserialize_list(json_data.get("Capability"), CapabilityDefinition),
            MountOptions=deserialize_list(json_data.get("MountOptions"), MountOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContextDefinition = ContextDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class SecretsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretsDefinition = SecretsDefinition


@dataclass
class CapabilityDefinition(BaseModel):
    AccessMode: Optional[str]
    AttachmentMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapabilityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapabilityDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessMode=json_data.get("AccessMode"),
            AttachmentMode=json_data.get("AttachmentMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapabilityDefinition = CapabilityDefinition


@dataclass
class MountOptionsDefinition(BaseModel):
    FsType: Optional[str]
    MountFlags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MountOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            MountFlags=json_data.get("MountFlags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountOptionsDefinition = MountOptionsDefinition


