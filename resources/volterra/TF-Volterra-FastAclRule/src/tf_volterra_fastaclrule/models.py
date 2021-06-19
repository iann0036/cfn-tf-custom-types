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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    IpPrefixSet: Optional[Sequence["_IpPrefixSetDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]
    Prefix: Optional[Sequence["_PrefixDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            IpPrefixSet=deserialize_list(json_data.get("IpPrefixSet"), IpPrefixSetDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            Prefix=deserialize_list(json_data.get("Prefix"), PrefixDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ActionDefinition(BaseModel):
    SimpleAction: Optional[str]
    PolicerAction: Optional[Sequence["_PolicerActionDefinition"]]
    ProtocolPolicerAction: Optional[Sequence["_ProtocolPolicerActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            SimpleAction=json_data.get("SimpleAction"),
            PolicerAction=deserialize_list(json_data.get("PolicerAction"), PolicerActionDefinition),
            ProtocolPolicerAction=deserialize_list(json_data.get("ProtocolPolicerAction"), ProtocolPolicerActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class PolicerActionDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicerActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicerActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicerActionDefinition = PolicerActionDefinition


@dataclass
class RefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefDefinition = RefDefinition


@dataclass
class ProtocolPolicerActionDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolPolicerActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolPolicerActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolPolicerActionDefinition = ProtocolPolicerActionDefinition


@dataclass
class IpPrefixSetDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixSetDefinition = IpPrefixSetDefinition


@dataclass
class PortDefinition(BaseModel):
    All: Optional[bool]
    Dns: Optional[bool]
    UserDefined: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Dns=json_data.get("Dns"),
            UserDefined=json_data.get("UserDefined"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


@dataclass
class PrefixDefinition(BaseModel):
    Prefix: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixDefinition = PrefixDefinition


