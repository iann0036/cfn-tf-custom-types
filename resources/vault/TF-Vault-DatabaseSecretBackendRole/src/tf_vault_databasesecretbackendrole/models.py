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
    Backend: Optional[str]
    CreationStatements: Optional[Sequence[str]]
    DbName: Optional[str]
    DefaultTtl: Optional[float]
    Id: Optional[str]
    MaxTtl: Optional[float]
    Name: Optional[str]
    RenewStatements: Optional[Sequence[str]]
    RevocationStatements: Optional[Sequence[str]]
    RollbackStatements: Optional[Sequence[str]]

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
            Backend=json_data.get("Backend"),
            CreationStatements=json_data.get("CreationStatements"),
            DbName=json_data.get("DbName"),
            DefaultTtl=json_data.get("DefaultTtl"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            Name=json_data.get("Name"),
            RenewStatements=json_data.get("RenewStatements"),
            RevocationStatements=json_data.get("RevocationStatements"),
            RollbackStatements=json_data.get("RollbackStatements"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


