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
    Addr: Optional[str]
    AddrTCtrl: Optional[str]
    AllowedSelfAsCnt: Optional[str]
    Annotation: Optional[str]
    AsNumber: Optional[str]
    Ctrl: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LocalAsn: Optional[str]
    LocalAsnPropagate: Optional[str]
    LogicalNodeProfileDn: Optional[str]
    NameAlias: Optional[str]
    Password: Optional[str]
    PeerCtrl: Optional[str]
    PrivateASctrl: Optional[str]
    RelationBgpRsPeerPfxPol: Optional[str]
    Ttl: Optional[str]
    Weight: Optional[str]

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
            Addr=json_data.get("Addr"),
            AddrTCtrl=json_data.get("AddrTCtrl"),
            AllowedSelfAsCnt=json_data.get("AllowedSelfAsCnt"),
            Annotation=json_data.get("Annotation"),
            AsNumber=json_data.get("AsNumber"),
            Ctrl=json_data.get("Ctrl"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LocalAsn=json_data.get("LocalAsn"),
            LocalAsnPropagate=json_data.get("LocalAsnPropagate"),
            LogicalNodeProfileDn=json_data.get("LogicalNodeProfileDn"),
            NameAlias=json_data.get("NameAlias"),
            Password=json_data.get("Password"),
            PeerCtrl=json_data.get("PeerCtrl"),
            PrivateASctrl=json_data.get("PrivateASctrl"),
            RelationBgpRsPeerPfxPol=json_data.get("RelationBgpRsPeerPfxPol"),
            Ttl=json_data.get("Ttl"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


