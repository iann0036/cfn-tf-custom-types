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
    AnpSchemaId: Optional[str]
    AnpTemplateName: Optional[str]
    DisplayName: Optional[str]
    ExternalEpgName: Optional[str]
    ExternalEpgType: Optional[str]
    Id: Optional[str]
    IncludeInPreferredGroup: Optional[bool]
    L3outName: Optional[str]
    L3outSchemaId: Optional[str]
    L3outTemplateName: Optional[str]
    SchemaId: Optional[str]
    SelectorIp: Optional[str]
    SelectorName: Optional[str]
    SiteId: Optional[Sequence[str]]
    TemplateName: Optional[str]
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
            AnpSchemaId=json_data.get("AnpSchemaId"),
            AnpTemplateName=json_data.get("AnpTemplateName"),
            DisplayName=json_data.get("DisplayName"),
            ExternalEpgName=json_data.get("ExternalEpgName"),
            ExternalEpgType=json_data.get("ExternalEpgType"),
            Id=json_data.get("Id"),
            IncludeInPreferredGroup=json_data.get("IncludeInPreferredGroup"),
            L3outName=json_data.get("L3outName"),
            L3outSchemaId=json_data.get("L3outSchemaId"),
            L3outTemplateName=json_data.get("L3outTemplateName"),
            SchemaId=json_data.get("SchemaId"),
            SelectorIp=json_data.get("SelectorIp"),
            SelectorName=json_data.get("SelectorName"),
            SiteId=json_data.get("SiteId"),
            TemplateName=json_data.get("TemplateName"),
            VrfName=json_data.get("VrfName"),
            VrfSchemaId=json_data.get("VrfSchemaId"),
            VrfTemplateName=json_data.get("VrfTemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


