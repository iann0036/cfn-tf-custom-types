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
    ConfigId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastModified: Optional[str]
    AllowedPublishers: Optional[Sequence["_AllowedPublishersDefinition"]]
    Policies: Optional[Sequence["_PoliciesDefinition"]]

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
            ConfigId=json_data.get("ConfigId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastModified=json_data.get("LastModified"),
            AllowedPublishers=deserialize_list(json_data.get("AllowedPublishers"), AllowedPublishersDefinition),
            Policies=deserialize_list(json_data.get("Policies"), PoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowedPublishersDefinition(BaseModel):
    SigningProfileVersionArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedPublishersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedPublishersDefinition"]:
        if not json_data:
            return None
        return cls(
            SigningProfileVersionArns=json_data.get("SigningProfileVersionArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedPublishersDefinition = AllowedPublishersDefinition


@dataclass
class PoliciesDefinition(BaseModel):
    UntrustedArtifactOnDeployment: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            UntrustedArtifactOnDeployment=json_data.get("UntrustedArtifactOnDeployment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoliciesDefinition = PoliciesDefinition


