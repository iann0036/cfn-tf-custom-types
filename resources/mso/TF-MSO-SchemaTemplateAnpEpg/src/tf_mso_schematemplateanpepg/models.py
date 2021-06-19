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
    BdName: Optional[str]
    BdSchemaId: Optional[str]
    BdTemplateName: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IntersiteMulticastSource: Optional[bool]
    IntraEpg: Optional[str]
    Name: Optional[str]
    PreferredGroup: Optional[bool]
    ProxyArp: Optional[bool]
    SchemaId: Optional[str]
    TemplateName: Optional[str]
    UsegEpg: Optional[bool]
    VrfName: Optional[str]
    VrfSchemaId: Optional[str]
    VrfTemplateName: Optional[str]

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
            BdName=json_data.get("BdName"),
            BdSchemaId=json_data.get("BdSchemaId"),
            BdTemplateName=json_data.get("BdTemplateName"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IntersiteMulticastSource=json_data.get("IntersiteMulticastSource"),
            IntraEpg=json_data.get("IntraEpg"),
            Name=json_data.get("Name"),
            PreferredGroup=json_data.get("PreferredGroup"),
            ProxyArp=json_data.get("ProxyArp"),
            SchemaId=json_data.get("SchemaId"),
            TemplateName=json_data.get("TemplateName"),
            UsegEpg=json_data.get("UsegEpg"),
            VrfName=json_data.get("VrfName"),
            VrfSchemaId=json_data.get("VrfSchemaId"),
            VrfTemplateName=json_data.get("VrfTemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


