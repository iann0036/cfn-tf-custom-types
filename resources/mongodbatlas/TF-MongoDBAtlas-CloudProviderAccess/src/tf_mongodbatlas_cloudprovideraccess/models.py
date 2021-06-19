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
    AtlasAssumedRoleExternalId: Optional[str]
    AtlasAwsAccountArn: Optional[str]
    AuthorizedDate: Optional[str]
    CreatedDate: Optional[str]
    FeatureUsages: Optional[Sequence["_FeatureUsagesDefinition"]]
    IamAssumedRoleArn: Optional[str]
    Id: Optional[str]
    ProjectId: Optional[str]
    ProviderName: Optional[str]
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
            AtlasAssumedRoleExternalId=json_data.get("AtlasAssumedRoleExternalId"),
            AtlasAwsAccountArn=json_data.get("AtlasAwsAccountArn"),
            AuthorizedDate=json_data.get("AuthorizedDate"),
            CreatedDate=json_data.get("CreatedDate"),
            FeatureUsages=deserialize_list(json_data.get("FeatureUsages"), FeatureUsagesDefinition),
            IamAssumedRoleArn=json_data.get("IamAssumedRoleArn"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            ProviderName=json_data.get("ProviderName"),
            RoleId=json_data.get("RoleId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


