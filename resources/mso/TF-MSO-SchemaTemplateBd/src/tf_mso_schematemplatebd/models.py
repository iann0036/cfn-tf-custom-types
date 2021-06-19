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
    DhcpPolicy: Optional[Sequence["_DhcpPolicyDefinition"]]
    DisplayName: Optional[str]
    Id: Optional[str]
    IntersiteBumTraffic: Optional[bool]
    Layer2Stretch: Optional[bool]
    Layer2UnknownUnicast: Optional[str]
    Layer3Multicast: Optional[bool]
    Name: Optional[str]
    OptimizeWanBandwidth: Optional[bool]
    SchemaId: Optional[str]
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
            DhcpPolicy=deserialize_list(json_data.get("DhcpPolicy"), DhcpPolicyDefinition),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IntersiteBumTraffic=json_data.get("IntersiteBumTraffic"),
            Layer2Stretch=json_data.get("Layer2Stretch"),
            Layer2UnknownUnicast=json_data.get("Layer2UnknownUnicast"),
            Layer3Multicast=json_data.get("Layer3Multicast"),
            Name=json_data.get("Name"),
            OptimizeWanBandwidth=json_data.get("OptimizeWanBandwidth"),
            SchemaId=json_data.get("SchemaId"),
            TemplateName=json_data.get("TemplateName"),
            VrfName=json_data.get("VrfName"),
            VrfSchemaId=json_data.get("VrfSchemaId"),
            VrfTemplateName=json_data.get("VrfTemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DhcpPolicyDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpPolicyDefinition = DhcpPolicyDefinition


