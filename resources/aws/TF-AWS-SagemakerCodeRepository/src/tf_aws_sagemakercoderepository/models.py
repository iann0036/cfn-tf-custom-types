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
    CodeRepositoryName: Optional[str]
    Id: Optional[str]
    GitConfig: Optional[Sequence["_GitConfigDefinition"]]

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
            CodeRepositoryName=json_data.get("CodeRepositoryName"),
            Id=json_data.get("Id"),
            GitConfig=deserialize_list(json_data.get("GitConfig"), GitConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GitConfigDefinition(BaseModel):
    Branch: Optional[str]
    RepositoryUrl: Optional[str]
    SecretArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            RepositoryUrl=json_data.get("RepositoryUrl"),
            SecretArn=json_data.get("SecretArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitConfigDefinition = GitConfigDefinition


