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
    AwsKms: Optional[Sequence["_AwsKmsDefinition"]]
    AzureKeyVault: Optional[Sequence["_AzureKeyVaultDefinition"]]
    GoogleCloudKms: Optional[Sequence["_GoogleCloudKmsDefinition"]]
    Id: Optional[str]
    ProjectId: Optional[str]

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
            AwsKms=deserialize_list(json_data.get("AwsKms"), AwsKmsDefinition),
            AzureKeyVault=deserialize_list(json_data.get("AzureKeyVault"), AzureKeyVaultDefinition),
            GoogleCloudKms=deserialize_list(json_data.get("GoogleCloudKms"), GoogleCloudKmsDefinition),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsKmsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKmsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKmsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKmsDefinition = AwsKmsDefinition


@dataclass
class AzureKeyVaultDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureKeyVaultDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureKeyVaultDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureKeyVaultDefinition = AzureKeyVaultDefinition


@dataclass
class GoogleCloudKmsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleCloudKmsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleCloudKmsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleCloudKmsDefinition = GoogleCloudKmsDefinition


