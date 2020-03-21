# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    GraphCid: Optional[str]
    Title: Optional[str]
    Overlays: Optional[Sequence["_Overlays"]]
    DataOpts: Optional[Sequence["_DataOpts"]]
    UiSpecs: Optional[Sequence["_UiSpecs"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            GraphCid=json_data.get("GraphCid"),
            Title=json_data.get("Title"),
            Overlays=json_data.get("Overlays"),
            DataOpts=json_data.get("DataOpts"),
            UiSpecs=json_data.get("UiSpecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Overlays:
    Id: Optional[str]
    DataOpts: Optional[Sequence["_DataOpts"]]
    UiSpecs: Optional[Sequence["_UiSpecs"]]

    @classmethod
    def _deserialize(
        cls: Type["_Overlays"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Overlays"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            DataOpts=json_data.get("DataOpts"),
            UiSpecs=json_data.get("UiSpecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Overlays = Overlays


@dataclass
class DataOpts:
    GraphTitle: Optional[str]
    GraphUuid: Optional[str]
    XShift: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataOpts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataOpts"]:
        if not json_data:
            return None
        return cls(
            GraphTitle=json_data.get("GraphTitle"),
            GraphUuid=json_data.get("GraphUuid"),
            XShift=json_data.get("XShift"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataOpts = DataOpts


@dataclass
class UiSpecs:
    Decouple: Optional[bool]
    Id: Optional[str]
    Label: Optional[str]
    Type: Optional[str]
    Z: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UiSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UiSpecs"]:
        if not json_data:
            return None
        return cls(
            Decouple=json_data.get("Decouple"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Type=json_data.get("Type"),
            Z=json_data.get("Z"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UiSpecs = UiSpecs


