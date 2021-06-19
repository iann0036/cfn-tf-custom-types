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
    AuthorizedDate: Optional[str]
    Aws: Optional[Sequence["_AwsDefinition"]]
    FeatureUsages: Optional[Sequence["_FeatureUsagesDefinition"]]
    Id: Optional[str]
    ProjectId: Optional[str]
    RoleId: Optional[str]

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
            AuthorizedDate=json_data.get("AuthorizedDate"),
            Aws=deserialize_list(json_data.get("Aws"), AwsDefinition),
            FeatureUsages=deserialize_list(json_data.get("FeatureUsages"), FeatureUsagesDefinition),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            RoleId=json_data.get("RoleId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDefinition = AwsDefinition


@dataclass
class FeatureUsagesDefinition(BaseModel):
    FeatureId: Optional[str]
    FeatureType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureUsagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureUsagesDefinition"]:
        if not json_data:
            return None
        return cls(
            FeatureId=json_data.get("FeatureId"),
            FeatureType=json_data.get("FeatureType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureUsagesDefinition = FeatureUsagesDefinition


