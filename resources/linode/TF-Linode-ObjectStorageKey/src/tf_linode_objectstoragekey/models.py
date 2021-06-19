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
    AccessKey: Optional[str]
    Id: Optional[str]
    Label: Optional[str]
    Limited: Optional[bool]
    SecretKey: Optional[str]
    BucketAccess: Optional[Sequence["_BucketAccessDefinition"]]

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
            AccessKey=json_data.get("AccessKey"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Limited=json_data.get("Limited"),
            SecretKey=json_data.get("SecretKey"),
            BucketAccess=deserialize_list(json_data.get("BucketAccess"), BucketAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BucketAccessDefinition(BaseModel):
    BucketName: Optional[str]
    Cluster: Optional[str]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BucketAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Cluster=json_data.get("Cluster"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketAccessDefinition = BucketAccessDefinition


