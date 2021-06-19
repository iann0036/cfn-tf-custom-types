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
    ActivationState: Optional[str]
    AliasCount: Optional[float]
    Comment: Optional[str]
    Contract: Optional[str]
    EndCustomerId: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Masters: Optional[Sequence[str]]
    SignAndServe: Optional[bool]
    SignAndServeAlgorithm: Optional[str]
    Target: Optional[str]
    Type: Optional[str]
    VersionId: Optional[str]
    Zone: Optional[str]
    TsigKey: Optional[Sequence["_TsigKeyDefinition"]]

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
            ActivationState=json_data.get("ActivationState"),
            AliasCount=json_data.get("AliasCount"),
            Comment=json_data.get("Comment"),
            Contract=json_data.get("Contract"),
            EndCustomerId=json_data.get("EndCustomerId"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Masters=json_data.get("Masters"),
            SignAndServe=json_data.get("SignAndServe"),
            SignAndServeAlgorithm=json_data.get("SignAndServeAlgorithm"),
            Target=json_data.get("Target"),
            Type=json_data.get("Type"),
            VersionId=json_data.get("VersionId"),
            Zone=json_data.get("Zone"),
            TsigKey=deserialize_list(json_data.get("TsigKey"), TsigKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TsigKeyDefinition(BaseModel):
    Algorithm: Optional[str]
    Name: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TsigKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TsigKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Name=json_data.get("Name"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TsigKeyDefinition = TsigKeyDefinition


