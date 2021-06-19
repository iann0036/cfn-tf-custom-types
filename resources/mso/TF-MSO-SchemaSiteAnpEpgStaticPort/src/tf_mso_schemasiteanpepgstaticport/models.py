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
    DeploymentImmediacy: Optional[str]
    EpgName: Optional[str]
    Fex: Optional[str]
    Id: Optional[str]
    Leaf: Optional[str]
    MicroSegVlan: Optional[float]
    Mode: Optional[str]
    Path: Optional[str]
    PathType: Optional[str]
    Pod: Optional[str]
    SchemaId: Optional[str]
    SiteId: Optional[str]
    TemplateName: Optional[str]
    Vlan: Optional[float]

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
            DeploymentImmediacy=json_data.get("DeploymentImmediacy"),
            EpgName=json_data.get("EpgName"),
            Fex=json_data.get("Fex"),
            Id=json_data.get("Id"),
            Leaf=json_data.get("Leaf"),
            MicroSegVlan=json_data.get("MicroSegVlan"),
            Mode=json_data.get("Mode"),
            Path=json_data.get("Path"),
            PathType=json_data.get("PathType"),
            Pod=json_data.get("Pod"),
            SchemaId=json_data.get("SchemaId"),
            SiteId=json_data.get("SiteId"),
            TemplateName=json_data.get("TemplateName"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


