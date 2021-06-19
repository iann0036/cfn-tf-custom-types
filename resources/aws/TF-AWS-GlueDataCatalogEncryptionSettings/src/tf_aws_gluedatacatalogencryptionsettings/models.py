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
    CatalogId: Optional[str]
    Id: Optional[str]
    DataCatalogEncryptionSettings: Optional[Sequence["_DataCatalogEncryptionSettingsDefinition"]]

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
            CatalogId=json_data.get("CatalogId"),
            Id=json_data.get("Id"),
            DataCatalogEncryptionSettings=deserialize_list(json_data.get("DataCatalogEncryptionSettings"), DataCatalogEncryptionSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DataCatalogEncryptionSettingsDefinition(BaseModel):
    ConnectionPasswordEncryption: Optional[Sequence["_ConnectionPasswordEncryptionDefinition"]]
    EncryptionAtRest: Optional[Sequence["_EncryptionAtRestDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataCatalogEncryptionSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCatalogEncryptionSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionPasswordEncryption=deserialize_list(json_data.get("ConnectionPasswordEncryption"), ConnectionPasswordEncryptionDefinition),
            EncryptionAtRest=deserialize_list(json_data.get("EncryptionAtRest"), EncryptionAtRestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCatalogEncryptionSettingsDefinition = DataCatalogEncryptionSettingsDefinition


@dataclass
class ConnectionPasswordEncryptionDefinition(BaseModel):
    AwsKmsKeyId: Optional[str]
    ReturnConnectionPasswordEncrypted: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionPasswordEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionPasswordEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsKmsKeyId=json_data.get("AwsKmsKeyId"),
            ReturnConnectionPasswordEncrypted=json_data.get("ReturnConnectionPasswordEncrypted"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionPasswordEncryptionDefinition = ConnectionPasswordEncryptionDefinition


@dataclass
class EncryptionAtRestDefinition(BaseModel):
    CatalogEncryptionMode: Optional[str]
    SseAwsKmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionAtRestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionAtRestDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogEncryptionMode=json_data.get("CatalogEncryptionMode"),
            SseAwsKmsKeyId=json_data.get("SseAwsKmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionAtRestDefinition = EncryptionAtRestDefinition


