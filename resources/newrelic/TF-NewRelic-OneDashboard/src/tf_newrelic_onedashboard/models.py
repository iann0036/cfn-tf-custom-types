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
    AccountId: Optional[float]
    Description: Optional[str]
    Guid: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Permalink: Optional[str]
    Permissions: Optional[str]
    Page: Optional[Sequence["_PageDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            Description=json_data.get("Description"),
            Guid=json_data.get("Guid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Permalink=json_data.get("Permalink"),
            Permissions=json_data.get("Permissions"),
            Page=deserialize_list(json_data.get("Page"), PageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PageDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    WidgetArea: Optional[Sequence["_WidgetAreaDefinition"]]
    WidgetBar: Optional[Sequence["_WidgetBarDefinition"]]
    WidgetBillboard: Optional[Sequence["_WidgetBillboardDefinition"]]
    WidgetBullet: Optional[Sequence["_WidgetBulletDefinition"]]
    WidgetFunnel: Optional[Sequence["_WidgetFunnelDefinition"]]
    WidgetHeatmap: Optional[Sequence["_WidgetHeatmapDefinition"]]
    WidgetHistogram: Optional[Sequence["_WidgetHistogramDefinition"]]
    WidgetJson: Optional[Sequence["_WidgetJsonDefinition"]]
    WidgetLine: Optional[Sequence["_WidgetLineDefinition"]]
    WidgetMarkdown: Optional[Sequence["_WidgetMarkdownDefinition"]]
    WidgetPie: Optional[Sequence["_WidgetPieDefinition"]]
    WidgetTable: Optional[Sequence["_WidgetTableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PageDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            WidgetArea=deserialize_list(json_data.get("WidgetArea"), WidgetAreaDefinition),
            WidgetBar=deserialize_list(json_data.get("WidgetBar"), WidgetBarDefinition),
            WidgetBillboard=deserialize_list(json_data.get("WidgetBillboard"), WidgetBillboardDefinition),
            WidgetBullet=deserialize_list(json_data.get("WidgetBullet"), WidgetBulletDefinition),
            WidgetFunnel=deserialize_list(json_data.get("WidgetFunnel"), WidgetFunnelDefinition),
            WidgetHeatmap=deserialize_list(json_data.get("WidgetHeatmap"), WidgetHeatmapDefinition),
            WidgetHistogram=deserialize_list(json_data.get("WidgetHistogram"), WidgetHistogramDefinition),
            WidgetJson=deserialize_list(json_data.get("WidgetJson"), WidgetJsonDefinition),
            WidgetLine=deserialize_list(json_data.get("WidgetLine"), WidgetLineDefinition),
            WidgetMarkdown=deserialize_list(json_data.get("WidgetMarkdown"), WidgetMarkdownDefinition),
            WidgetPie=deserialize_list(json_data.get("WidgetPie"), WidgetPieDefinition),
            WidgetTable=deserialize_list(json_data.get("WidgetTable"), WidgetTableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PageDefinition = PageDefinition


@dataclass
class WidgetAreaDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetAreaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetAreaDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetAreaDefinition = WidgetAreaDefinition


@dataclass
class NrqlQueryDefinition(BaseModel):
    AccountId: Optional[float]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NrqlQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NrqlQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NrqlQueryDefinition = NrqlQueryDefinition


@dataclass
class WidgetBarDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    LinkedEntityGuids: Optional[Sequence[str]]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetBarDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetBarDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            LinkedEntityGuids=json_data.get("LinkedEntityGuids"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetBarDefinition = WidgetBarDefinition


@dataclass
class WidgetBillboardDefinition(BaseModel):
    Column: Optional[float]
    Critical: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Warning: Optional[float]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetBillboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetBillboardDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Critical=json_data.get("Critical"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Warning=json_data.get("Warning"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetBillboardDefinition = WidgetBillboardDefinition


@dataclass
class WidgetBulletDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Limit: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetBulletDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetBulletDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Limit=json_data.get("Limit"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetBulletDefinition = WidgetBulletDefinition


@dataclass
class WidgetFunnelDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetFunnelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetFunnelDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetFunnelDefinition = WidgetFunnelDefinition


@dataclass
class WidgetHeatmapDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetHeatmapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetHeatmapDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetHeatmapDefinition = WidgetHeatmapDefinition


@dataclass
class WidgetHistogramDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetHistogramDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetHistogramDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetHistogramDefinition = WidgetHistogramDefinition


@dataclass
class WidgetJsonDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetJsonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetJsonDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetJsonDefinition = WidgetJsonDefinition


@dataclass
class WidgetLineDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetLineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetLineDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetLineDefinition = WidgetLineDefinition


@dataclass
class WidgetMarkdownDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Text: Optional[str]
    Title: Optional[str]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetMarkdownDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetMarkdownDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Text=json_data.get("Text"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetMarkdownDefinition = WidgetMarkdownDefinition


@dataclass
class WidgetPieDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    LinkedEntityGuids: Optional[Sequence[str]]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetPieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetPieDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            LinkedEntityGuids=json_data.get("LinkedEntityGuids"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetPieDefinition = WidgetPieDefinition


@dataclass
class WidgetTableDefinition(BaseModel):
    Column: Optional[float]
    Height: Optional[float]
    LinkedEntityGuids: Optional[Sequence[str]]
    Row: Optional[float]
    Title: Optional[str]
    Width: Optional[float]
    NrqlQuery: Optional[Sequence["_NrqlQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetTableDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            LinkedEntityGuids=json_data.get("LinkedEntityGuids"),
            Row=json_data.get("Row"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            NrqlQuery=deserialize_list(json_data.get("NrqlQuery"), NrqlQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetTableDefinition = WidgetTableDefinition


