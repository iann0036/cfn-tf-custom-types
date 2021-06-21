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
    Arn: Optional[str]
    CatalogId: Optional[str]
    ClassName: Optional[str]
    CreateTime: Optional[str]
    DatabaseName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OwnerName: Optional[str]
    OwnerType: Optional[str]
    ResourceUris: Optional[Sequence["_ResourceUrisDefinition"]]

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
            Arn=json_data.get("Arn"),
            CatalogId=json_data.get("CatalogId"),
            ClassName=json_data.get("ClassName"),
            CreateTime=json_data.get("CreateTime"),
            DatabaseName=json_data.get("DatabaseName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OwnerName=json_data.get("OwnerName"),
            OwnerType=json_data.get("OwnerType"),
            ResourceUris=deserialize_list(json_data.get("ResourceUris"), ResourceUrisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceUrisDefinition(BaseModel):
    ResourceType: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceUrisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceUrisDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceUrisDefinition = ResourceUrisDefinition

