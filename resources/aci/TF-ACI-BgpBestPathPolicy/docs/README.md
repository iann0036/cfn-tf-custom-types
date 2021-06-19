# TF::ACI::BgpBestPathPolicy

Manages ACI BGP Best Path Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::BgpBestPathPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#ctrl" title="Ctrl">Ctrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::BgpBestPathPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#ctrl" title="Ctrl">Ctrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object BGP Best Path Policy.
- `description` - (Optional) Description for object BGP Best Path Policy.
- `ctrl` - (Optional) The control state.
Allowed values: "asPathMultipathRelax", "0". Default Value: "0".
- `name_alias` - (Optional) Name alias for object BGP Best Path Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ctrl

The control state.
Allowed values: "asPathMultipathRelax", "0". Default Value: "0".
- `name_alias` - (Optional) Name alias for object BGP Best Path Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object BGP Best Path Policy.
- `ctrl` - (Optional) The control state.
Allowed values: "asPathMultipathRelax", "0". Default Value: "0".
- `name_alias` - (Optional) Name alias for object BGP Best Path Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Object BGP Best Path Policy.
- `annotation` - (Optional) Annotation for object BGP Best Path Policy.
- `description` - (Optional) Description for object BGP Best Path Policy.
- `ctrl` - (Optional) The control state.
Allowed values: "asPathMultipathRelax", "0". Default Value: "0".
- `name_alias` - (Optional) Name alias for object BGP Best Path Policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object BGP Best Path Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of Object BGP Best Path Policy.
- `annotation` - (Optional) Annotation for object BGP Best Path Policy.
- `description` - (Optional) Description for object BGP Best Path Policy.
- `ctrl` - (Optional) The control state.
Allowed values: "asPathMultipathRelax", "0". Default Value: "0".
- `name_alias` - (Optional) Name alias for object BGP Best Path Policy.

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

