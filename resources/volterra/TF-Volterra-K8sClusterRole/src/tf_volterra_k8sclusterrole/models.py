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
    Yaml: Optional[str]
    K8sClusterRoleSelector: Optional[Sequence["_K8sClusterRoleSelectorDefinition"]]
    PolicyRuleList: Optional[Sequence["_PolicyRuleListDefinition"]]

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
            Yaml=json_data.get("Yaml"),
            K8sClusterRoleSelector=deserialize_list(json_data.get("K8sClusterRoleSelector"), K8sClusterRoleSelectorDefinition),
            PolicyRuleList=deserialize_list(json_data.get("PolicyRuleList"), PolicyRuleListDefinition),
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
class K8sClusterRoleSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_K8sClusterRoleSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_K8sClusterRoleSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_K8sClusterRoleSelectorDefinition = K8sClusterRoleSelectorDefinition


@dataclass
class PolicyRuleListDefinition(BaseModel):
    PolicyRule: Optional[Sequence["_PolicyRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyRuleListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyRuleListDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyRule=deserialize_list(json_data.get("PolicyRule"), PolicyRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyRuleListDefinition = PolicyRuleListDefinition


@dataclass
class PolicyRuleDefinition(BaseModel):
    NonResourceUrlList: Optional[Sequence["_NonResourceUrlListDefinition"]]
    ResourceList: Optional[Sequence["_ResourceListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            NonResourceUrlList=deserialize_list(json_data.get("NonResourceUrlList"), NonResourceUrlListDefinition),
            ResourceList=deserialize_list(json_data.get("ResourceList"), ResourceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyRuleDefinition = PolicyRuleDefinition


@dataclass
class NonResourceUrlListDefinition(BaseModel):
    Urls: Optional[Sequence[str]]
    Verbs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NonResourceUrlListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NonResourceUrlListDefinition"]:
        if not json_data:
            return None
        return cls(
            Urls=json_data.get("Urls"),
            Verbs=json_data.get("Verbs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NonResourceUrlListDefinition = NonResourceUrlListDefinition


@dataclass
class ResourceListDefinition(BaseModel):
    ApiGroups: Optional[Sequence[str]]
    ResourceInstances: Optional[Sequence[str]]
    ResourceTypes: Optional[Sequence[str]]
    Verbs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceListDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiGroups=json_data.get("ApiGroups"),
            ResourceInstances=json_data.get("ResourceInstances"),
            ResourceTypes=json_data.get("ResourceTypes"),
            Verbs=json_data.get("Verbs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceListDefinition = ResourceListDefinition


