# Terraform::Vault::GenericEndpoint

CloudFormation equivalent of vault_generic_endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::GenericEndpoint",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#datajson" title="DataJson">DataJson</a>" : <i>String</i>,
        "<a href="#disabledelete" title="DisableDelete">DisableDelete</a>" : <i>Boolean</i>,
        "<a href="#disableread" title="DisableRead">DisableRead</a>" : <i>Boolean</i>,
        "<a href="#ignoreabsentfields" title="IgnoreAbsentFields">IgnoreAbsentFields</a>" : <i>Boolean</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#writedata" title="WriteData">WriteData</a>" : <i>[ &lt;a href=&#34;writedata.md&#34;&gt;WriteData&lt;/a&gt;, ... ]</i>,
        "<a href="#writedatajson" title="WriteDataJson">WriteDataJson</a>" : <i>String</i>,
        "<a href="#writefields" title="WriteFields">WriteFields</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::GenericEndpoint
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#datajson" title="DataJson">DataJson</a>: <i>String</i>
    <a href="#disabledelete" title="DisableDelete">DisableDelete</a>: <i>Boolean</i>
    <a href="#disableread" title="DisableRead">DisableRead</a>: <i>Boolean</i>
    <a href="#ignoreabsentfields" title="IgnoreAbsentFields">IgnoreAbsentFields</a>: <i>Boolean</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#writedata" title="WriteData">WriteData</a>: <i>
      - &lt;a href=&#34;writedata.md&#34;&gt;WriteData&lt;/a&gt;</i>
    <a href="#writedatajson" title="WriteDataJson">WriteDataJson</a>: <i>String</i>
    <a href="#writefields" title="WriteFields">WriteFields</a>: <i>
      - String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataJson

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRead

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreAbsentFields

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteData

_Required_: No

_Type_: List of &lt;a href=&#34;writedata.md&#34;&gt;WriteData&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteDataJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteFields

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### WriteData

Returns the &lt;code&gt;WriteData&lt;/code&gt; value.

#### WriteDataJson

Returns the &lt;code&gt;WriteDataJson&lt;/code&gt; value.

