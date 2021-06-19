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
    Apn: Optional[str]
    BlockTrafficOtherEndUserDomains: Optional[bool]
    BlockTrafficThisEndUserDomain: Optional[bool]
    Color: Optional[str]
    Comments: Optional[str]
    EndUserDomain: Optional[str]
    EnforceEndUserDomain: Optional[bool]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]

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
            Apn=json_data.get("Apn"),
            BlockTrafficOtherEndUserDomains=json_data.get("BlockTrafficOtherEndUserDomains"),
            BlockTrafficThisEndUserDomain=json_data.get("BlockTrafficThisEndUserDomain"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            EndUserDomain=json_data.get("EndUserDomain"),
            EnforceEndUserDomain=json_data.get("EnforceEndUserDomain"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


