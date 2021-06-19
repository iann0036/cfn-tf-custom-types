# TF::MSO::SchemaTemplateExternalEpg

CloudFormation equivalent of mso_schema_template_external_epg

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaTemplateExternalEpg",
    "Properties" : {
        "<a href="#anpname" title="AnpName">AnpName</a>" : <i>String</i>,
        "<a href="#anpschemaid" title="AnpSchemaId">AnpSchemaId</a>" : <i>String</i>,
        "<a href="#anptemplatename" title="AnpTemplateName">AnpTemplateName</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#externalepgname" title="ExternalEpgName">ExternalEpgName</a>" : <i>String</i>,
        "<a href="#externalepgtype" title="ExternalEpgType">ExternalEpgType</a>" : <i>String</i>,
        "<a href="#includeinpreferredgroup" title="IncludeInPreferredGroup">IncludeInPreferredGroup</a>" : <i>Boolean</i>,
        "<a href="#l3outname" title="L3outName">L3outName</a>" : <i>String</i>,
        "<a href="#l3outschemaid" title="L3outSchemaId">L3outSchemaId</a>" : <i>String</i>,
        "<a href="#l3outtemplatename" title="L3outTemplateName">L3outTemplateName</a>" : <i>String</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#selectorip" title="SelectorIp">SelectorIp</a>" : <i>String</i>,
        "<a href="#selectorname" title="SelectorName">SelectorName</a>" : <i>String</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>[ String, ... ]</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#vrfname" title="VrfName">VrfName</a>" : <i>String</i>,
        "<a href="#vrfschemaid" title="VrfSchemaId">VrfSchemaId</a>" : <i>String</i>,
        "<a href="#vrftemplatename" title="VrfTemplateName">VrfTemplateName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaTemplateExternalEpg
Properties:
    <a href="#anpname" title="AnpName">AnpName</a>: <i>String</i>
    <a href="#anpschemaid" title="AnpSchemaId">AnpSchemaId</a>: <i>String</i>
    <a href="#anptemplatename" title="AnpTemplateName">AnpTemplateName</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#externalepgname" title="ExternalEpgName">ExternalEpgName</a>: <i>String</i>
    <a href="#externalepgtype" title="ExternalEpgType">ExternalEpgType</a>: <i>String</i>
    <a href="#includeinpreferredgroup" title="IncludeInPreferredGroup">IncludeInPreferredGroup</a>: <i>Boolean</i>
    <a href="#l3outname" title="L3outName">L3outName</a>: <i>String</i>
    <a href="#l3outschemaid" title="L3outSchemaId">L3outSchemaId</a>: <i>String</i>
    <a href="#l3outtemplatename" title="L3outTemplateName">L3outTemplateName</a>: <i>String</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#selectorip" title="SelectorIp">SelectorIp</a>: <i>String</i>
    <a href="#selectorname" title="SelectorName">SelectorName</a>: <i>String</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>
      - String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#vrfname" title="VrfName">VrfName</a>: <i>String</i>
    <a href="#vrfschemaid" title="VrfSchemaId">VrfSchemaId</a>: <i>String</i>
    <a href="#vrftemplatename" title="VrfTemplateName">VrfTemplateName</a>: <i>String</i>
</pre>

## Properties

#### AnpName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnpSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnpTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalEpgName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalEpgType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeInPreferredGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3outName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3outSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3outTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectorIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectorName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

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

