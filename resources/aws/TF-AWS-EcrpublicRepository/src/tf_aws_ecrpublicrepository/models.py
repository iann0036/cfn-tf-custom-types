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
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    RegistryId: Optional[str]
    RepositoryName: Optional[str]
    RepositoryUri: Optional[str]
    CatalogData: Optional[Sequence["_CatalogDataDefinition"]]
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
            Arn=json_data.get("Arn"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            RegistryId=json_data.get("RegistryId"),
            RepositoryName=json_data.get("RepositoryName"),
            RepositoryUri=json_data.get("RepositoryUri"),
            CatalogData=deserialize_list(json_data.get("CatalogData"), CatalogDataDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CatalogDataDefinition(BaseModel):
    AboutText: Optional[str]
    Architectures: Optional[Sequence[str]]
    Description: Optional[str]
    LogoImageBlob: Optional[str]
    OperatingSystems: Optional[Sequence[str]]
    UsageText: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AboutText=json_data.get("AboutText"),
            Architectures=json_data.get("Architectures"),
            Description=json_data.get("Description"),
            LogoImageBlob=json_data.get("LogoImageBlob"),
            OperatingSystems=json_data.get("OperatingSystems"),
            UsageText=json_data.get("UsageText"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogDataDefinition = CatalogDataDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


