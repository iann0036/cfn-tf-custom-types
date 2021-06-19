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
    Accprofile: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdom: Optional[Sequence[str]]
    Trusthost: Optional[Sequence["_TrusthostDefinition"]]

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
            Accprofile=json_data.get("Accprofile"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdom=json_data.get("Vdom"),
            Trusthost=deserialize_list(json_data.get("Trusthost"), TrusthostDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TrusthostDefinition(BaseModel):
    Ipv4Trusthost: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrusthostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrusthostDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Trusthost=json_data.get("Ipv4Trusthost"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrusthostDefinition = TrusthostDefinition


