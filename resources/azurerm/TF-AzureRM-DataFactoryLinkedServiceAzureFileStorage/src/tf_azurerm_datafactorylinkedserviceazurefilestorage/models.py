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
    AdditionalProperties: Optional[Sequence["_AdditionalPropertiesDefinition"]]
    Annotations: Optional[Sequence[str]]
    ConnectionString: Optional[str]
    DataFactoryName: Optional[str]
    Description: Optional[str]
    FileShare: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    IntegrationRuntimeName: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    Password: Optional[str]
    ResourceGroupName: Optional[str]
    UserId: Optional[str]
    KeyVaultPassword: Optional[Sequence["_KeyVaultPasswordDefinition"]]
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
            AdditionalProperties=deserialize_list(json_data.get("AdditionalProperties"), AdditionalPropertiesDefinition),
            Annotations=json_data.get("Annotations"),
            ConnectionString=json_data.get("ConnectionString"),
            DataFactoryName=json_data.get("DataFactoryName"),
            Description=json_data.get("Description"),
            FileShare=json_data.get("FileShare"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            IntegrationRuntimeName=json_data.get("IntegrationRuntimeName"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Password=json_data.get("Password"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            UserId=json_data.get("UserId"),
            KeyVaultPassword=deserialize_list(json_data.get("KeyVaultPassword"), KeyVaultPasswordDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalPropertiesDefinition = AdditionalPropertiesDefinition


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
class KeyVaultPasswordDefinition(BaseModel):
    LinkedServiceName: Optional[str]
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyVaultPasswordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyVaultPasswordDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkedServiceName=json_data.get("LinkedServiceName"),
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyVaultPasswordDefinition = KeyVaultPasswordDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition

