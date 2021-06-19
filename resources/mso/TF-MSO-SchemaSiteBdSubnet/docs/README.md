# TF::MSO::SchemaSiteBdSubnet

CloudFormation equivalent of mso_schema_site_bd_subnet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaSiteBdSubnet",
    "Properties" : {
        "<a href="#bdname" title="BdName">BdName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#nodefaultgateway" title="NoDefaultGateway">NoDefaultGateway</a>" : <i>Boolean</i>,
        "<a href="#querier" title="Querier">Querier</a>" : <i>Boolean</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Boolean</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaSiteBdSubnet
Properties:
    <a href="#bdname" title="BdName">BdName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#nodefaultgateway" title="NoDefaultGateway">NoDefaultGateway</a>: <i>Boolean</i>
    <a href="#querier" title="Querier">Querier</a>: <i>Boolean</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Boolean</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
</pre>

## Properties

#### BdName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDefaultGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Querier

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

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

