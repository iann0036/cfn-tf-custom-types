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
    Arn: Optional[str]
    DeleteAllPolicyResources: Optional[bool]
    ExcludeResourceTags: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    PolicyUpdateToken: Optional[str]
    RemediationEnabled: Optional[bool]
    ResourceTags: Optional[Sequence["_ResourceTagsDefinition"]]
    ResourceType: Optional[str]
    ResourceTypeList: Optional[Sequence[str]]
    ExcludeMap: Optional[Sequence["_ExcludeMapDefinition"]]
    IncludeMap: Optional[Sequence["_IncludeMapDefinition"]]
    SecurityServicePolicyData: Optional[Sequence["_SecurityServicePolicyDataDefinition"]]

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
            Arn=json_data.get("Arn"),
            DeleteAllPolicyResources=json_data.get("DeleteAllPolicyResources"),
            ExcludeResourceTags=json_data.get("ExcludeResourceTags"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyUpdateToken=json_data.get("PolicyUpdateToken"),
            RemediationEnabled=json_data.get("RemediationEnabled"),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), ResourceTagsDefinition),
            ResourceType=json_data.get("ResourceType"),
            ResourceTypeList=json_data.get("ResourceTypeList"),
            ExcludeMap=deserialize_list(json_data.get("ExcludeMap"), ExcludeMapDefinition),
            IncludeMap=deserialize_list(json_data.get("IncludeMap"), IncludeMapDefinition),
            SecurityServicePolicyData=deserialize_list(json_data.get("SecurityServicePolicyData"), SecurityServicePolicyDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTagsDefinition = ResourceTagsDefinition


@dataclass
class ExcludeMapDefinition(BaseModel):
    Account: Optional[Sequence[str]]
    Orgunit: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeMapDefinition"]:
        if not json_data:
            return None
        return cls(
            Account=json_data.get("Account"),
            Orgunit=json_data.get("Orgunit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeMapDefinition = ExcludeMapDefinition


@dataclass
class IncludeMapDefinition(BaseModel):
    Account: Optional[Sequence[str]]
    Orgunit: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IncludeMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludeMapDefinition"]:
        if not json_data:
            return None
        return cls(
            Account=json_data.get("Account"),
            Orgunit=json_data.get("Orgunit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludeMapDefinition = IncludeMapDefinition


@dataclass
class SecurityServicePolicyDataDefinition(BaseModel):
    ManagedServiceData: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityServicePolicyDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityServicePolicyDataDefinition"]:
        if not json_data:
            return None
        return cls(
            ManagedServiceData=json_data.get("ManagedServiceData"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityServicePolicyDataDefinition = SecurityServicePolicyDataDefinition


