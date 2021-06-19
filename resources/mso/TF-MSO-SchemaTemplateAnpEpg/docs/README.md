# TF::MSO::SchemaTemplateAnpEpg

CloudFormation equivalent of mso_schema_template_anp_epg

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaTemplateAnpEpg",
    "Properties" : {
        "<a href="#anpname" title="AnpName">AnpName</a>" : <i>String</i>,
        "<a href="#bdname" title="BdName">BdName</a>" : <i>String</i>,
        "<a href="#bdschemaid" title="BdSchemaId">BdSchemaId</a>" : <i>String</i>,
        "<a href="#bdtemplatename" title="BdTemplateName">BdTemplateName</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#intersitemulticastsource" title="IntersiteMulticastSource">IntersiteMulticastSource</a>" : <i>Boolean</i>,
        "<a href="#intraepg" title="IntraEpg">IntraEpg</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preferredgroup" title="PreferredGroup">PreferredGroup</a>" : <i>Boolean</i>,
        "<a href="#proxyarp" title="ProxyArp">ProxyArp</a>" : <i>Boolean</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#usegepg" title="UsegEpg">UsegEpg</a>" : <i>Boolean</i>,
        "<a href="#vrfname" title="VrfName">VrfName</a>" : <i>String</i>,
        "<a href="#vrfschemaid" title="VrfSchemaId">VrfSchemaId</a>" : <i>String</i>,
        "<a href="#vrftemplatename" title="VrfTemplateName">VrfTemplateName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaTemplateAnpEpg
Properties:
    <a href="#anpname" title="AnpName">AnpName</a>: <i>String</i>
    <a href="#bdname" title="BdName">BdName</a>: <i>String</i>
    <a href="#bdschemaid" title="BdSchemaId">BdSchemaId</a>: <i>String</i>
    <a href="#bdtemplatename" title="BdTemplateName">BdTemplateName</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#intersitemulticastsource" title="IntersiteMulticastSource">IntersiteMulticastSource</a>: <i>Boolean</i>
    <a href="#intraepg" title="IntraEpg">IntraEpg</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preferredgroup" title="PreferredGroup">PreferredGroup</a>: <i>Boolean</i>
    <a href="#proxyarp" title="ProxyArp">ProxyArp</a>: <i>Boolean</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#usegepg" title="UsegEpg">UsegEpg</a>: <i>Boolean</i>
    <a href="#vrfname" title="VrfName">VrfName</a>: <i>String</i>
    <a href="#vrfschemaid" title="VrfSchemaId">VrfSchemaId</a>: <i>String</i>
    <a href="#vrftemplatename" title="VrfTemplateName">VrfTemplateName</a>: <i>String</i>
</pre>

## Properties

#### AnpName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BdName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BdSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BdTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntersiteMulticastSource

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntraEpg

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyArp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsegEpg

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfTemplateName

_Required_: No

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

