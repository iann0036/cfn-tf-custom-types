# TF::ACI::OspfRouteSummarization

Manages ACI OSPF Route Summarization

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::OspfRouteSummarization",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#cost" title="Cost">Cost</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#interareaenabled" title="InterAreaEnabled">InterAreaEnabled</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::OspfRouteSummarization
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#cost" title="Cost">Cost</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#interareaenabled" title="InterAreaEnabled">InterAreaEnabled</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object OSPF route summarization.
- `description` - Description for for object OSPF route summarization.
- `cost` - (Optional) The OSPF Area cost for the default summary LSAs. The Area cost is used with NSSA and stub area types only. Default value: "unspecified".
- `inter_area_enabled` - (Optional) Inter area enabled flag for object OSPF route summarization.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cost

The OSPF Area cost for the default summary LSAs. The Area cost is used with NSSA and stub area types only. Default value: "unspecified".
- `inter_area_enabled` - (Optional) Inter area enabled flag for object OSPF route summarization.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for for object OSPF route summarization.
- `cost` - (Optional) The OSPF Area cost for the default summary LSAs. The Area cost is used with NSSA and stub area types only. Default value: "unspecified".
- `inter_area_enabled` - (Optional) Inter area enabled flag for object OSPF route summarization.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterAreaEnabled

Inter area enabled flag for object OSPF route summarization.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of object OSPF route summarization.
- `annotation` - (Optional) Annotation for object OSPF route summarization.
- `description` - Description for for object OSPF route summarization.
- `cost` - (Optional) The OSPF Area cost for the default summary LSAs. The Area cost is used with NSSA and stub area types only. Default value: "unspecified".
- `inter_area_enabled` - (Optional) Inter area enabled flag for object OSPF route summarization.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

The color of a policy label. Default value: "0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of object OSPF route summarization.
- `annotation` - (Optional) Annotation for object OSPF route summarization.
- `description` - Description for for object OSPF route summarization.
- `cost` - (Optional) The OSPF Area cost for the default summary LSAs. The Area cost is used with NSSA and stub area types only. Default value: "unspecified".
- `inter_area_enabled` - (Optional) Inter area enabled flag for object OSPF route summarization.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object OSPF route summarization.
- `tag` - (Optional) The color of a policy label. Default value: "0".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

