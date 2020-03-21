# Terraform::Datadog::IntegrationAws

CloudFormation equivalent of datadog_integration_aws

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::IntegrationAws",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#accountspecificnamespacerules" title="AccountSpecificNamespaceRules">AccountSpecificNamespaceRules</a>" : <i>[ &lt;a href=&#34;accountspecificnamespacerules.md&#34;&gt;AccountSpecificNamespaceRules&lt;/a&gt;, ... ]</i>,
        "<a href="#externalid" title="ExternalId">ExternalId</a>" : <i>String</i>,
        "<a href="#filtertags" title="FilterTags">FilterTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#hosttags" title="HostTags">HostTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::IntegrationAws
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#accountspecificnamespacerules" title="AccountSpecificNamespaceRules">AccountSpecificNamespaceRules</a>: <i>
      - &lt;a href=&#34;accountspecificnamespacerules.md&#34;&gt;AccountSpecificNamespaceRules&lt;/a&gt;</i>
    <a href="#externalid" title="ExternalId">ExternalId</a>: <i>String</i>
    <a href="#filtertags" title="FilterTags">FilterTags</a>: <i>
      - String</i>
    <a href="#hosttags" title="HostTags">HostTags</a>: <i>
      - String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountSpecificNamespaceRules

_Required_: No

_Type_: List of &lt;a href=&#34;accountspecificnamespacerules.md&#34;&gt;AccountSpecificNamespaceRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

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

#### ExternalId

Returns the &lt;code&gt;ExternalId&lt;/code&gt; value.

