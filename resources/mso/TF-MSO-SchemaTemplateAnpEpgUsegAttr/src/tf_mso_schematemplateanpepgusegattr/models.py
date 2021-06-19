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
    AnpName: Optional[str]
    Category: Optional[str]
    Description: Optional[str]
    EpgName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Operator: Optional[str]
    SchemaId: Optional[str]
    TemplateName: Optional[str]
    UsegSubnet: Optional[bool]
    UsegType: Optional[str]
    Value: Optional[str]

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
            AnpName=json_data.get("AnpName"),
            Category=json_data.get("Category"),
            Description=json_data.get("Description"),
            EpgName=json_data.get("EpgName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Operator=json_data.get("Operator"),
            SchemaId=json_data.get("SchemaId"),
            TemplateName=json_data.get("TemplateName"),
            UsegSubnet=json_data.get("UsegSubnet"),
            UsegType=json_data.get("UsegType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


