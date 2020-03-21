# Terraform::OVH::MeInstallationTemplate

Use this resource to create a custom installation template available for dedicated servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::MeInstallationTemplate",
    "Properties" : {
        "<a href="#basetemplatename" title="BaseTemplateName">BaseTemplateName</a>" : <i>String</i>,
        "<a href="#defaultlanguage" title="DefaultLanguage">DefaultLanguage</a>" : <i>String</i>,
        "<a href="#removedefaultpartitionschemes" title="RemoveDefaultPartitionSchemes">RemoveDefaultPartitionSchemes</a>" : <i>Boolean</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#customization" title="Customization">Customization</a>" : <i>[ <a href="customization.md">Customization</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::MeInstallationTemplate
Properties:
    <a href="#basetemplatename" title="BaseTemplateName">BaseTemplateName</a>: <i>String</i>
    <a href="#defaultlanguage" title="DefaultLanguage">DefaultLanguage</a>: <i>String</i>
    <a href="#removedefaultpartitionschemes" title="RemoveDefaultPartitionSchemes">RemoveDefaultPartitionSchemes</a>: <i>Boolean</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#customization" title="Customization">Customization</a>: <i>
      - <a href="customization.md">Customization</a></i>
</pre>

## Properties

#### BaseTemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLanguage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveDefaultPartitionSchemes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customization

_Required_: No

_Type_: List of <a href="customization.md">Customization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailableLanguages

Returns the <code>AvailableLanguages</code> value.

#### Beta

Returns the <code>Beta</code> value.

#### BitFormat

Returns the <code>BitFormat</code> value.

#### Category

Returns the <code>Category</code> value.

#### Deprecated

Returns the <code>Deprecated</code> value.

#### Description

Returns the <code>Description</code> value.

#### Distribution

Returns the <code>Distribution</code> value.

#### Family

Returns the <code>Family</code> value.

#### Filesystems

Returns the <code>Filesystems</code> value.

#### HardRaidConfiguration

Returns the <code>HardRaidConfiguration</code> value.

#### LastModification

Returns the <code>LastModification</code> value.

#### SupportsDistributionKernel

Returns the <code>SupportsDistributionKernel</code> value.

#### SupportsGptLabel

Returns the <code>SupportsGptLabel</code> value.

#### SupportsRtm

Returns the <code>SupportsRtm</code> value.

#### SupportsSqlServer

Returns the <code>SupportsSqlServer</code> value.

#### SupportsUefi

Returns the <code>SupportsUefi</code> value.

