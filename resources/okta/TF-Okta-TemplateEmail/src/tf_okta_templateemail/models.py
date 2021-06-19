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
    DefaultLanguage: Optional[str]
    Id: Optional[str]
    Type: Optional[str]
    Translations: Optional[Sequence["_TranslationsDefinition"]]

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
            DefaultLanguage=json_data.get("DefaultLanguage"),
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
            Translations=deserialize_list(json_data.get("Translations"), TranslationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TranslationsDefinition(BaseModel):
    Language: Optional[str]
    Subject: Optional[str]
    Template: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TranslationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TranslationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Language=json_data.get("Language"),
            Subject=json_data.get("Subject"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TranslationsDefinition = TranslationsDefinition


