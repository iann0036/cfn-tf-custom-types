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
    Description: Optional[str]
    Destination: Optional[str]
    Disabled: Optional[bool]
    Filter: Optional[str]
    Id: Optional[str]
    IncludeChildren: Optional[bool]
    Name: Optional[str]
    OrgId: Optional[str]
    WriterIdentity: Optional[str]
    BigqueryOptions: Optional[Sequence["_BigqueryOptionsDefinition"]]
    Exclusions: Optional[Sequence["_ExclusionsDefinition"]]

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
            Description=json_data.get("Description"),
            Destination=json_data.get("Destination"),
            Disabled=json_data.get("Disabled"),
            Filter=json_data.get("Filter"),
            Id=json_data.get("Id"),
            IncludeChildren=json_data.get("IncludeChildren"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            WriterIdentity=json_data.get("WriterIdentity"),
            BigqueryOptions=deserialize_list(json_data.get("BigqueryOptions"), BigqueryOptionsDefinition),
            Exclusions=deserialize_list(json_data.get("Exclusions"), ExclusionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BigqueryOptionsDefinition(BaseModel):
    UsePartitionedTables: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            UsePartitionedTables=json_data.get("UsePartitionedTables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryOptionsDefinition = BigqueryOptionsDefinition


@dataclass
class ExclusionsDefinition(BaseModel):
    Description: Optional[str]
    Disabled: Optional[bool]
    Filter: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Filter=json_data.get("Filter"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionsDefinition = ExclusionsDefinition


