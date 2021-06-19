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
    Id: Optional[str]
    IsActive: Optional[bool]
    LimitDateRangeFrom: Optional[str]
    LimitDateRangeTo: Optional[str]
    LimitNumClients: Optional[float]
    LimitNumDownloads: Optional[float]
    LimitPackageQuery: Optional[str]
    LimitPathQuery: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    Repository: Optional[str]
    Token: Optional[str]

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
            Id=json_data.get("Id"),
            IsActive=json_data.get("IsActive"),
            LimitDateRangeFrom=json_data.get("LimitDateRangeFrom"),
            LimitDateRangeTo=json_data.get("LimitDateRangeTo"),
            LimitNumClients=json_data.get("LimitNumClients"),
            LimitNumDownloads=json_data.get("LimitNumDownloads"),
            LimitPackageQuery=json_data.get("LimitPackageQuery"),
            LimitPathQuery=json_data.get("LimitPathQuery"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Repository=json_data.get("Repository"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


